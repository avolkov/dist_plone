# Plone packaging script, by Simon Eisenmann, 2004.
# 
# This script:
#  
# 1) Gets the PloneBase-X.Y tarball (contains only CMFPlone dir, nothing 
#    else) from SF.net (I would like to move it away from SF, though - since
#    it's not meant for public consumption).
#  
# 2) Adds the Plone Core specified products, and creates PloneCore-X.Y
#  
# 3) Adds the cross-platform additions that consitute Plone, and creates 
#    Plone-X.Y
#  
# The installers are normally built on top of [3]. Plone Core[2] is for 
# people who just want the minimal Plone install with minimal dependencies, 
# aka. People Who Know What They Want.
#  
# Which means any platform-specific installers:
#  
# a) Get Plone-X.Y.tgz [3]
# 
# b) Add their platform-specific additions (PIL, win32all, etc)
# 
# c) Create the installer
#
# Read http://plone.org/development/teams/release/ for definitions and 
# further explanations.
#
# -- Alexander Limi

import tarfile
import time
import os, getopt, sys
import tempfile, urllib

from distutils.dir_util import mkpath, copy_tree, remove_tree
from distutils.file_util import move_file


class Software:
    """ general software """
    type = 'Software'
                                                                                                                             
    name = None
    download_url = None
    filename = None
    parent = None

    destination = 'downloads'
                                                                                                                             
    def __init__(self, name, download_url):
        self.name = name
        self.download_url = download_url



class Bundle(Software):
    """ a archive which contains multiple other parts """

    type = 'Bundle'
    items = []

    destination = 'downloads'

    def __init__(self, name, download_url, mapping):
        # define a subfolder -> class mapping here to 
        # specify the contents of this bundle

        Software.__init__(self, name, download_url)

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


class Plone:

    parameters = None
    data = []

    # getopt command line parameters
    short_options = ""
    long_options = ["help", "target=", "dest=", "core", "build"]

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

    def usage(self):
        print "Write me."

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
        parameters = Parameters()
        parameters.dest = dest
        parameters.target = target

        # go through each cmd line argument
        for cmd, arg in opts:

            if cmd in ('--help',):
                self.usage()
                sys.exit()

            if cmd in ('--dest',): 
                dest = arg
                assert os.isdir(dest)
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

        # get distribution    
        load='platforms.%s' % target
        try: Distribution = __import__(load, globals(), locals(), 'Distribution')
        except: 
            raise
            Distribution = None
        if Distribution:
            print "Distribution", repr(Distribution)
            Distribution = Distribution.Distribution
            dist=Distribution()
        else:
            raise getopt.GetoptError, "Platform %s is not supported." % target

                
        parameters.feed('dist', dist)
        # remember parameters
        self.parameters = parameters 

        self.setup()
        self.download()
        self.build()
        self.cleanup()


    def download(self):

        download_destination = self.basefolder
        if not self.parameters.given('build') and self.parameters.given('dest'): download_destination=self.parameters.dest

        contents = os.path.join(download_destination, 'CONTENTS.txt')
        contents = open(contents, "w")
        contents.write("The following packages were downloaded at %s.\n" % time.asctime())

        data = []
        def dl_callback(ob):
            print "Retrieving %s.\n" % ob.name,
            print "--> %s" % ob.download_url
            filename = os.path.split(ob.download_url)[1]
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
        if not self.parameters.given('core'): walk=walk+('addons', )

        for w in walk:
            cur = getattr(dist, w, []) 
            for c in cur:
                callback(c)


    def build(self):

        if not self.parameters.given('build'): return

        # check if we have products only
        got = map(lambda x: (x.type, x), self.data)

        # check if we only got products
        products = filter(lambda x: x[0] == 'ZProduct', got)
        products = len(products) == len(got)

        if products:
            # if we only have products reset their destination
            for ob in got:
                ob[1].destination=''
        else: pass
        got = map(lambda x: x[1], got)

        items = []
        def expand(ob):
            if hasattr(ob,  'items'):
                for item in ob.items:
                    expand(item)
            else:
                items.append(ob)
                                                             
        # expand bundles
        map(lambda x: expand(x), got)

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
            print "Processing %s %s." % (ob.type, visible_name)
            tar=tarfile.open(filename)
            base=''
            for f in tar.getmembers():
                need=1
                if search:
                    need=0
                    name = f.name
                    name = name.split('/')
                    if len(name): 
                        if name[0] == search:
                            need=1
                        elif len(name)>1 and name[1] == search:
                            need=1
                if need:
                    try: base=name[0]
                    except: pass
                    tar.extract(f, destination)
                else: continue

            # close tar
            tar.close()

            # move directory if needed
            if move:
                source = os.path.join(destination,base,search)
                destination = move
                copy_tree(source, destination) 
                remove_tree(os.path.split(source)[0])
            else:
                destination = os.path.join(destination, ob.name)

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
                print "--> NO VERSION."

        # cleanup for packaging
        for ob in self.data:
            filename = ob.filename
            os.unlink(filename)


    def cleanup(self):
        print "Cleaning up %s." % self.basefolder
        #remove_tree(self.basefolder)
        pass

# main class
if __name__ == '__main__':
    plone=Plone()
    plone.main()


