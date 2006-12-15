from dist_plone import Software, PyModule, ZProduct, Bundle

BASE = 'http://osdn.dl.sourceforge.net/sourceforge/'

PLONE_BASE = BASE + 'plone/'
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
    ZProduct('ATContentTypes', PLONE_ORG + 'atcontenttypes/releases/1.1.3/ATContentTypes-1.1.3.tgz'),
    ZProduct('ATReferenceBrowserWidget', PLONE_ORG + 'atreferencebrowserwidget/releases/1.7/ATReferenceBrowserWidget-1.7.tar.gz'),
    ZProduct('CacheFu', PLONE_ORG + 'cachefu/releases/1.0.1/CacheFu-1.0.1.tgz', 'CacheFu-1.0.1'),
    ZProduct('CMFDynamicViewFTI', PLONE_ORG + 'cmfdynamicviewfti/releases/2.1/CMFDynamicViewFTI-2.1.tar.gz'),
    ZProduct('CMFFormController', PLONE_ORG + 'cmfformcontroller/releases/2.0.6/CMFFormController-2.0.6.tar.gz'),
    ZProduct('CMFPlacefulWorkflow', PLONE_ORG + 'cmfplacefulworkflow/releases/1.0.2/CMFPlacefulWorkflow-1.0.2.tgz'),
    ZProduct('CMFPlone', PLONE_BASE + 'PloneBase-2.5.1-final.tar.gz'),
    ZProduct('CMFQuickInstallerTool', PLONE_ORG + 'cmfquickinstallertool/releases/1.5.9/CMFQuickInstallerTool-1.5.9.tar.gz'),
    ZProduct('ExtendedPathIndex', PLONE_ORG + 'extendedpathindex/releases/2.4/ExtendedPathIndex-2.4.tgz'),
    ZProduct('Five', 'http://codespeak.net/z3/five/release/Five-1.3.8.tgz'),
    ZProduct('GroupUserFolder', PLONE_ORG + 'groupuserfolder/releases/3.54/GroupUserFolder-3.54.tgz'),
    ZProduct('PlacelessTranslationService',  PLONE_ORG + 'pts/releases/1.3.4/PlacelessTranslationService-1.3.4.tar.gz'),
    ZProduct('PloneErrorReporting',PLONE_ORG + 'ploneerrorreporting/releases/1.0/PloneErrorReporting-1.0.tar.gz'),
    ZProduct('PloneTestCase',PLONE_ORG + 'plonetestcase/releases/0.8.4/PloneTestCase-0.8.4.tar.gz'),
    ZProduct('PloneTranslations',PLONE_ORG + 'plonetranslations/releases/2.6.1/PloneTranslations-2.6.1.tar.gz'),
    ZProduct('PloneLanguageTool', PLONE_ORG + 'plonelanguagetool/releases/1.5/PloneLanguageTool-1.5.tar.gz'),
    ZProduct('SecureMailHost', PLONE_ORG + 'securemailhost/releases/1.0.4/SecureMailHost-1.0.4.tar.gz'),
    ZProduct('ResourceRegistries', PLONE_ORG + 'resourceregistries/releases/1.3.3/ResourceRegistries-1.3.3.tar.gz'),
    ZProduct('statusmessages', PLONE_ORG + 'statusmessages/releases/2.0.1/statusmessages-2.0.1.tar.gz'),
    ZProduct('PlonePAS', PLONE_ORG + 'plonepas/releases/2.1/PlonePAS-2.1.tar.gz'),
    ZProduct('PluggableAuthService', ZOPE_ORG + 'PluggableAuthService/PluggableAuthService-1.4/PluggableAuthService-1.4.tar.gz', 'PluggableAuthService-1.4'),
    ZProduct('PasswordResetTool', PLONE_ORG + 'passwordresettool/releases/0.4.1/PasswordResetTool-0.4.1.tar.gz'),
    ZProduct('PluginRegistry', ZOPE_ORG + 'PluginRegistry/PluginRegistry-1.1.1/PluginRegistry-1.1.1.tar.gz', 'PluginRegistry-1.1.1'),
]

ADDONS = [
    ZProduct('ExternalEditor', 'http://plope.com/software/ExternalEditor/ExternalEditor-0.9.2-src.tgz'),
    ZProduct('kupu', PLONE_ORG + 'kupu/releases/1.3.8/kupu-1.3.8.tgz')
]

AT1_4 = [
    ZProduct('Archetypes', PLONE_ORG + 'archetypes/releases/1.4.1/Archetypes-1.4.1-final-Bundle.tar.gz'),
]

README_TXT = """Plone's README is in CMFPlone/README.txt
"""

class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.4.3/Python-2.4.3.tgz')
    zope   =  Software('zope'  , ZOPE_ORG + 'Zope/2.9.4/Zope-2.9.4-final.tgz')

    # plone core
    core   = PLONE_CORE

    # plone addons
    addons = ADDONS + AT1_4

    # the readme.txt
    readme = README_TXT
