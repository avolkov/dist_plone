from dist_plone import Software, PyModule, ZProduct, Bundle

BASE = 'http://osdn.dl.sourceforge.net/sourceforge/'
#BASE = 'http://voxel.dl.sourceforge.net/sourceforge/'
#BASE = 'http://switch.dl.sourceforge.net/sourceforge/'

PLONE_BASE = BASE + 'plone/'

PLONE_ORG = 'http://plone.org/products/'
OSCOM_ORG = 'http://kupu.oscom.org/'

PLONE_CORE = [
    Bundle('CMF',
           'http://www.zope.org/Products/CMF/CMF-1.5.5/CMF-1.5.5.tar.gz',
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
    ZProduct('CMFPlone', PLONE_BASE + 'PloneBase-2.1.1.tar.gz'),
    ZProduct('CMFFormController', PLONE_ORG + 'cmfformcontroller/releases/1.0.6/CMFFormController-1.0.6.tar.gz'),
    ZProduct('CMFQuickInstallerTool', PLONE_ORG + 'cmfquickinstallertool/releases/1.5.5/CMFQuickInstallerTool-1.5.5.tgz'),
    #XXX ZProduct('BTreeFolder2', 'http://hathawaymix.org/Software/BTreeFolder2/BTreeFolder2-1.0.1.tar.gz'),
    ZProduct('BTreeFolder2', 'http://plone.org/Members/tiran/BTreeFolder2-1.0.2.tar.gz'),
    ZProduct('GroupUserFolder', PLONE_ORG + 'groupuserfolder/releases/3.4/GroupUserFolder-3.4.tar.gz'),
    ZProduct('PlacelessTranslationService', PLONE_ORG + 'pts/releases/1.2.5/PlacelessTranslationService-1.2.5.tar.gz'),
    ZProduct('PloneErrorReporting', PLONE_ORG + 'ploneerrorreporting/releases/0.11/PloneErrorReporting-0.11.tar.gz'),
    ZProduct('PloneTranslations', PLONE_ORG + 'plonetranslations/releases/2.1.1/PloneTranslations-2.1.1.tar.gz'),
    ZProduct('PloneLanguageTool', PLONE_ORG + 'plonelanguagetool/releases/0.9/PloneLanguageTool-0.9.tar.gz'),
    ZProduct('SecureMailHost', PLONE_ORG + 'smh/releases/1.0.1/SecureMailHost-1.0.1.tar.gz'),
    ZProduct('ExtendedPathIndex', PLONE_ORG + 'extendedpathindex/releases/2.2/ExtendedPathIndex-2.2.tar.gz'),
    ZProduct('ResourceRegistries', PLONE_ORG + 'resourceregistries/releases/1.0.5/ResourceRegistries-1.0.5.tar.gz'),
    ZProduct('ATReferenceBrowserWidget', PLONE_ORG + 'atreferencebrowserwidget/releases/1.1/ATReferenceBrowserWidget.tar.gz'),
    ZProduct('ATContentTypes', PLONE_ORG + 'atcontenttypes/releases/1.0.1/ATContentTypes-1.0.1-final.tar.gz'),
    ZProduct('CMFDynamicViewFTI', PLONE_ORG + 'cmfdynamicviewfti/releases/1.0.1/CMFDynamicViewFTI-1.0.1.tar.gz'),
]

ADDONS = [
    ZProduct('ExternalEditor', 'http://plope.com/software/ExternalEditor/ExternalEditor-0.9.1-src.tgz'),
    ZProduct('kupu', PLONE_ORG + 'kupu/releases/1.3.3/kupu-1-3-3.tgz'),
    #ZProduct('kupu', OSCOM_ORG + 'midcom-serveattachmentguid-f40122579e491f7a7417987bef0c49ee/kupu-1.3.1.tar.gz')
]

AT1_3 = [
    ZProduct('Archetypes', PLONE_ORG + 'archetypes/releases/1.3.5/Archetypes-1.3.5-final-Bundle.tar.gz'),
]

README_TXT = """Plone's README is in CMFPlone/README.txt
"""

class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.3.5/Python-2.3.5.tgz')
    zope   =  Software('zope'  , 'http://www.zope.org/Products/Zope/2.8.4/Zope-2.8.4-final.tgz')

    # plone core
    core   = PLONE_CORE

    # plone addons
    addons = ADDONS + AT1_3

    # the readme.txt
    readme = README_TXT

