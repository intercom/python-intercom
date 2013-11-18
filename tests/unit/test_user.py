# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import time

from datetime import datetime
from mock import patch
from nose.tools import raises
from unittest import TestCase

from . import create_response
from . import local_response

from intercom import AuthenticationError
from intercom.user import CustomData
from intercom.user import LocationData
from intercom.user import SocialProfile
from intercom.user import User
from intercom.user import Company


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

class CompanyTest(TestCase):
    """ Test the Company object. """

    def test_properties(self):
        c_dict = {
            'id': 1,
            'name': 'Intercom',
            'created_at': 1331764344
        }
        company = Company(c_dict)
        self.assertEqual(1, company.id)
        self.assertEqual('Intercom', company.name)
        self.assertEqual(datetime.fromtimestamp(1331764344), company.created_at)

class UsersTest(TestCase):

    @patch('requests.request', create_response(200, 'create_user_valid.json'))
    def test_create(self):
        user = User.create(email='xxx@example.com')
        self.assertEqual(None, user.user_id)
        self.assertEqual('xxx@example.com', user.email)

    @patch('requests.request', create_response(200, 'delete_user_valid.json'))
    def test_delete(self):
        user = User.delete(email='xxx@example.com')
        self.assertEqual(u'7902', user.user_id)
        self.assertEqual('ben@intercom.io', user.email)

    @raises(AuthenticationError)
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
        self.assertEqual('Joe', user.name)
        self.assertEqual('192.168.1.100', user.last_seen_ip)
        self.assertEqual('Mozilla/5.0', user.last_seen_user_agent)
        self.assertEqual(50, user.relationship_score)
        self.assertTrue(isinstance(user.last_impression_at, datetime))
        self.assertEqual(1331834352,
                time.mktime(user.last_impression_at.timetuple()))
        self.assertTrue(isinstance(user.created_at, datetime))
        self.assertEqual(1331764344,
                time.mktime(user.created_at.timetuple()))
        self.assertTrue(1, len(user.social_profiles))
        profile = user.social_profiles[0]
        self.assertTrue(isinstance(profile, SocialProfile))
        self.assertEqual('twitter', profile.type)
        self.assertEqual('foo', profile.username)
        self.assertEqual('http://twitter.com/foo', profile.url)
        self.assertEqual('1234567', profile.id)
        self.assertEqual('Santiago', user.location_data['city_name'])
        self.assertEqual('Santiago', user.location_data.city_name)
        self.assertTrue(isinstance(user.location_data, LocationData))
        self.assertEqual('johnny', user.custom_data['nick'])
        self.assertRaises(AttributeError, lambda: user.companies)

    @patch('requests.request', create_response(200, 'get_user_id_valid.json'))
    def test_find_by_user_id(self):
        user = User.find_by_user_id(1234)
        self.assertEqual(1234, user.user_id)

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

    def test_properties(self):
        user = User()
        user.email = 'xxx@example.com'
        user.user_id = 1234
        user.name = 'Joe'
        user.last_seen_ip = '192.168.1.100'
        user.last_seen_user_agent = 'Mozilla/5.0'
        user.created_at = datetime.fromtimestamp(1331764344)
        user.custom_data = { 'name': 'Ace' }
        user.companies = [{
            'id': 1,
            'name':' Intercom',
            'created_at': datetime.fromtimestamp(1331764344)}]
        try:
            # cannot set the relationship score
            user.relationship_score = 50
            self.fail()
        except AttributeError:
            pass

        self.assertEqual('xxx@example.com', user.email)
        self.assertEqual(1234, user.user_id)
        self.assertEqual('Joe', user.name)
        self.assertEqual('192.168.1.100', user.last_seen_ip)
        self.assertEqual('Mozilla/5.0', user.last_seen_user_agent)
        self.assertEqual(None, user.relationship_score)
        self.assertEqual(1331764344,
                time.mktime(user.created_at.timetuple()))
        self.assertEqual('Ace', user.custom_data['name'])
        self.assertRaises(AttributeError, lambda: user.companies)

    def test_company(self):
        user = User()
        user.company = {
            'id': 1,
            'name':' Intercom',
            'created_at': datetime.fromtimestamp(1331764344)}
        self.assertRaises(AttributeError, lambda: user.company)
        try:
            user.company = ['foo']
            self.fail()
        except ValueError:
            pass

    def test_companies(self):
        user = User()
        user.companies = [{
            'id': 1,
            'name':' Intercom',
            'created_at': datetime.fromtimestamp(1331764344)}]
        self.assertRaises(AttributeError, lambda: user.companies)
        try:
            user.companies = {'foo':'bar'}
            self.fail()
        except ValueError:
            pass

class LocationDataTest(TestCase):

    @raises(AttributeError)
    def test_setattr(self):
        location_data = LocationData()
        location_data.city_name = "Dublin"

    @raises(NotImplementedError)
    def test_setitem(self):
        location_data = LocationData()
        location_data['city_name'] = "Dublin"

    def test_properties(self):
        location_data = LocationData({
            "city_name": "Santiago",
            "continent_code": "SA",
            "country_name": "Chile",
            "latitude": -33.44999999999999,
            "longitude": -70.6667,
            "postal_code": "",
            "region_name": "12",
            "timezone": "Chile/Continental",
            "country_code": "CHL"
        })

        self.assertEqual('Santiago', location_data.city_name)
        self.assertEqual('SA', location_data.continent_code)
        self.assertEqual('Chile', location_data.country_name)
        self.assertEqual(-33.44999999999999, location_data.latitude)
        self.assertEqual(-70.6667, location_data.longitude)
        self.assertEqual('', location_data.postal_code)
        self.assertEqual('12', location_data.region_name)
        self.assertEqual('Chile/Continental', location_data.timezone)
        self.assertEqual('CHL', location_data.country_code)
