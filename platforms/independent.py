from dist_plone import Software, PyModule, ZProduct, Bundle

BASE = 'http://voxel.dl.sourceforge.net/sourceforge/'
PLONE_BASE = BASE + 'plone/'
PLONE_I18N_BASE = BASE + 'plone-i18n/'
COLLECTIVE_BASE = BASE + 'collective/'
ARCHETYPES_BASE = BASE + 'archetypes/'

PLONE_CORE = [
    Bundle('CMF',
           'http://zope.org/Products/CMF/CMF-1.4.6/CMF-1.4.6.tar.gz',
           { 'CMFCalendar': ZProduct,
             'CMFCore'    : ZProduct,
             'CMFDefault' : ZProduct,
             'CMFTopic'   : ZProduct,
             'DCWorkflow' : ZProduct,
           }
    ),
    ZProduct('BTreeFolder2', 'http://hathawaymix.org/Software/BTreeFolder2/BTreeFolder2-1.0.1.tar.gz'),
    Bundle('CMFActionIcons',
           'http://zope.org/Members/tseaver/CMFActionIcons/CMFActionIcons-0.9/CMFActionIcons-0.9.tar.gz',
           {'CMFActionIcons': ZProduct,}
    ),
    ZProduct('CMFFormController', COLLECTIVE_BASE + 'CMFFormController-1.0.3-beta.tar.gz'),
    ZProduct('CMFPlone', PLONE_BASE + 'PloneBase-2.0.4.tar.gz'),
    ZProduct('CMFQuickInstallerTool', COLLECTIVE_BASE + 'CMFQuickInstallerTool-1.5.0.tgz'),
    ZProduct('Formulator', 'http://zope.org/Members/infrae/Formulator/Formulator-1.6.2/Formulator-1.6.2.tgz'),
    ZProduct('GroupUserFolder', COLLECTIVE_BASE + 'GroupUserFolder-2.0.1.tgz'),
    ZProduct('PlacelessTranslationService', COLLECTIVE_BASE + 'PlacelessTranslationService-1.0-rc8.tar.gz'),
    ZProduct('PloneErrorReporting', COLLECTIVE_BASE + 'PloneErrorReporting-0.11.tar.gz'),
    ZProduct('PloneTranslations', PLONE_I18N_BASE + 'PloneTranslations-0.4.tar.gz'),
    ZProduct('SecureMailHost', COLLECTIVE_BASE + 'SecureMailHost-0.2rc3.tar.gz'),
    ]

ADDONS = [
    ZProduct('ExternalEditor', 'http://zope.org/Members/Caseman/ExternalEditor/0.8/ExternalEditor-0.8-src.tgz'),
    ZProduct('Epoz', 'http://mjablonski.zope.de/Epoz/releases/Epoz-0.8.2.tar.gz'),
##    ZProduct('kupu', 'http://kupu.oscom.org/midcom-serveattachmentguid-6799a2e8aec0edc19a6a1f2682ac8a4a/kupu-1.1.tgz')
    ]

AT1_2 = [
    Bundle('Archetypes',  ARCHETYPES_BASE + 'Archetypes-1.2.5-rc5.tar.gz',
           { 'Archetypes': ZProduct,
             'generator' : ZProduct,
             'validation': ZProduct,
             'PortalTransforms': ZProduct,
           }
        ),
    #Bundle('PortalTransforms',
    #       ARCHETYPES_BASE + 'PortalTransforms-1.0.4.tgz',
    #       {'PortalTransforms': ZProduct,}
    #    ),
    ]

AT1_3 = [
    Bundle('Archetypes',  ARCHETYPES_BASE + 'Archetypes-1.3.0-beta5.tar.gz',
           { 'Archetypes': ZProduct,
             'generator' : ZProduct,
             'validation': ZProduct,
             'PortalTransforms': ZProduct,
             'MimetypesRegistry': ZProduct,
           }
    ),
    ZProduct('ATContentTypes', COLLECTIVE_BASE + 'ATCT-0.2beta8.tar.gz'),
]


README_TXT = """Plone's README is in CMFPlone/README.txt
"""


class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.3.4/Python-2.3.4.tgz')
    zope   =  Software('zope'  , 'http://zope.org/Products/Zope/2.7.2/Zope-2.7.2.tgz')

    # plone core
    core   = PLONE_CORE

    # plone addons
    addons = ADDONS + AT1_2

    # the readme.txt
    readme = README_TXT


