from dist_plone import Software, PyModule, ZProduct, Bundle

#BASE = 'http://osdn.dl.sourceforge.net/sourceforge/'
#BASE = 'http://voxel.dl.sourceforge.net/sourceforge/'
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
    ZProduct('ATContentTypes', PLONE_ORG + 'atcontenttypes/releases/1.1/ATContentTypes-1.1-beta1.tar.gz'),
    ZProduct('ATReferenceBrowserWidget', PLONE_ORG + 'atreferencebrowserwidget/releases/1.3/ATReferenceBrowserWidget-1.3.tar.gz'),
    ZProduct('CacheFu', PLONE_ORG + 'cachefu/releases/1.0-beta/cachefu-1-0beta-tar.gz', 'CacheFu-1.0beta'),
    ZProduct('CMFDynamicViewFTI', PLONE_ORG + 'cmfdynamicviewfti/releases/2.0.0/CMFDynamicViewFTI-2.0.0.tar.gz'),
    ZProduct('CMFFormController', PLONE_ORG + 'cmfformcontroller/releases/2.0.2/CMFFormController-2.0.2.tar.gz'),
    # Poor release name
    ZProduct('CMFPlacefulWorkflow', PLONE_ORG + 'cmfplacefulworkflow/releases/0.5alpha2/cmfplacefulworkflow-0-5alpha2.tgz'),
    ZProduct('CMFPlone', PLONE_BASE + 'PloneBase-2.5-beta1.tar.gz'),
    ZProduct('CMFQuickInstallerTool', PLONE_ORG + 'cmfquickinstallertool/releases/1.5.8/CMFQuickInstallerTool-1.5.8.tar.gz'),
    ZProduct('Five', 'http://codespeak.net/z3/five/release/Five-1.2.4.tgz'),
    ZProduct('GroupUserFolder', PLONE_ORG + 'groupuserfolder/releases/3.51/groupuserfolder-3-51.tgz'),
    ZProduct('PlacelessTranslationService',  PLONE_ORG + 'pts/releases/1.3.0/PlacelessTranslationService-1.3.0.tar.gz'),
    ZProduct('PloneErrorReporting',PLONE_ORG + 'ploneerrorreporting/releases/0.11/PloneErrorReporting-0.11.tar.gz'),
    ZProduct('PloneTestCase',PLONE_ORG + 'plonetestcase/releases/0.8.0/PloneTestCase-0.8.0.tar.gz'),
    ZProduct('PloneTranslations',PLONE_ORG + 'plonetranslations/releases/2.5-beta1/PloneTranslations-2.5-beta1.tar.gz'),
    ZProduct('PloneLanguageTool', PLONE_ORG + 'plonelanguagetool/releases/1.1/PloneLanguageTool-1.1.tar.gz'),
    ZProduct('SecureMailHost', PLONE_ORG + 'securemailhost/releases/1.0.4/SecureMailHost-1.0.4.tar.gz'),
    ZProduct('ExtendedPathIndex', PLONE_ORG + 'extendedpathindex/releases/2.3/ExtendedPathIndex-2.3.tar.gz'),
    ZProduct('ResourceRegistries', PLONE_ORG + 'resourceregistries/releases/1.3/resourceregistries-1-3-beta1-tar.gz'),
    ZProduct('statusmessages', PLONE_ORG + 'statusmessages/releases/2.0/statusmessages-2.0.tar.gz'),
    ZProduct('PlonePAS', PLONE_ORG + 'plonepas/releases/1.2/plonepas-1-2-tar.gz'),
    ZProduct('PluggableAuthService', ZOPE_ORG + 'PluggableAuthService/PluggableAuthService-1.2-beta/PluggableAuthService-1.2-beta.tar.gz'),
    ZProduct('PasswordResetTool', PLONE_ORG + 'passwordresettool/releases/0.4.0/passwordresettool-0-4-tar.gz'),
    ZProduct('PluginRegistry', ZOPE_ORG + 'PluginRegistry/PluginRegistry-1.1/PluginRegistry-1.1.tar.gz'),
]

ADDONS = [
    ZProduct('ExternalEditor', 'http://plope.com/software/ExternalEditor/ExternalEditor-0.9.1-src.tgz'),
    ZProduct('kupu', PLONE_ORG + 'kupu/releases/1.3.5-plone25beta/kupu-1.3.5-plone25beta-tar.gz')
]

AT1_4 = [
    ZProduct('Archetypes', PLONE_ORG + 'archetypes/releases/1.4-alpha3/archetypes-1.4.0-alpha03-bundle.tar.gz'),
]

README_TXT = """Plone's README is in CMFPlone/README.txt
"""

class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.3.5/Python-2.3.5.tgz')
    zope   =  Software('zope'  , ZOPE_ORG + 'Zope/2.8.6/Zope-2.8.6-final.tgz')

    # plone core
    core   = PLONE_CORE

    # plone addons
    addons = ADDONS + AT1_4

    # the readme.txt
    readme = README_TXT

