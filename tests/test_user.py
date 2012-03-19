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

from intercom.intercom import AuthError
from intercom.user import CustomData
from intercom.user import SocialProfile
from intercom.user import User

class CustomDataTest(TestCase):
    """ Test the CustomData object. """

    def test_init_no_arg(self):
        # no arg __init__
        custom_data = CustomData()
        self.assertEqual(0, len(custom_data))

    def test_init_dict_arg(self):
        # dict arg __init__
        custom_data = CustomData({'color': 'red'})
        self.assertEqual(1, len(custom_data))

    def test_string_key(self):
        # string keys are allowed
        custom_data = CustomData()
        custom_data['a'] = 'b'

    @raises(ValueError)
    def test_numeric_key(self):
        # numeric keys are not allowed
        custom_data = CustomData()
        custom_data[1] = 'a'

    @raises(ValueError)
    def test_dict_key(self):
        # dict keys are not allowed
        custom_data = CustomData()
        custom_data[{'a': 'b'}] = 'c'

    def test_numeric_values(self):
        # numeric values are allowed
        custom_data = CustomData()
        custom_data['a'] = 1
        custom_data['b'] = 3.14
        custom_data['c'] = 0177
        custom_data['d'] = 0x7F

    @raises(ValueError)
    def test_complex_number_values(self):
        # complex numeber values are allowed
        custom_data = CustomData()
        custom_data['a'] = complex(1.0, 0.2)

    @raises(ValueError)
    def test_dict_value(self):
        # dict values are not allowed
        custom_data = CustomData()
        custom_data['a'] = { 'b': 'c' }

    @raises(ValueError)
    def test_list_value(self):
        # list values are not allowed
        custom_data = CustomData()
        custom_data['a'] = ['b', 'c']

class SocialProfileTest(TestCase):

    def test_attr(self):
        sc_dict = {
            'type': 'twitter',
            'url': 'http://twitter.com/myname',
            'username': 'myname',
            'id': '123456789'
        }

        social_profile = SocialProfile(sc_dict)
        self.assertEqual('twitter', social_profile.type)
        self.assertEqual('http://twitter.com/myname', social_profile.url)
        self.assertEqual('myname', social_profile.username)
        self.assertEqual('123456789', social_profile.id)

    @raises(NotImplementedError)
    def test_setitem(self):
        social_profile = SocialProfile()
        social_profile['type'] = 'facebook'

class UsersTest(TestCase):

    @patch('requests.request', create_response(200, 'create_user_valid.json'))
    def test_create(self):
        user = User.create(email='xxx@example.com')
        self.assertEqual(None, user.user_id)
        self.assertEqual('xxx@example.com', user.email)

    @raises(AuthError)
    @patch('requests.request', create_response(401))
    def test_find_identifiers(self):
        User.find()

    @patch('requests.request', create_response(200, 'get_user_valid.json'))
    def test_find(self):
        user = User.find(email='xxx@example.com')
        self.assertEqual(None, user.user_id)
        self.assertEqual('xxx@example.com', user.email)

    @patch('requests.request', create_response(200, 'get_user_valid.json'))
    def test_find_by_email(self):
        user = User.find_by_email('xxx@example.com')
        self.assertEqual(None, user.user_id)
        self.assertEqual('xxx@example.com', user.email)

    @patch('requests.request', create_response(200, 'update_user_valid.json'))
    def test_save_user(self):
        user = User(email='xxx@example.com', custom_data={'age': '42'})
        user.save()
        self.assertEqual(None, user.user_id)
        self.assertEqual('xxx@example.com', user.email)
        self.assertEqual('42', user.custom_data['age'])
        self.assertEqual(1, user.session_count)

    @patch('requests.request', create_response(200, 'get_users_valid.json'))
    def test_get_users_valid(self):
        users = User.all()
        self.assertEqual(3, len(users))
        self.assertEqual('joebloggs@example.com', users[0].email)
        self.assertEqual('foobloggs@example.com', users[1].email)
        self.assertEqual('barbloggs@example.com', users[2].email)
