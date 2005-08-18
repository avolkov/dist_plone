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

PLONE_ORG = 'http://plone.org/products/'

PLONE_CORE = [
    Bundle('CMF',
           'http://www.zope.org/Products/CMF/CMF-1.5.3/CMF-1.5.3.tar.gz',
           { 'CMFActionIcons': ZProduct,
             'CMFCalendar': ZProduct,
             'CMFCore'    : ZProduct,
             'CMFDefault' : ZProduct,
             'CMFSetup'   : ZProduct,
             'CMFTopic'   : ZProduct,
             'CMFUid'     : ZProduct,
             'DCWorkflow' : ZProduct,
           }
    ),
    ZProduct('CMFPlone', PLONE_BASE + 'PloneBase-2.1-rc3.tar.gz'),
    ZProduct('CMFFormController', COLLECTIVE_BASE + 'CMFFormController-1.0.5-beta.tar.gz'),
    ZProduct('CMFQuickInstallerTool', COLLECTIVE_BASE + 'CMFQuickInstallerTool-1.5.5.tgz'),
    #XXX ZProduct('BTreeFolder2', 'http://hathawaymix.org/Software/BTreeFolder2/BTreeFolder2-1.0.1.tar.gz'),
    ZProduct('BTreeFolder2', 'http://plone.org/Members/tiran/BTreeFolder2-1.0.2.tar.gz'),
    ZProduct('GroupUserFolder', PLONE_ORG + 'GroupUserFolder/releases/3.4RC/GroupUserFolder-3.4RC.tar.gz'),
    ZProduct('PlacelessTranslationService', COLLECTIVE_BASE + 'PlacelessTranslationService-1.2.1.tar.gz'),
    ZProduct('PloneErrorReporting', COLLECTIVE_BASE + 'PloneErrorReporting-0.11.tar.gz'),
    ZProduct('PloneTranslations', PLONE_I18N_BASE + 'PloneTranslations-2.1-rc3.tar.gz'),
    ZProduct('PloneLanguageTool', PLONE_ORG + 'plonelanguagetool/releases/0.6/PloneLanguageTool-0.6.tar.gz'),
    ZProduct('SecureMailHost', PLONE_ORG + 'smh/releases/1.0.1/SecureMailHost-1.0.1.tar.gz'),
    ZProduct('ExtendedPathIndex', PLONE_ORG + 'extendedpathindex/releases/2.1/ExtendedPathIndex-2.1.tar.gz'),
    ZProduct('ResourceRegistries', PLONE_ORG + 'resourceregistries/releases/1.0.3/ResourceRegistries-1.0.3.tgz'),
    ZProduct('ATReferenceBrowserWidget', PLONE_ORG + 'atreferencebrowserwidget/releases/1.1/ATReferenceBrowserWidget.tar.gz'),
    ZProduct('ATContentTypes', PLONE_ORG + 'atcontenttypes/releases/1.0/ATContentTypes-1.0.0-rc5.tar.gz'),
    ZProduct('CMFDynamicViewFTI', PLONE_ORG + 'cmfdynamicviewfti/releases/1.0.1/CMFDynamicViewFTI-1.0.1.tar.gz'),
]

ADDONS = [
    ZProduct('ExternalEditor', 'http://plope.com/software/ExternalEditor/ExternalEditor-0.9.1-src.tgz'),
    #ZProduct('Epoz', 'http://mjablonski.zope.de/Epoz/releases/Epoz-2.0.0.tar.gz'),
    #XXX ZProduct('kupu', 'http://kupu.oscom.org/midcom-serveattachmentguid-6b4584286e6cd5bbf2f82f0a83ead0e2/kupu-1.2.1.tar.gz')
    ZProduct('kupu', PLONE_ORG + 'kupu/releases/1.3rc3/kupu-1.3-rc3.tgz')
]

#AT1_3 = [
#    Bundle('Archetypes', ARCHETYPES_BASE + 'Archetypes-1.3.4-rc3-Bundle.tar.gz',
#           { 'Archetypes': ZProduct,
#             'generator' : ZProduct,
#             'validation': ZProduct,
#             'PortalTransforms': ZProduct,
#             'MimetypesRegistry': ZProduct,
#           }
#    ),
#] 

AT1_3 = [
    ZProduct('Archetypes', ARCHETYPES_BASE + 'Archetypes-1.3.4-rc3-Bundle.tar.gz'),
]


README_TXT = """Plone's README is in CMFPlone/README.txt
"""


class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.3.5/Python-2.3.5.tgz')
    zope   =  Software('zope'  , 'http://www.zope.org/Products/Zope/2.8.1/Zope-2.8.1-final.tar.gz')

    # plone core
    core   = PLONE_CORE

    # plone addons
    addons = ADDONS + AT1_3

    # the readme.txt
    readme = README_TXT


