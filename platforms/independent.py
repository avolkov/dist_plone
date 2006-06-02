from dist_plone import Software, PyModule, ZProduct, Bundle

BASE = 'http://switch.dl.sourceforge.net/sourceforge/'

PLONE_BASE = BASE + 'plone/'
#PLONE_BASE = 'http://localhost/plone25/'

PLONE_ORG = 'http://plone.org/products/'
OSCOM_ORG = 'http://kupu.oscom.org/'
ZOPE_ORG = 'http://www.zope.org/Products/'

PLONE_CORE = [
    Bundle('CMF',
           'http://www.zope.org/Products/CMF/CMF-1.6.0/CMF-1.6.0.tar.gz',
           { 'CMFActionIcons': ZProduct,
             'CMFCalendar': ZProduct,
             'CMFCore'    : ZProduct,
             'CMFDefault' : ZProduct,
             'CMFSetup'   : ZProduct,
             'CMFTopic'   : ZProduct,
             'CMFUid'     : ZProduct,
             'DCWorkflow' : ZProduct,
             'GenericSetup' : ZProduct,
           }
    ),
    ZProduct('ATContentTypes', PLONE_ORG + 'atcontenttypes/releases/1.1/ATContentTypes-1.1-beta2.tar.gz'),
    ZProduct('ATReferenceBrowserWidget', PLONE_ORG + 'atreferencebrowserwidget/releases/1.4/ATReferenceBrowserWidget-1.4.tar.gz'),
    ZProduct('CacheFu', PLONE_ORG + 'cachefu/releases/1.0-beta-2/cachefu-1-0-beta-2.tgz', 'CacheFu-1.0-beta2'),
    ZProduct('CMFDynamicViewFTI', PLONE_ORG + 'cmfdynamicviewfti/releases/2.0.0/CMFDynamicViewFTI-2.0.0.tar.gz'),
    ZProduct('CMFFormController', PLONE_ORG + 'cmfformcontroller/releases/2.0.2/CMFFormController-2.0.2.tar.gz'),
    # Poor release name
    ZProduct('CMFPlacefulWorkflow', PLONE_ORG + 'cmfplacefulworkflow/releases/1.0beta3/cmfplacefulworkflow-1-0beta3.tgz'),
    ZProduct('CMFPlone', PLONE_ORG + 'plone/releases/2.5/PloneBase-2.5-beta2.tar.gz'),
    ZProduct('CMFQuickInstallerTool', PLONE_ORG + 'cmfquickinstallertool/releases/1.5.9/CMFQuickInstallerTool-1.5.9.tar.gz'),
    ZProduct('GroupUserFolder', PLONE_ORG + 'groupuserfolder/releases/3.52/groupuserfolder-3-52.tgz'),
    ZProduct('PlacelessTranslationService',  PLONE_ORG + 'pts/releases/1.3.1/PlacelessTranslationService-1.3.1.tar.gz'),
    ZProduct('PloneErrorReporting',PLONE_ORG + 'ploneerrorreporting/releases/0.11/PloneErrorReporting-0.11.tar.gz'),
    ZProduct('PloneTestCase',PLONE_ORG + 'plonetestcase/releases/0.8.2/PloneTestCase-0.8.2.tar.gz'),
    ZProduct('PloneTranslations',PLONE_ORG + 'plonetranslations/releases/2.5-beta2/PloneTranslations-2.5-beta2.tar.gz'),
    ZProduct('PloneLanguageTool', PLONE_ORG + 'plonelanguagetool/releases/1.2/PloneLanguageTool-1.2.tar.gz'),
    ZProduct('SecureMailHost', PLONE_ORG + 'securemailhost/releases/1.0.4/SecureMailHost-1.0.4.tar.gz'),
    ZProduct('ExtendedPathIndex', PLONE_ORG + 'extendedpathindex/releases/2.3/ExtendedPathIndex-2.3.tar.gz'),
    ZProduct('ResourceRegistries', PLONE_ORG + 'resourceregistries/releases/1.3/resourceregistries-1-3-rc1-tar.gz'),
    ZProduct('statusmessages', PLONE_ORG + 'statusmessages/releases/2.0/statusmessages-2.0.tar.gz'),
    ZProduct('PlonePAS', PLONE_ORG + 'plonepas/releases/2.0/plonepas-2-0-beta2-tar.gz'),
    ZProduct('PluggableAuthService', ZOPE_ORG + 'PluggableAuthService/PluggableAuthService-1.2/PluggableAuthService-1.2.tar.gz'),
    ZProduct('PasswordResetTool', PLONE_ORG + 'passwordresettool/releases/0.4.0/passwordresettool-0-4-tar.gz'),
    ZProduct('PluginRegistry', ZOPE_ORG + 'PluginRegistry/PluginRegistry-1.1/PluginRegistry-1.1.tar.gz'),
]

ADDONS = [
    ZProduct('ExternalEditor', 'http://plope.com/software/ExternalEditor/ExternalEditor-0.9.1-src.tgz'),
    ZProduct('kupu', PLONE_ORG + 'kupu/releases/1.3.6-plone/kupu-1-3-6-plone-tar.gz')
]

AT1_4 = [
    ZProduct('Archetypes', PLONE_ORG + 'archetypes/releases/1.4-beta1/archetypes-1.4.0-beta1-bundle.tar.gz'),
]

README_TXT = """Plone's README is in CMFPlone/README.txt
"""

class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.4.3/Python-2.4.3.tgz')
    zope   =  Software('zope'  , ZOPE_ORG + 'Zope/2.9.3/Zope-2.9.3-final.tgz')

    # plone core
    core   = PLONE_CORE

    # plone addons
    addons = ADDONS + AT1_4

    # the readme.txt
    readme = README_TXT

