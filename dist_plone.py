
import time
import os, getopt, sys
import tempfile, urllib


class Software:
    """ general software """
                                                                                                                             
    name = None
    download_url = None
    filename = None
    parent = None
                                                                                                                             
    def __init__(self, name, download_url):
        self.name = name
        self.download_url = download_url



class Bundle(Software):
    """ a archive which contains multiple other parts """

    items = []

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
    pass


class ZProduct(Software):
    """ zope product """
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
        def dl_callback(ob):
            print "Retrieving %s.\n" % ob.name,
            print "%s" % ob.download_url
            filename = os.path.split(ob.download_url)[1]
            filename = os.path.join(download_destination, filename)
            urllib.urlretrieve(ob.download_url, filename)
            ob.filename=filename
            contents.write("%s - %s\n" % (ob.name, ob.download_url))
            print "-"*78
            
        # walk with our callback
        self.walk(dl_callback)
 
        # close log file
        contents.close()


    def walk(self, callback):

        dist = self.parameters.dist
        walk = ('core',)
        if not self.parameters.given('core'): walk=walk+('addons', )

        for w in walk:
            cur = getattr(dist, w, []) 
            for c in cur:
                callback(c)


    def build(self):
        pass


    def cleanup(self):
        pass

# main class
if __name__ == '__main__':
    plone=Plone()
    plone.main()


