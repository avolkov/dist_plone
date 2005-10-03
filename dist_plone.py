# Plone Distribution Script
# by Simon Eisenmann, 2004.
# for questions contact simon@longsleep.org
#
# $Rev: 1.15 $
# $Date: 2004-05-11 19:14:24 +0200 (Tue, 11 May 2004) $
"""
This script:

 1) Gets the PloneBase-X.Y tarball (contains only CMFPlone dir, nothing
    else) from SF.net (I would like to move it away from SF, though - since
    it's not meant for public consumption).

 2) Adds the Plone Core specified products, and creates PloneCore-X.Y

 3) Adds the cross-platform additions that consitute Plone, and creates
    Plone-X.Y

 The installers are normally built on top of [3]. Plone Core[2] is for
 people who just want the minimal Plone install with minimal dependencies,
 aka. People Who Know What They Want.

 Which means any platform-specific installers:

 a) Get Plone-X.Y.tgz [3]

 b) Add their platform-specific additions (PIL, win32all, etc)

 c) Create the installer

 Read http://plone.org/development/teams/release/ for definitions and
 further explanations.

 -- Alexander Limi
"""

import itarfile as tarfile # NOTE: pythons tarfile is borked, itarfile is a patched version
import zipfile
import time
import os, getopt, sys
import tempfile, urllib

from distutils.dir_util import mkpath, copy_tree, remove_tree
from distutils.file_util import move_file

from imp import find_module, load_module

__version__ = "$Revision: 1.15 $"[11:-1]

class Software:
    """ general software """
    type = 'Software'

    name = None
    download_url = None
    archive_rename = None
    productdir_rename = None
    filename = None
    parent = None

    destination = 'downloads'

    def __init__(self, name, download_url, productdir=None, archive_rename=None):
        self.name = name
        self.download_url = download_url
        self.productdir_rename = productdir
        self.archive_rename = archive_rename
        

class Bundle(Software):
    """ a archive which contains multiple other parts """

    type = 'Bundle'
    items = None

    destination = 'downloads'

    def __init__(self, name, download_url, mapping):
        # define a subfolder -> class mapping here to
        # specify the contents of this bundle

        Software.__init__(self, name, download_url)

        self.items = []
        for n, k in mapping.items():
            c = k(n, None)
            c.parent = self # set ourselfs as source for this file
            self.items.append(c)


class PyModule(Software):
    """ python module """

    type = 'PyModule'
    destination = 'lib/python'
    pass


class ZProduct(Software):
    """ zope product """

    type = 'ZProduct'
    destination = 'lib/python/Products'
    pass


class Parameters:

    _eaten = []

    def feed(self, p, arg):
        setattr(self, p, arg)
        if not self.given(p): self._eaten.append(p)

    def given(self, p):
        return p in self._eaten


USAGE="""Plone Distribution script %s.
Usage: python2.3 dist_plone.py [--download|--build] [OPTION]...

%sParameters:
  --help                   display this usage information and exit.
  --target=TARGET          selects package definition to use.
  --modules=DIRECTORY      directory where target module is to be found (defaults to dist_plone.platforms).
  --dest=DESTINATION       destination folder (default is ./build).
  --core                   use minimal mode.
  --build                  builds tarball mode.
  --download               download only mode.

Mail bug reports and suggestions to <simon@longsleep.org>.
"""


class Plone:

    version = None

    parameters = None
    data = []

    # getopt command line parameters
    short_options = ""
    long_options = ["help", "target=", "modules=", "dest=", "core", "build", "download"]

    def setup(self):
        self.basefolder = tempfile.mkdtemp()
        if not self.parameters.given('dest'):
            dest = os.path.join(self.parameters.dest, 'build')
            try: os.mkdir(dest)
            except: pass
            self.parameters.feed('dest', dest)

    def run(self, command):
        command = " ".join(command)
        print "command is %s" % repr(command)
        os.system(command)

    def usage(self, s=''):
        print USAGE % (__version__.strip(), s)

    def main(self):

        try:
            opts, args = getopt.getopt(sys.argv[1:],
                                       self.short_options,
                                       self.long_options,
                                       )
        except getopt.GetoptError:
            # print help information and exit
            self.usage()
            sys.exit(1)

        # default parameter values
        dest = os.getcwd()
        target = 'independent'
        modules = None
        parameters = Parameters()
        parameters.dest = dest
        parameters.target = target
        parameters.modules = modules

        # go through each cmd line argument
        for cmd, arg in opts:

            if cmd in ('--help',):
                self.usage()
                sys.exit()

            if cmd in ('--dest',):
                dest = arg
                assert os.path.isdir(dest)
                parameters.feed('dest', dest)

            if cmd in ('--core',):
                core = True
                parameters.feed('core', core)

            if cmd in ('--build',):
                build = True
                parameters.feed('build', build)

            if cmd in ('--target',):
                target = arg
                parameters.feed('target', target)
            
            if cmd in ('--modules',):
                modules = arg
                parameters.feed('modules', modules)

            if cmd in('--download',):
                download = True
                parameters.feed('download', download)

        # check for errors
        errors = []
        if parameters.given('download') and parameters.given('build'):
            errors.append('Either --download or --build mode is allowed')
        if not parameters.given('download') and not parameters.given('build'):
            errors.append('You need to give either --download or --build')

        # get distribution
        if not modules:
            load='platforms.%s' % target
            try: Distribution = __import__(load, globals(), locals(), 'Distribution')
            except:
                raise
                Distribution = None
        else:
            try:
                fp, pathname, description = find_module(target, [modules])
                try:
                    Distribution = load_module(target, fp, pathname, description)
                finally:
                    if fp: fp.close()
            except ImportError:
                errors.append("Target module '%s' cannot be found in '%s'" % (target, modules))
                Distribution = None
        if Distribution:
            Distribution = Distribution.Distribution
            dist=Distribution()
        else:
            errors.append('Platform %s is not supported' % target)

        # got errors?
        if len(errors):
            errors = map(lambda x: 'GetoptError: %s.' % str(x), errors)
            errors = '\n'.join(errors)
            errors = '%s\n\n' % errors
            self.usage(errors)
            sys.exit(1)


        parameters.feed('dist', dist)
        # remember parameters
        self.parameters = parameters

        self.setup()
        self.download()
        self.build()
        self.cleanup()


    def download(self):

        download_destination = self.basefolder
        if not self.parameters.given('build') and self.parameters.given('dest'):
            download_destination=self.parameters.dest

        contents = os.path.join(download_destination, 'CONTENTS.txt')
        contents = open(contents, "w")
        contents.write("The following packages were downloaded at %s.\n" % time.asctime())

        data = []
        def dl_callback(ob):
            print "Retrieving %s.\n" % ob.name,
            print "--> %s" % ob.download_url
            if ob.archive_rename:
                filename = ob.archive_rename
            else:
                filename = os.path.split(ob.download_url)[1]
            print "to:", filename
            filename = os.path.join(download_destination, filename)
            urllib.urlretrieve(ob.download_url, filename)
            ob.filename=filename
            contents.write("%s - %s\n" % (ob.name, ob.download_url))
            data.append(ob)

        # walk with our callback
        self.walk(dl_callback)

        # close log file
        contents.close()

        # store our data
        self.data = data


    def walk(self, callback):

        dist = self.parameters.dist
        walk = ('core',)
        if not self.parameters.given('core'): 
	    walk=walk+('addons', )

        for w in walk:
            cur = getattr(dist, w, [])
            for c in cur:
                callback(c)


    def build(self):

        if not self.parameters.given('build'): return

        got = self.data

        items = []
        def expand(ob):
            if hasattr(ob,  'items'):
                for item in ob.items:
                    expand(item)
            else:
                items.append(ob)

        # expand bundles
        map(lambda x: expand(x), got)

        # check if we have products only
        items = map(lambda x: (x.type, x), items)

        # check if we only got products
        products = filter(lambda x: x[0] == 'ZProduct', items)
        products = len(products) == len(items)

        if products:
            # if we only have products reset their destination
            for ob in items:
                ob[1].destination=''
        else: pass
        items = map(lambda x: x[1], items)

        # move stuff to their destinations
        for ob in items:

            destination = os.path.join(self.basefolder, ob.destination)
            move = None
            visible_name = ob.name

            search = None
            if ob.parent:
                search = ob.name
                ob=ob.parent
                move=os.path.join(destination, search)
                destination=os.path.join(self.basefolder, ob.destination)

            filename = ob.filename

            # make the path (including all anchestors)
            mkpath(destination, verbose=1)

            # extract the files
            print "Processing %s %s\n%s" % (ob.type, visible_name, filename)

            # determine type
            if tarfile.is_tarfile(filename):
                ar = tarfile.TarFileCompat(filename,'r',tarfile.TAR_GZIPPED)
            elif zipfile.is_zipfile(filename):
                ar = zipfile.ZipFile(filename)
            else:
                raise IOError, "file '%s' is of unusable archive type. Only ZIP and compressed TAR files can be handled." % filename
                
            # do extraction
            productdir_rename = ob.productdir_rename
            base=''
            for f in ar.namelist():
                if not os.path.split(f)[1]: continue   # zipfile returns dirs, tarfile compat does not. ignore dir entries.
                need=1
                if search:                     # do we need to include this directory?
                    need=0
                    name = f.split('/')
                    if len(name):
                        if name[0] == search:
                            need=1
                        elif len(name)>1 and name[1] == search:
                            need=1
                if need:
                    try: base=name[0]
                    except: pass
                    
                    # do Product directory rename if needed
                    if productdir_rename and f.find(productdir_rename) == 0:
                        new_f = f[len(productdir_rename)+1:]
                        new_f = os.path.join(ob.name, new_f)
                        ext_fname = os.path.join(destination,new_f)
                    else:
                        ext_fname = os.path.join(destination,f)
                        
                    # make destination directories and do extraction
                    try: os.makedirs(os.path.split(ext_fname)[0])
                    except OSError: pass
                    data = ar.read(f)
                    dest = open(ext_fname,'w')
                    dest.write(data)
                    dest.close()
                else: continue

            # close archive file
            ar.close()

            # move directory if needed
            if move:
                source = os.path.join(destination,base,search)
                destination = move
                copy_tree(source, destination)
                remove_tree(os.path.split(source)[0])
            else:
                destination = os.path.join(destination, ob.name)

            # XXX: hack PloneTranslations i18n folder to be inside CMFPlone
            # XXX: remove this hack as soon as we stop putting i18n into CMFPlone
            #if visible_name == 'PloneTranslations':
            #    s = os.path.join(destination, 'i18n')
            #    d = os.path.join(destination, '..', 'CMFPlone', 'i18n')
            #    copy_tree(s, d)

            # check version.txt
            contents = os.listdir(destination)
            check = map(lambda x: x.lower(), contents)
            try: index=check.index('version.txt')
            except: index = []
            if index != []:
                # found a version
                version = contents[index]
                fp = open(os.path.join(destination, version), 'r')
                version = fp.read().strip()
                fp.close()
                print "--> Version %s." % str(version)
            else:
                version = 'unkown'
                print "--> NO VERSION."

            # store version
            if visible_name in ('CMFPlone', ):
                # XXX: hack Plone package version
                version = version.split()[0]
                self.version = version
                print "--> Used as Plone Package Version."

        # write README.txt
        fp = open(os.path.join(self.basefolder, 'README.txt'), 'w')
        fp.write(self.parameters.dist.readme)
        fp.close()

        # cleanup for packaging
        for ob in self.data:
            filename = ob.filename
            os.unlink(filename)

        # check for empty folders in base
        for f in os.listdir(self.basefolder):
            f=os.path.join(self.basefolder, f)
            if not os.path.isdir(f): continue
            else:
                if not len(os.listdir(f)):
                    # remove empty folders
                    remove_tree(f)  

        # XXX: hack
        # actually remove PloneTranslations
        #if "PloneTranslations" in os.listdir(self.basefolder):
        #    f = os.path.join(self.basefolder, "PloneTranslations")
        #    remove_tree(f)
        
        # create new package
        name = getattr(self.parameters.dist, 'name', 'Plone')
        version = getattr(self.parameters.dist, 'version', self.version)
        if self.parameters.given('core'): name="%sCore" % name
        target = self.parameters.dist.target.lower()
        name = "%s-%s" % (name, version)
        if target not in ('independent',):
            name="%s-%s" % (name, target)
        filename = "%s.tar.gz" % name
        print "Creating Tarball %s." % filename
        filename = os.path.join(self.parameters.dest, filename)

        # make tar
        tar = tarfile.open(filename, 'w:gz')
        tar.posix = False
        tar.add(self.basefolder, '/%s' % name)
        tar.close()

        print "Wrote Tarball to %s." % filename



    def cleanup(self):
        print "Cleaning up %s." % self.basefolder
        remove_tree(self.basefolder)
        pass

# main class
if __name__ == '__main__':
    plone=Plone()
    plone.main()


