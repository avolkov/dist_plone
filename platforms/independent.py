from dist_plone import Software, PyModule, ZProduct, Bundle

BASE = 'http://osdn.dl.sourceforge.net/sourceforge/'
#BASE = 'http://voxel.dl.sourceforge.net/sourceforge/'
#BASE = 'http://switch.dl.sourceforge.net/sourceforge/'

PLONE_BASE = BASE + 'plone/'
#PLONE_BASE = 'http://localhost/plone25/'

PLONE_ORG = 'http://plone.org/products/'
OSCOM_ORG = 'http://kupu.oscom.org/'
ZOPE = 'http://www.zope.org/Members/'

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
    ZProduct('ATContentTypes', PLONE_ORG + 'atcontenttypes/releases/1.1/ATContentTypes-1.1-alpha2.tar.gz'),
    ZProduct('ATReferenceBrowserWidget', PLONE_ORG + 'atreferencebrowserwidget/releases/1.2/atreferencebrowserqidget-1_2.tgz'),
    ZProduct('CMFDynamicViewFTI', PLONE_ORG + 'cmfdynamicviewfti/releases/1.0.4/CMFDynamicViewFTI-1.0.4.tar.gz'),
    ZProduct('CMFFormController', PLONE_ORG + 'cmfformcontroller/releases/2.0/CMFFormController-2.0.tar.gz'),
    # Poor release name
    ZProduct('CMFPlacefulWorkflow', PLONE_ORG + 'cmfplacefulworkflow/releases/0.5alpha1/cmfplacefulworkflow-0-5alpha1.tgz'),
    ZProduct('CMFPlone', PLONE_BASE + 'PloneBase-2.5-alpha2.tar.gz'),
    ZProduct('CMFQuickInstallerTool', PLONE_ORG + 'cmfquickinstallertool/releases/1.5.7/CMFQuickInstallerTool-1.5.7.tar.gz'),
    ZProduct('Five', 'http://codespeak.net/z3/five/release/Five-1.2.1.tgz'),
    ZProduct('GroupUserFolder', PLONE_ORG + 'groupuserfolder/releases/3.5/groupuserfolder-3-5-tar.gz'),
    ZProduct('PlacelessTranslationService',  PLONE_ORG + 'pts/releases/1.2.7/PlacelessTranslationService-1.2.7.tar.gz'),
    ZProduct('PloneErrorReporting',PLONE_ORG + 'ploneerrorreporting/releases/0.11/PloneErrorReporting-0.11.tar.gz'),
    ZProduct('PloneTranslations',PLONE_ORG + 'plonetranslations/releases/2.5-beta1/PloneTranslations-2.5-beta1.tar.gz'),
    ZProduct('PloneLanguageTool', PLONE_ORG + 'plonelanguagetool/releases/1.0/PloneLanguageTool-1.0.tar.gz'),
    ZProduct('SecureMailHost', PLONE_ORG + 'securemailhost/releases/1.0.3/SecureMailHost-1.0.3.tar.gz'),
    ZProduct('ExtendedPathIndex', PLONE_ORG + 'extendedpathindex/releases/2.3/ExtendedPathIndex-2.3.tar.gz'),
    ZProduct('ResourceRegistries', PLONE_ORG + 'resourceregistries/releases/1.3/resourceregistries-1-3-alpha1-tar.gz'),
    ZProduct('statusmessages', PLONE_ORG + 'statusmessages/releases/1.1/statusmessages-1.1.tar.gz'),
    ZProduct('PlonePAS', PLONE_ORG + 'plonepas/releases/1.2/plonepas-1-2-tar.gz'),
    ZProduct('PluggableAuthService', ZOPE + 'urbanape/PluggableAuthService/PluggableAuthService-1.2-beta/PluggableAuthService-1.2-beta.tar.gz'),
    ZProduct('PasswordResetTool', BASE + 'collective/PasswordResetTool-0.3.0.tar.gz'),
    ZProduct('PluginRegistry', ZOPE + 'urbanape/PluginRegistry/PluginRegistry-1.1/PluginRegistry-1.1.tar.gz', 'PluginRegistry-1.1'),
]

ADDONS = [
    ZProduct('ExternalEditor', 'http://plope.com/software/ExternalEditor/ExternalEditor-0.9.1-src.tgz'),
    ZProduct('kupu', OSCOM_ORG + 'midcom-serveattachmentguid-e73585dd09549cfe130f91177d889819/kupu-1.3.5.tar.gz')
]

AT1_4 = [
    ZProduct('Archetypes', PLONE_ORG + 'archetypes/releases/1.4-alpha2/archetypes-1-4-0-alpha02-bundle.tar.gz'),
]

README_TXT = """Plone's README is in CMFPlone/README.txt
"""

class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.3.5/Python-2.3.5.tgz')
    zope   =  Software('zope'  , 'http://zope.org/Products/Zope/2.8.6/Zope-2.8.6-final.tgz')

    # plone core
    core   = PLONE_CORE

    # plone addons
    addons = ADDONS + AT1_4

    # the readme.txt
    readme = README_TXT

