from dist_plone import Software, PyModule, ZProduct, Bundle

BASE = 'http://osdn.dl.sourceforge.net/sourceforge/'

PLONE_BASE = BASE + 'plone/'
PLONE_BASE = 'http://antiloop.plone.org/download/'
PLONE_GOOGLE = "http://plone.googlecode.com/files/"

PLONE_ORG = 'http://plone.org/products/'
OSCOM_ORG = 'http://kupu.oscom.org/'
ZOPE_ORG = 'http://www.zope.org/Products/'

CHEESE_SOURCE = 'http://cheeseshop.python.org/packages/source/'

PLONE_CORE = [
    Bundle('CMF',
           'http://www.zope.org/Products/CMF/CMF-2.1.0-alpha2/CMF-2.1.0-alpha2.tar.gz',
           { 'CMFActionIcons': ZProduct,
             'CMFCalendar': ZProduct,
             'CMFCore'    : ZProduct,
             'CMFDefault' : ZProduct,
             'CMFTopic'   : ZProduct,
             'CMFUid'     : ZProduct,
             'DCWorkflow' : ZProduct,
             'GenericSetup' : ZProduct,
           }
    ),
    ZProduct('ATContentTypes', PLONE_ORG + 'atcontenttypes/releases/1.2/ATContentTypes-1.2-alpha2.tgz'),
    ZProduct('ATReferenceBrowserWidget', PLONE_ORG + 'atreferencebrowserwidget/releases/1.7/ATReferenceBrowserWidget-1.7.1.tgz'),
    ZProduct('CMFDynamicViewFTI', PLONE_ORG + 'cmfdynamicviewfti/releases/2.1.1/CMFDynamicViewFTI-2.1.1.tar.gz'),
    ZProduct('CMFFormController', PLONE_ORG + 'cmfformcontroller/releases/2.0.7/CMFFormController-2.0.7.tar.gz'),
    ZProduct('CMFPlacefulWorkflow', PLONE_ORG + 'cmfplacefulworkflow/releases/1.0.2/CMFPlacefulWorkflow-1.0.2.tgz'),
    ZProduct('CMFPlone', PLONE_BASE + 'PloneBase-3.0-alpha1.tar.gz'),
    ZProduct('CMFQuickInstallerTool', PLONE_ORG + 'cmfquickinstallertool/releases/2.0.1/CMFQuickInstallerTool-2.0.1.tar.gz'),
    ZProduct('CMFDiffTool', PLONE_ORG + 'cmfdifftool/releases/0.3.1/CMFDiffTool-0.3.1.tgz'),
    ZProduct('ExtendedPathIndex', PLONE_ORG + 'extendedpathindex/releases/2.4/ExtendedPathIndex-2.4.tgz'),
    ZProduct('GroupUserFolder', PLONE_ORG + 'groupuserfolder/releases/3.54.2/GroupUserFolder-3.54.2.tgz'),
    ZProduct('PlacelessTranslationService',  PLONE_ORG + 'pts/releases/1.4.1/PlacelessTranslationService-1.4.1.tar.gz'),
    ZProduct('PloneErrorReporting',PLONE_ORG + 'ploneerrorreporting/releases/1.1/PloneErrorReporting-1.1.tar.gz'),
    ZProduct('PloneTestCase',PLONE_ORG + 'plonetestcase/releases/0.9.0/PloneTestCase-0.9.0.tar.gz'),
    ZProduct('PloneTranslations',PLONE_ORG + 'plonetranslations/releases/2.6.1/PloneTranslations-2.6.1.tar.gz'),
    ZProduct('PloneLanguageTool', PLONE_ORG + 'plonelanguagetool/releases/1.5/PloneLanguageTool-1.5.tar.gz'),
    ZProduct('SecureMailHost', PLONE_ORG + 'securemailhost/releases/1.0.4/SecureMailHost-1.0.4.tar.gz'),
    ZProduct('ResourceRegistries', PLONE_ORG + 'resourceregistries/releases/1.3.4/ResourceRegistries-1.3.4.tar.gz'),
    ZProduct('statusmessages', PLONE_ORG + 'statusmessages/releases/2.1/statusmessages-2.1.tar.gz'),
    ZProduct('PlonePAS', PLONE_ORG + 'plonepas/releases/2.2/PlonePAS-2.2.tar.gz'),
    ZProduct('PluggableAuthService', ZOPE_ORG + 'PluggableAuthService/PluggableAuthService-1.4.1/PluggableAuthService-1.4.1.tar.gz', 'PluggableAuthService-1.4.1'),
    ZProduct('PasswordResetTool', PLONE_ORG + 'passwordresettool/releases/0.4.2/PasswordResetTool-0.4.2.tar.gz'),
    ZProduct('PluginRegistry', ZOPE_ORG + 'PluginRegistry/PluginRegistry-1.1.1/PluginRegistry-1.1.1.tar.gz', 'PluginRegistry-1.1.1'),
    ZProduct('ZopeVersionControl', 'http://antiloop.plone.org/download/ZopeVersionControl-0.3.3.tar.gz'),
    ZProduct('CMFEditions', PLONE_ORG + 'cmfeditions/releases/1.1/CMFEditions-1.1-alpha2.tgz'),

# Test tools
    ZProduct('CMFTestCase', PLONE_ORG + 'cmftestcase/releases/0.9.0/CMFTestCase-0.9.0.tar.gz'),
]

PLONE_CORE_PACKAGES = [
    PyModule('archetypes.kss', CHEESE_SOURCE + 'a/archetypes.kss/archetypes.kss-1.2-alpha2.tar.gz'),
    PyModule('plone.app.contentmenu', CHEESE_SOURCE + 'p/plone.app.contentmenu/plone.app.contentmenu-1.0a2.tar.gz'),
    PyModule('plone.app.contentrules', CHEESE_SOURCE + 'p/plone.app.contentrules/plone.app.contentrules-1.0a2.tar.gz'),
    PyModule('plone.app.controlpanel', CHEESE_SOURCE + 'p/plone.app.controlpanel/plone.app.controlpanel-1.0a2.tar.gz'),
    PyModule('plone.app.iterate', CHEESE_SOURCE + 'p/plone.app.iterate/plone.app.iterate-1.0a2.tar.gz'),
    PyModule('plone.app.kss', CHEESE_SOURCE + 'p/plone.app.kss/plone.app.kss-1.2-alpha2.tar.gz'),
    PyModule('plone.app.layout', CHEESE_SOURCE + 'p/plone.app.layout/plone.app.layout-1.0a2.tar.gz'),
    PyModule('plone.app.linkintegrity', CHEESE_SOURCE + 'p/plone.app.linkintegrity/plone.app.linkintegrity-1.0a2.tar.gz'),
    PyModule('plone.app.openid', PLONE_GOOGLE + 'plone.app.openid-0.9.tar.gz'),
    PyModule('plone.app.portlets', CHEESE_SOURCE + 'p/plone.app.portlets/plone.app.portlets-1.0a2.tar.gz'),
    PyModule('plone.app.redirector', CHEESE_SOURCE + 'p/plone.app.redirector/plone.app.redirector-1.0a2.tar.gz'),
    PyModule('plone.app.vocabularies', CHEESE_SOURCE + 'p/plone.app.vocabularies/plone.app.vocabularies-1.0a2.tar.gz'),
    PyModule('plone.app.workflow', CHEESE_SOURCE + 'p/plone.app.workflow/plone.app.workflow-1.0a2.tar.gz'),
    PyModule('plone.contentrules', CHEESE_SOURCE + 'p/plone.contentrules/plone.contentrules-1.0a2.tar.gz'),
    PyModule('plone.locking', CHEESE_SOURCE + 'p/plone.locking/plone.locking-1.0a2.tar.gz'),
    PyModule('plone.memoize', CHEESE_SOURCE + 'p/plone.memoize/plone.memoize-1.0a2.tar.gz'),
    PyModule('plone.openid', PLONE_GOOGLE + 'plone.openid-0.9.tar.gz'),
    PyModule('plone.portlets', CHEESE_SOURCE + 'p/plone.portlets/plone.portlets-1.0a2.tar.gz'),
    PyModule('plone.session', PLONE_GOOGLE + 'plone.session-0.9.tar.gz'),
    PyModule('wicked', CHEESE_SOURCE + 'w/wicked/wicked-1.1.0.tar.gz'),
]


ADDONS = [
    ZProduct('ExternalEditor', PLONE_ORG + 'external-editor/releases/0.9.3/ExternalEditor-0.9.3-src.tgz'),
    ZProduct('kupu', PLONE_ORG + 'kupu/releases/1.4/kupu-1.4b3.tgz')
]

AT1_5 = [
    ZProduct('Archetypes', PLONE_ORG + 'archetypes/releases/1.5/Archetypes-1.5.0-a2.tar.gz'),
]

README_TXT = """Plone's README is in CMFPlone/README.txt
"""

class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://www.python.org/ftp/python/2.4.4/Python-2.4.4.tgz')
    zope   =  Software('zope'  , ZOPE_ORG + 'Zope/2.10.2/Zope-2.10.2.tgz')

    # plone core
    core   = PLONE_CORE
    # plone core packages
    core_packages = PLONE_CORE_PACKAGES

    # plone addons
    addons = ADDONS + AT1_5

    # the readme.txt
    readme = README_TXT

    # documentation to copy to the tar root
    documentation = [ 'README.txt', 'INSTALL.txt' ]

