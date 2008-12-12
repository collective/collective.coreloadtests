# -*- coding: iso-8859-15 -*-
"""WriteHeavy FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
from webunit.utility import Upload
from funkload.utils import Data
from funkload.Lipsum import Lipsum, V_ASCII, CHARS, SEP

#from funkload.utils import xmlrpc_get_credential

class Writeheavy(FunkLoadTestCase):
    """Heavy write load test scenario

    This test use a configuration file Writeheavy.conf.
    """

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url')
        self.lipsum = Lipsum(vocab=V_ASCII, chars=CHARS, sep=SEP)
        # XXX here you can setup the credential access like this
        # credential_host = self.conf_get('credential', 'host')
        # credential_port = self.conf_getInt('credential', 'port')
        # self.login, self.password = xmlrpc_get_credential(credential_host,
        #                                                   credential_port,
        # XXX replace with a valid group
        #                                                   'members')

    def test_WriteHeavy(self):
        # The description should be set in the configuration file
        
        server_url = self.server_url
        # begin of test ---------------------------------------------

        self.get(server_url + "/plone",
            description="Get /plone")

        join_form = self.get(server_url + "/plone/join_form",
                          description="Get /plone/join_form")

        _authenticator = join_form.extractForm([('form',1)]).get('_authenticator')


        user_id = self.lipsum.getWord()
        user_fullname = self.lipsum.getSubject(length=2, prefix=None, uniq=True)
        
        self.post(server_url + "/plone/join_form", params=[
            ['last_visit:date', '2008/12/12 14:53:21.283 GMT'],
            ['prev_visit:date', '2008/12/12 14:53:21.283 GMT'],
            ['came_from_prefs', ''],
            ['fullname', user_fullname],
            ['username', user_id],
            ['email', 'user@foobar.com'],
            ['password', '12345'],
            ['password_confirm', '12345'],
            ['form.button.Register', 'Register'],
            ['form.submitted', '1'],
            ['_authenticator', _authenticator]],
            description="Post /plone/join_form")

        self.post(server_url + "/plone/login_form", params=[
            ['form.submitted', '1'],
            ['js_enabled', '0'],
            ['cookies_enabled', '0'],
            ['login_name', ''],
            ['pwd_empty', '0'],
            ['came_from', 'login_success'],
            ['__ac_name', user_id],
            ['__ac_password', '12345']],
            description="Post /plone/login_form")

        self.get(server_url + "/plone/dashboard",
            description="Get /plone/dashboard")

        self.get(server_url + "/plone/Members/" + user_id +"/view",
            description="Get /plone/Members/user/view")

        folder_portal_factory = self._browse(server_url + "/plone/Members/" + user_id +"/createObject?type_name=Folder",
                                             method='get', 
                                             follow_redirect=False,
                                             description = 'Get folder portal factory')

        folder_edit_url = folder_portal_factory.headers.get('Location')        
        folder_id = folder_edit_url.split('/')[-2]
 
        folder_created = self.post(server_url + "/plone/Members/" + user_id +"/portal_factory/Folder/" + folder_id +"/atct_edit", params=[
            ['id', folder_id],
            ['title', 'folder'],
            ['description', ''],
            ['description_text_format', 'text/plain'],
            ['subject_existing_keywords:default:list', ''],
            ['location', ''],
            ['language', ''],
            ['effectiveDate', ''],
            ['effectiveDate_year', '0000'],
            ['effectiveDate_month', '00'],
            ['effectiveDate_day', '00'],
            ['effectiveDate_hour', '12'],
            ['effectiveDate_minute', '00'],
            ['effectiveDate_ampm', 'AM'],
            ['expirationDate', ''],
            ['expirationDate_year', '0000'],
            ['expirationDate_month', '00'],
            ['expirationDate_day', '00'],
            ['expirationDate_hour', '12'],
            ['expirationDate_minute', '00'],
            ['expirationDate_ampm', 'AM'],
            ['creators:lines', 'user'],
            ['contributors:lines', ''],
            ['rights', ''],
            ['rights_text_format', 'text/html'],
            ['allowDiscussion:boolean:default', ''],
            ['excludeFromNav:boolean:default', ''],
            ['nextPreviousEnabled:boolean:default', ''],
            ['fieldsets:list', 'default'],
            ['fieldsets:list', 'categorization'],
            ['fieldsets:list', 'dates'],
            ['fieldsets:list', 'ownership'],
            ['fieldsets:list', 'settings'],
            ['form.submitted', '1'],
            ['add_reference.field:record', ''],
            ['add_reference.type:record', ''],
            ['add_reference.destination:record', ''],
            ['last_referer', 'http://localhost:8080/plone/Members/' + user_id + '/view'],
            ['form_submit', 'Save']],
            description="Post /plone/Members/user...280843853/atct_edit")

        new_folder_id = folder_created.url.split('/')[-2]

        document_portal_factory = self._browse(server_url + "/plone/Members/" + user_id +"/" + new_folder_id + "/createObject?type_name=Document",
                                             method='get', 
                                             follow_redirect=False,
                                             description = 'Get document portal factory')

        document_edit_url = document_portal_factory.headers.get('Location')        
        document_id = document_edit_url.split('/')[-2]
        
        self.post(server_url + "/plone/Members/" + user_id +"/" + new_folder_id + "/portal_factory/Document/" + document_id + "/atct_edit", params=[
            ['id', document_id],
            ['title', self.lipsum.getSubject(length=5, prefix=None, uniq=False,length_min=None, length_max=None)],
            ['description', self.lipsum.getMessage(length=10)],
            ['description_text_format', 'text/plain'],
            ['text_text_format', 'text/html'],
            ['text_text_format:default', 'text/html'],
            ['text', self.lipsum.getMessage(length=30)],
            ['text_file', Upload("")],
            ['subject_existing_keywords:default:list', ''],
            ['relatedItems:default:list', ''],
            ['location', ''],
            ['language', ''],
            ['effectiveDate', ''],
            ['effectiveDate_year', '0000'],
            ['effectiveDate_month', '00'],
            ['effectiveDate_day', '00'],
            ['effectiveDate_hour', '12'],
            ['effectiveDate_minute', '00'],
            ['effectiveDate_ampm', 'AM'],
            ['expirationDate', ''],
            ['expirationDate_year', '0000'],
            ['expirationDate_month', '00'],
            ['expirationDate_day', '00'],
            ['expirationDate_hour', '12'],
            ['expirationDate_minute', '00'],
            ['expirationDate_ampm', 'AM'],
            ['creators:lines', 'user'],
            ['contributors:lines', ''],
            ['rights', ''],
            ['rights_text_format', 'text/html'],
            ['allowDiscussion:boolean:default', ''],
            ['excludeFromNav:boolean:default', ''],
            ['presentation:boolean:default', ''],
            ['tableContents:boolean:default', ''],
            ['cmfeditions_version_comment', 'Lorem Ipsum'],
            ['fieldsets:list', 'default'],
            ['fieldsets:list', 'categorization'],
            ['fieldsets:list', 'dates'],
            ['fieldsets:list', 'ownership'],
            ['fieldsets:list', 'settings'],
            ['form.submitted', '1'],
            ['add_reference.field:record', ''],
            ['add_reference.type:record', ''],
            ['add_reference.destination:record', ''],
            ['last_referer', 'http://localhost:8080/plone/Members/' + user_id +'/' + new_folder_id + '/'],
            ['form_submit', 'Save']],
            description="Post /plone/Members/user...511052309/atct_edit")

        self.get(server_url + "/plone/logout",
            description="Get /plone/logout")

        # end of test -----------------------------------------------

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")

if __name__ in ('main', '__main__'):
    unittest.main()
