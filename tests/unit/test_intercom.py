#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import os

from . import create_response
from mock import patch
from nose.tools import raises
from unittest import TestCase

from intercom import ServerError
from intercom import AuthenticationError
from intercom import ResourceNotFound
from intercom import Intercom
from intercom.user import CustomData
from intercom.user import SocialProfile
from intercom.user import User

class IntercomUsersTest(TestCase):

    @raises(AuthenticationError)
    @patch('requests.request', create_response(401))
    def test_create_user_identifiers(self):
        Intercom.create_user()

    @patch('requests.request', create_response(200, 'create_user_valid.json'))
    def test_create_valid(self):
        resp = Intercom.create_user(email='xxx@example.com')
        self.assertEqual(None, resp['user_id'])
        self.assertEqual('xxx@example.com', resp['email'])

    @raises(AuthenticationError)
    @patch('requests.request', create_response(401))
    def test_get_user_identifiers(self):
        Intercom.get_user()

    @patch('requests.request', create_response(200, 'get_user_valid.json'))
    def test_get_user_valid(self):
        resp = Intercom.get_user(email='xxx@example.com')
        self.assertEqual(None, resp['user_id'])
        self.assertEqual('xxx@example.com', resp['email'])

    @raises(AuthenticationError)
    @patch('requests.request', create_response(401))
    def test_create_user_identifiers(self):
        Intercom.update_user()

    @patch('requests.request', create_response(200, 'update_user_valid.json'))
    def test_update_user_valid(self):
        resp = Intercom.update_user(
                email='xxx@example.com', custom_data={'age': '42'} )
        self.assertEqual(None, resp['user_id'])
        self.assertEqual('xxx@example.com', resp['email'])
        self.assertEqual('42', resp['custom_data']['age'])

    @raises(AuthenticationError)
    @patch('requests.request', create_response(401))
    def test_get_users_identifiers(self):
        Intercom.create_user()

    @patch('requests.request', create_response(200, 'get_users_valid.json'))
    def test_get_users_valid(self):
        resp = Intercom.get_users()
        self.assertEqual(3, len(resp['users']))
        self.assertEqual(3, resp['total_count'])
        self.assertEqual(1, resp['total_pages'])

    @raises(ResourceNotFound)
    @patch('requests.request', create_response(404, '404.json'))
    def test_not_found(self):
        resp = Intercom.get_users()

    @raises(ServerError)
    @patch('requests.request', create_response(500, '500.json'))
    def test_api_error(self):
        resp = Intercom.get_users()

    @raises(ServerError)
    @patch('requests.request', create_response(500, 'invalid.json'))
    def test_api_error_when_json_is_invalid(self):
        Intercom.get_users()
