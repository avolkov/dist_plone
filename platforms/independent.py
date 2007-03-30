from dist_plone import Software, PyModule, ZProduct, Bundle

BASE = 'http://plone.googlecode.com/files/'

PLONE_BASE = BASE
#PLONE_BASE = 'http://localhost/plone25/'

PLONE_ORG = 'http://plone.org/products/'
OSCOM_ORG = 'http://kupu.oscom.org/'
ZOPE_ORG = 'http://www.zope.org/Products/'

PLONE_CORE = [
    Bundle('CMF',
           'http://www.zope.org/Products/CMF/CMF-1.6.2/CMF-1.6.2.tar.gz',
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
    ZProduct('ATContentTypes', PLONE_ORG + 'atcontenttypes/releases/1.1.4/ATContentTypes-1.1.4.tgz'),
    ZProduct('ATReferenceBrowserWidget', PLONE_ORG + 'atreferencebrowserwidget/releases/1.7/ATReferenceBrowserWidget-1.7.1.tgz'),
    ZProduct('CacheFu', PLONE_ORG + 'cachefu/releases/1.0.2/CacheFu-1.0.2.tgz', 'CacheFu-1.0.2'),
    ZProduct('CMFDynamicViewFTI', PLONE_ORG + 'cmfdynamicviewfti/releases/2.1/CMFDynamicViewFTI-2.1.tar.gz'),
    ZProduct('CMFFormController', PLONE_ORG + 'cmfformcontroller/releases/2.0.7/CMFFormController-2.0.7.tar.gz'),
    ZProduct('CMFPlacefulWorkflow', PLONE_ORG + 'cmfplacefulworkflow/releases/1.0.2/CMFPlacefulWorkflow-1.0.2.tgz'),
    ZProduct('CMFPlone', PLONE_BASE + 'PloneBase-2.5.2.tar.gz'),
    ZProduct('CMFQuickInstallerTool', PLONE_ORG + 'cmfquickinstallertool/releases/1.5.9/CMFQuickInstallerTool-1.5.9.tar.gz'),
    ZProduct('ExtendedPathIndex', PLONE_ORG + 'extendedpathindex/releases/2.4/ExtendedPathIndex-2.4.tgz'),
    ZProduct('GroupUserFolder', PLONE_ORG + 'groupuserfolder/releases/3.54.1/GroupUserFolder-3.54.1.tgz'),
    ZProduct('PlacelessTranslationService',  PLONE_ORG + 'pts/releases/1.3.5/PlacelessTranslationService-1.3.5.tar.gz'),
    ZProduct('PloneErrorReporting',PLONE_ORG + 'ploneerrorreporting/releases/1.0/PloneErrorReporting-1.0.tar.gz'),
    ZProduct('PloneTestCase',PLONE_ORG + 'plonetestcase/releases/0.9.0/PloneTestCase-0.9.0.tar.gz'),
    ZProduct('PloneTranslations',PLONE_ORG + 'plonetranslations/releases/2.6.1/PloneTranslations-2.6.1.tar.gz'),
    ZProduct('PloneLanguageTool', PLONE_ORG + 'plonelanguagetool/releases/1.5/PloneLanguageTool-1.5.tar.gz'),
    ZProduct('SecureMailHost', PLONE_ORG + 'securemailhost/releases/1.0.4/SecureMailHost-1.0.4.tar.gz'),
    ZProduct('ResourceRegistries', PLONE_ORG + 'resourceregistries/releases/1.3.4/ResourceRegistries-1.3.4.tar.gz'),
    ZProduct('statusmessages', PLONE_ORG + 'statusmessages/releases/2.0.1/statusmessages-2.0.1.tar.gz'),
    ZProduct('PlonePAS', PLONE_ORG + 'plonepas/releases/2.3/PlonePAS-2.3.tar.gz'),
    ZProduct('PluggableAuthService', ZOPE_ORG + 'PluggableAuthService/PluggableAuthService-1.4.1/PluggableAuthService-1.4.1.tar.gz', 'PluggableAuthService-1.4.1'),
    ZProduct('PasswordResetTool', PLONE_ORG + 'passwordresettool/releases/0.4.2/PasswordResetTool-0.4.2.tar.gz'),
    ZProduct('PluginRegistry', ZOPE_ORG + 'PluginRegistry/PluginRegistry-1.1.1/PluginRegistry-1.1.1.tar.gz', 'PluginRegistry-1.1.1'),
]

ADDONS = [
    ZProduct('ExternalEditor', PLONE_ORG + 'external-editor/releases/0.9.3/ExternalEditor-0.9.3-src.tgz'),
    ZProduct('kupu', PLONE_ORG + 'kupu/releases/1.3.9/kupu.tgz')
]

AT1_4 = [
    ZProduct('Archetypes', PLONE_ORG + 'archetypes/releases/1.4.2/Archetypes-1.4.2-final-Bundle.tar.gz'),
]

README_TXT = """Plone's README is in CMFPlone/README.txt
"""

class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.4.4/Python-2.4.4.tgz')
    zope   =  Software('zope'  , ZOPE_ORG + 'Zope/2.9.7/Zope-2.9.7-final.tgz')

    # plone core
    core   = PLONE_CORE

    # plone addons
    addons = ADDONS + AT1_4

    # the readme.txt
    readme = README_TXT
