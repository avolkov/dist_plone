from dist_plone import Software, PyModule, ZProduct, Bundle

BASE = 'http://osdn.dl.sourceforge.net/sourceforge/'

PLONE_BASE = BASE + 'plone/'
PLONE_BASE = 'http://home.wiggy.net/~wichert/'

PLONE_ORG = 'http://plone.org/products/'
OSCOM_ORG = 'http://kupu.oscom.org/'
ZOPE_ORG = 'http://www.zope.org/Products/'

PLONE_CORE = [
    Bundle('CMF',
           'http://www.zope.org/Products/CMF/CMF-2.1.0-alpha/CMF-2.1.0-alpha.tar.gz',
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
    ZProduct('ATContentTypes', PLONE_ORG + 'atcontenttypes/releases/1.2/ATContentTypes-1.2-alpha1.tgz'),
    ZProduct('ATReferenceBrowserWidget', PLONE_ORG + 'atreferencebrowserwidget/releases/1.6/ATReferenceBrowserWidget-1.6.tar.gz'),
    ZProduct('CacheFu', PLONE_ORG + 'cachefu/releases/1.0.1/CacheFu-1.0.1.tgz', 'CacheFu-1.0.1'),
    ZProduct('CMFDynamicViewFTI', PLONE_ORG + 'cmfdynamicviewfti/releases/2.1/CMFDynamicViewFTI-2.1.tar.gz'),
    ZProduct('CMFFormController', PLONE_ORG + 'cmfformcontroller/releases/2.0.6/CMFFormController-2.0.6.tar.gz'),
    ZProduct('CMFPlacefulWorkflow', PLONE_ORG + 'cmfplacefulworkflow/releases/1.0.2/CMFPlacefulWorkflow-1.0.2.tgz'),
    ZProduct('CMFPlone', PLONE_BASE + 'PloneBase-3.0-alpha1.tar.gz'),
    ZProduct('CMFQuickInstallerTool', PLONE_ORG + 'cmfquickinstallertool/releases/2.0.0/CMFQuickInstallerTool-2.0.0.tar.gz'),
    ZProduct('CMFDiffTool', PLONE_ORG + 'cmfdifftool/releases/0.3/CMFDiffTool-0.3.tgz'),
    ZProduct('ExtendedPathIndex', PLONE_ORG + 'extendedpathindex/releases/2.4/ExtendedPathIndex-2.4.tgz'),
    ZProduct('GroupUserFolder', PLONE_ORG + 'groupuserfolder/releases/3.54/GroupUserFolder-3.54.tgz'),
    ZProduct('PlacelessTranslationService',  PLONE_ORG + 'pts/releases/1.4.0/PlacelessTranslationService-1.4.0.tar.gz'),
    ZProduct('PloneErrorReporting',PLONE_ORG + 'ploneerrorreporting/releases/1.0/PloneErrorReporting-1.0.tar.gz'),
    ZProduct('PloneTestCase',PLONE_ORG + 'plonetestcase/releases/0.8.6/PloneTestCase-0.8.6.tar.gz'),
    ZProduct('PloneTranslations',PLONE_ORG + 'plonetranslations/releases/2.6.0/PloneTranslations-2.6.0.tar.gz'),
    ZProduct('PloneLanguageTool', PLONE_ORG + 'plonelanguagetool/releases/1.4/PloneLanguageTool-1.4.tar.gz'),
    ZProduct('SecureMailHost', PLONE_ORG + 'securemailhost/releases/1.0.4/SecureMailHost-1.0.4.tar.gz'),
    ZProduct('ResourceRegistries', PLONE_ORG + 'resourceregistries/releases/1.3.2/ResourceRegistries-1.3.2.tar.gz'),
    ZProduct('statusmessages', PLONE_ORG + 'statusmessages/releases/2.1/statusmessages-2.1.tar.gz'),
    ZProduct('PlonePAS', PLONE_ORG + 'plonepas/releases/2.1/PlonePAS-2.1.tar.gz'),
    ZProduct('PluggableAuthService', ZOPE_ORG + 'PluggableAuthService/PluggableAuthService-1.4/PluggableAuthService-1.4.tar.gz', 'PluggableAuthService-1.4'),
    ZProduct('PasswordResetTool', PLONE_ORG + 'passwordresettool/releases/0.4.1/PasswordResetTool-0.4.1.tar.gz'),
    ZProduct('PluginRegistry', ZOPE_ORG + 'PluginRegistry/PluginRegistry-1.1.1/PluginRegistry-1.1.1.tar.gz', 'PluginRegistry-1.1.1'),
    ZProduct('ZopeVersionControl', 'http://antiloop.plone.org/download/ZopeVersionControl-0.3.3.tar.gz'),
    ZProduct('CMFEditions', PLONE_ORG + 'cmfeditions/releases/1.1/CMFEditions-1.1-alpha1.tgz'),
]

PLONE_CORE_PACKAGES = [
    PyModule('plone.portlets', 'http://antiloop.plone.org/download/plone.portlets-0.1dev-r11127.tar.gz'),
    PyModule('plone.app.portlets', 'http://antiloop.plone.org/download/plone.app.portlets-0.1dev-r11257.tar.gz'),
]


ADDONS = [
    ZProduct('ExternalEditor', 'http://plope.com/software/ExternalEditor/ExternalEditor-0.9.2-src.tgz'),
    ZProduct('kupu', PLONE_ORG + 'kupu/releases/1.4/kupu-1.4b2.tgz')
]

AT1_5 = [
    ZProduct('Archetypes', PLONE_ORG + 'archetypes/releases/1.5/Archetypes-1.5.0-a1-all.tar.gz'),
]

README_TXT = """Plone's README is in CMFPlone/README.txt
"""

class Distribution:

    target = 'independent'

    # this is what plone is based on
    python =  Software('python', 'http://python.org/ftp/python/2.4.3/Python-2.4.3.tgz')
    zope   =  Software('zope'  , ZOPE_ORG + 'Zope/2.10.0/Zope-2.10.0-final.tgz')

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

