from dist_plone import Software, PyModule, ZProduct, Bundle

BASE = 'http://osdn.dl.sourceforge.net/sourceforge/'
#BASE = 'http://voxel.dl.sourceforge.net/sourceforge/'
#BASE = 'http://switch.dl.sourceforge.net/sourceforge/'

PLONE_BASE = BASE + 'plone/'
#PLONE_BASE = 'http://dev.clearwind.ca/Files/Plone/Nightly/'
#PLONE_BASE = 'http://localhost/plone21/'

PLONE_I18N_BASE = BASE + 'plone-i18n/'
COLLECTIVE_BASE = BASE + 'collective/'
ARCHETYPES_BASE = BASE + 'archetypes/'

PLONE_CORE = [
    Bundle('CMF',
           'http://zope.org/Products/CMF/CMF-1.4.8/CMF-1.4.8.tar.gz',
           { 'CMFCalendar': ZProduct,
             'CMFCore'    : ZProduct,
             'CMFDefault' : ZProduct,
             'CMFTopic'   : ZProduct,
             'DCWorkflow' : ZProduct,
           }
    ),
    Bundle('CMFActionIcons',
           'http://zope.org/Members/tseaver/CMFActionIcons/CMFActionIcons-0.9/CMFActionIcons-0.9.tar.gz',
           {'CMFActionIcons': ZProduct,}
    ),
    ZProduct('CMFPlone', PLONE_BASE + 'PloneBase-2.1-alpha2.tar.gz'),
    ZProduct('CMFFormController', COLLECTIVE_BASE + 'CMFFormController-1.0.4.tar.gz'),
    ZProduct('CMFQuickInstallerTool', COLLECTIVE_BASE + 'CMFQuickInstallerTool-1.5.3.tgz'),
    ZProduct('BTreeFolder2', 'http://hathawaymix.org/Software/BTreeFolder2/BTreeFolder2-1.0.1.tar.gz'),
    ZProduct('GroupUserFolder', COLLECTIVE_BASE + 'GroupUserFolder-3.2.tar.gz'),
    ZProduct('PlacelessTranslationService', COLLECTIVE_BASE + 'PlacelessTranslationService-1.2-rc2.tar.gz'),
    ZProduct('PloneErrorReporting', COLLECTIVE_BASE + 'PloneErrorReporting-0.11.tar.gz'),
    ZProduct('PloneTranslations', PLONE_I18N_BASE + 'PloneTranslations-2.1beta2.tar.gz'),
    ZProduct('SecureMailHost', COLLECTIVE_BASE + 'SecureMailHost-1.0-rc1.tar.gz'),
    ZProduct('ExtendedPathIndex', 'http://plone.org/products/extendedpathindex/releases/2.1/ExtendedPathIndex-2.1.tar.gz'),
    ZProduct('ResourceRegistries', 'http://plone.org/products/resourceregistries/releases/0.8.1/ResourceRegistries-0.8.1.tar.gz'),
    ZProduct('ATReferenceBrowserWidget', 'http://plone.org/products/atreferencebrowserwidget/releases/1.0/ATReferenceBrowserWidget1.0.tar.gz')
]

ADDONS = [
    ZProduct('ExternalEditor', 'http://zope.org/Members/Caseman/ExternalEditor/0.8/ExternalEditor-0.8-src.tgz'),
    ZProduct('Epoz', 'http://mjablonski.zope.de/Epoz/releases/Epoz-0.9.0.tar.gz'),
#    ZProduct('kupu', 'http://kupu.oscom.org/midcom-serveattachmentguid-6799a2e8aec0edc19a6a1f2682ac8a4a/kupu-1.1.tgz')
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

#AT1_3 = [
#    Bundle('Archetypes', ARCHETYPES_BASE + 'Archetypes-1.3.2-final-Bundle.tar.gz',
#           { 'Archetypes': ZProduct,
#             'generator' : ZProduct,
#             'validation': ZProduct,
#             'PortalTransforms': ZProduct,
#             'MimetypesRegistry': ZProduct,
#           }
#    ),
#]

AT1_3 = [
    ZProduct('Archetypes', ARCHETYPES_BASE + 'Archetypes-1.3.4-beta1-Bundle.tar.gz'),
]

ATCT = [
    ZProduct('ATContentTypes', 'http://plone.org/products/atcontenttypes/releases/1.0/ATContentTypes-snapshot-20050524.tar.gz'),
]


README_TXT = """Plone's README is in CMFPlone/README.txt
"""


class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.3.5/Python-2.3.5.tgz')
    zope   =  Software('zope'  , 'http://zope.org/Products/Zope/2.7.6/Zope-2.7.6-final.tgz')

    # plone core
    core   = PLONE_CORE

    # plone addons
    addons = ADDONS + AT1_3 + ATCT

    # the readme.txt
    readme = README_TXT


