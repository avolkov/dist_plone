from dist_plone import Software, PyModule, ZProduct, Bundle


PLONE_CORE = [
    Bundle('CMF',
           'http://cmf.zope.org/download/CMF-1.4.2/CMF-1.4.2.tar.gz',
           { 'CMFCalendar': ZProduct,
             'CMFCore'    : ZProduct,
             'CMFDefault' : ZProduct,
             'CMFTopic'   : ZProduct,
             'DCWorkflow' : ZProduct,
           }
    ),
    ZProduct('BTreeFolder2', 'http://hathaway.freezope.org/Software/BTreeFolder2/BTreeFolder2-1.0.tar.gz'),
    Bundle('CMFActionIcons', 
           'http://zope.org/Members/tseaver/CMFActionIcons/CMFActionIcons-0.9/CMFActionIcons-0.9.tar.gz',
           {'CMFActionIcons': ZProduct,}
    ),
    ZProduct('CMFFormController', 'http://heanet.dl.sourceforge.net/sourceforge/collective/CMFFormController-1.0.1.tar.gz'),
    ZProduct('CMFPlone', 'http://osdn.dl.sourceforge.net/sourceforge/plone/PloneBase-2.0-final.tar.gz'),
    ZProduct('CMFQuickInstallerTool', 'http://heanet.dl.sourceforge.net/sourceforge/collective/CMFQuickInstallerTool_1.4.tgz'),
    ZProduct('Formulator', 'http://zope.org/Members/infrae/Formulator/Formulator-1.6.2/Formulator-1.6.2.tgz'),
    ZProduct('GroupUserFolder', 'http://heanet.dl.sourceforge.net/sourceforge/collective/GroupUserFolder-2.0.tar.gz'),
    ZProduct('PlacelessTranslationService', 'http://heanet.dl.sourceforge.net/sourceforge/collective/PlacelessTranslationService-1.0fork-rc3.tar.gz'),
    ZProduct('PloneErrorReporting', 'http://heanet.dl.sourceforge.net/sourceforge/collective/PloneErrorReporting-0.1.tar.gz'),
    #ZProduct('PloneTranslations', 'http://thisissuppostedtolivesomewhereonsf/PloneTranslations-X.Y.tar.gz'),
    ]

ADDONS = [
    Bundle('Archetypes',
           'http://heanet.dl.sourceforge.net/sourceforge/archetypes/archetypes-1.2.5-rc4.tgz',
           { 'Archetypes': ZProduct,
             'generator' : ZProduct, # omg .. why the hell these go into Products?
             'validation': ZProduct, # omg .. why the hell these go into Products?
           }
    ),
    Bundle('PortalTransforms',
           'http://heanet.dl.sourceforge.net/sourceforge/archetypes/PortalTransforms-1.0.3.tgz',
           {'PortalTransforms': ZProduct,}
    ),
    ZProduct('ExternalEditor', 'http://zope.org/Members/Caseman/ExternalEditor/0.7/ExternalEditor-0.7.tgz'),
    ZProduct('Epoz', 'http://mjablonski.zope.de/Epoz/releases/Epoz-0.8.0.tar.gz'),
    ]

README_TXT = """Plone's README is in CMFPlone/README.txt
"""



class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.3.3/Python-2.3.3.tgz')
    zope   =  Software('zope'  , 'http://zope.org/Products/Zope/2.7.0/Zope-2.7.0.tgz')

    # plone core
    core   = PLONE_CORE

    # plone addons
    addons = ADDONS

    # the readme.txt
    readme = README_TXT


