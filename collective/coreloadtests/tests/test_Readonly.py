# -*- coding: iso-8859-15 -*-
"""ReadOnly FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
from webunit.utility import Upload
from funkload.utils import Data
#from funkload.utils import xmlrpc_get_credential

class Readonly(FunkLoadTestCase):
    """Read only load test scenario

    This test use a configuration file Readonly.conf.
    """

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url')
        # XXX here you can setup the credential access like this
        # credential_host = self.conf_get('credential', 'host')
        # credential_port = self.conf_getInt('credential', 'port')
        # self.login, self.password = xmlrpc_get_credential(credential_host,
        #                                                   credential_port,
        # XXX replace with a valid group
        #                                                   'members')

    def test_ReadOnly(self):
        # The description should be set in the configuration file
        server_url = self.server_url
        # begin of test ---------------------------------------------

        self.get(server_url + "/plone",
            description="Get /plone")

        self.get(server_url + "/plone/@@overview-controlpanel",
            description="Get /plone/@@overview-controlpanel")

        self.get(server_url + "/plone/contact-info",
            description="Get /plone/contact-info")

        self.get(server_url + "/plone/folder_listing",
            description="Get plone/folder_listing")

        self.get(server_url + "/plone/sitemap",
            description="Get plone/sitemap")


        # end of test -----------------------------------------------

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")

def test_suite():
    return unittest.makeSuite(Readonly)

additional_tests = test_suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
    
