from dist_plone import Software, PyModule, ZProduct, Bundle


PLONE_CORE = [
    Bundle('CMF',
           'http://cmf.zope.org/download/CMF-1.4.3/CMF-1.4.3.tar.gz',
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
    ZProduct('CMFFormController', 'http://heanet.dl.sourceforge.net/sourceforge/collective/CMFFormController-1.0.2.tgz'),
    ZProduct('CMFPlone', 'http://osdn.dl.sourceforge.net/sourceforge/plone/PloneBase-2.0.1.tgz'),
    ZProduct('CMFQuickInstallerTool', 'http://heanet.dl.sourceforge.net/sourceforge/collective/CMFQuickInstallerTool-1.5.0.tgz'),
    ZProduct('Formulator', 'http://zope.org/Members/infrae/Formulator/Formulator-1.6.2/Formulator-1.6.2.tgz'),
    ZProduct('GroupUserFolder', 'http://heanet.dl.sourceforge.net/sourceforge/collective/GroupUserFolder-2.0.1.tgz'),
    ZProduct('PlacelessTranslationService', 'http://osdn.dl.sourceforge.net/sourceforge/collective/PlacelessTranslationService-1.0fork-rc7.tar.gz'),
    ZProduct('PloneErrorReporting', 'http://heanet.dl.sourceforge.net/sourceforge/collective/PloneErrorReporting-0.1.tar.gz'),
    ZProduct('PloneTranslations', 'http://osdn.dl.sourceforge.net/sourceforge/plone-i18n/PloneTranslations-0.3.tar.gz'),
    ]

ADDONS = [
    Bundle('Archetypes',  'http://heanet.dl.sourceforge.net/sourceforge/archetypes/archetypes-1.2.5-rc4.tgz',
           { 'Archetypes': ZProduct,
             'generator' : ZProduct,
             'validation': ZProduct,
           }
    ),
    Bundle('PortalTransforms',
           'http://heanet.dl.sourceforge.net/sourceforge/archetypes/PortalTransforms-1.0.4.tgz',
           {'PortalTransforms': ZProduct,}
    ),
    ZProduct('ExternalEditor', 'http://zope.org/Members/Caseman/ExternalEditor/0.7.2/ExternalEditor-0.7.2-src.tgz'),
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


