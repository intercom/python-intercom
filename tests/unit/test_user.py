# -*- coding: utf-8 -*-

import json
import mock
import time
import unittest

from datetime import datetime
from intercom.collection_proxy import CollectionProxy
from intercom.lib.flat_store import FlatStore
from intercom import Intercom
from intercom import User
from intercom import MultipleMatchingUsersError
from intercom.utils import create_class_instance
from mock import patch
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import istest
from tests.unit import get_user
from tests.unit import mock_response


class UserTest(unittest.TestCase):

    @istest
    def it_to_dict_itself(self):
        created_at = datetime.utcnow()
        user = User(
            email="jim@example.com", user_id="12345",
            created_at=created_at, name="Jim Bob")
        as_dict = user.to_dict
        eq_(as_dict["email"], "jim@example.com")
        eq_(as_dict["user_id"], "12345")
        eq_(as_dict["created_at"], time.mktime(created_at.timetuple()))
        eq_(as_dict["name"], "Jim Bob")

    @istest
    def it_presents_created_at_and_last_impression_at_as_datetime(self):
        now = datetime.utcnow()
        now_ts = time.mktime(now.timetuple())
        user = User.from_api(
            {'created_at': now_ts, 'last_impression_at': now_ts})
        self.assertIsInstance(user.created_at, datetime)
        eq_(now.strftime('%c'), user.created_at.strftime('%c'))
        self.assertIsInstance(user.last_impression_at, datetime)
        eq_(now.strftime('%c'), user.last_impression_at.strftime('%c'))

    @istest
    def it_throws_an_attribute_error_on_trying_to_access_an_attribute_that_has_not_been_set(self):  # noqa
        with assert_raises(AttributeError):
            user = User()
            user.foo_property

    @istest
    def it_presents_a_complete_user_record_correctly(self):
        user = User.from_api(get_user())
        eq_('id-from-customers-app', user.user_id)
        eq_('bob@example.com', user.email)
        eq_('Joe Schmoe', user.name)
        eq_('the-app-id', user.app_id)
        eq_(123, user.session_count)
        eq_(1401970114, time.mktime(user.created_at.timetuple()))
        eq_(1393613864, time.mktime(user.remote_created_at.timetuple()))
        eq_(1401970114, time.mktime(user.updated_at.timetuple()))

        Avatar = create_class_instance('Avatar')  # noqa
        Company = create_class_instance('Company')  # noqa
        SocialProfile = create_class_instance('SocialProfile')  # noqa
        LocationData = create_class_instance('LocationData')  # noqa
        self.assertIsInstance(user.avatar, Avatar.__class__)
        img_url = 'https://graph.facebook.com/1/picture?width=24&height=24'
        eq_(img_url, user.avatar.image_url)

        self.assertIsInstance(user.companies, list)
        eq_(1, len(user.companies))
        self.assertIsInstance(user.companies[0], Company.__class__)
        eq_('123', user.companies[0].company_id)
        eq_('bbbbbbbbbbbbbbbbbbbbbbbb', user.companies[0].id)
        eq_('the-app-id', user.companies[0].app_id)
        eq_('Company 1', user.companies[0].name)
        eq_(1390936440, time.mktime(
            user.companies[0].remote_created_at.timetuple()))
        eq_(1401970114, time.mktime(
            user.companies[0].created_at.timetuple()))
        eq_(1401970114, time.mktime(
            user.companies[0].updated_at.timetuple()))
        eq_(1401970113, time.mktime(
            user.companies[0].last_request_at.timetuple()))
        eq_(0, user.companies[0].monthly_spend)
        eq_(0, user.companies[0].session_count)
        eq_(1, user.companies[0].user_count)
        eq_([], user.companies[0].tag_ids)

        self.assertIsInstance(user.custom_attributes, FlatStore)
        eq_('b', user.custom_attributes["a"])
        eq_(2, user.custom_attributes["b"])

        eq_(4, len(user.social_profiles))
        twitter_account = user.social_profiles[0]
        self.assertIsInstance(twitter_account, SocialProfile.__class__)
        eq_('twitter', twitter_account.name)
        eq_('abc', twitter_account.username)
        eq_('http://twitter.com/abc', twitter_account.url)

        self.assertIsInstance(user.location_data, LocationData.__class__)
        eq_('Dublin', user.location_data.city_name)
        eq_('EU', user.location_data.continent_code)
        eq_('Ireland', user.location_data.country_name)
        eq_('90', user.location_data.latitude)
        eq_('10', user.location_data.longitude)
        eq_('IRL', user.location_data.country_code)

        ok_(user.unsubscribed_from_emails)
        eq_("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", user.user_agent_data)  # noqa

    @istest
    def it_allows_update_last_request_at(self):
        payload = {
            'user_id': '1224242',
            'update_last_request_at': True,
            'custom_attributes': {}
        }
        with patch.object(Intercom, 'post', return_value=payload) as mock_method:
            User.create(user_id='1224242', update_last_request_at=True)
            mock_method.assert_called_once_with(
                '/users/', update_last_request_at=True, user_id='1224242')

    @istest
    def it_allows_easy_setting_of_custom_data(self):
        now = datetime.utcnow()
        now_ts = time.mktime(now.timetuple())

        user = User()
        user.custom_attributes["mad"] = 123
        user.custom_attributes["other"] = now_ts
        user.custom_attributes["thing"] = "yay"
        attrs = {"mad": 123, "other": now_ts, "thing": "yay"}
        eq_(user.to_dict["custom_attributes"], attrs)

    @istest
    def it_allows_easy_setting_of_multiple_companies(self):
        user = User()
        companies = [
            {"name": "Intercom", "company_id": "6"},
            {"name": "Test", "company_id": "9"},
        ]
        user.companies = companies
        eq_(user.to_dict["companies"], companies)

    @istest
    def it_rejects_nested_data_structures_in_custom_attributes(self):
        user = User()
        with assert_raises(ValueError):
            user.custom_attributes["thing"] = [1]

        with assert_raises(ValueError):
            user.custom_attributes["thing"] = {1: 2}

        with assert_raises(ValueError):
            user.custom_attributes = {1: {2: 3}}

        user = User.from_api(get_user())
        with assert_raises(ValueError):
            user.custom_attributes["thing"] = [1]

    @istest
    def it_fetches_a_user(self):
        with patch.object(Intercom, 'get', return_value=get_user()) as mock_method:  # noqa
            user = User.find(email='somebody@example.com')
            eq_(user.email, 'bob@example.com')
            eq_(user.name, 'Joe Schmoe')
            mock_method.assert_called_once_with('/users', email='somebody@example.com')  # noqa

    @istest
    # @httpretty.activate
    def it_saves_a_user_always_sends_custom_attributes(self):
        user = User(email="jo@example.com", user_id="i-1224242")

        body = {
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'custom_attributes': {}
        }

        with patch.object(Intercom, 'post', return_value=body) as mock_method:
            user.save()
            eq_(user.email, 'jo@example.com')
            eq_(user.custom_attributes, {})
            mock_method.assert_called_once_with(
                '/users',
                email="jo@example.com", user_id="i-1224242",
                custom_attributes={})

    @istest
    def it_saves_a_user_with_a_company(self):
        user = User(
            email="jo@example.com", user_id="i-1224242",
            company={'company_id': 6, 'name': 'Intercom'})

        body = {
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        }
        with patch.object(Intercom, 'post', return_value=body) as mock_method:
            user.save()
            eq_(user.email, 'jo@example.com')
            eq_(len(user.companies), 1)
            mock_method.assert_called_once_with(
                '/users',
                email="jo@example.com", user_id="i-1224242",
                company={'company_id': 6, 'name': 'Intercom'},
                custom_attributes={})

    @istest
    def it_saves_a_user_with_companies(self):
        user = User(
            email="jo@example.com", user_id="i-1224242",
            companies=[{'company_id': 6, 'name': 'Intercom'}])
        body = {
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        }
        with patch.object(Intercom, 'post', return_value=body) as mock_method:
            user.save()
            eq_(user.email, 'jo@example.com')
            eq_(len(user.companies), 1)
            mock_method.assert_called_once_with(
                '/users',
                email="jo@example.com", user_id="i-1224242",
                companies=[{'company_id': 6, 'name': 'Intercom'}],
                custom_attributes={})

    @istest
    def it_can_save_a_user_with_a_none_email(self):
        user = User(
            email=None, user_id="i-1224242",
            companies=[{'company_id': 6, 'name': 'Intercom'}])
        body = {
            'custom_attributes': {},
            'email': None,
            'user_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        }
        with patch.object(Intercom, 'post', return_value=body) as mock_method:
            user.save()
            ok_(user.email is None)
            eq_(user.user_id, 'i-1224242')
            mock_method.assert_called_once_with(
                '/users',
                email=None, user_id="i-1224242",
                companies=[{'company_id': 6, 'name': 'Intercom'}],
                custom_attributes={})

    @istest
    def it_deletes_a_user(self):
        user = User(id="1")
        with patch.object(Intercom, 'delete', return_value={}) as mock_method:
            user = user.delete()
            eq_(user.id, "1")
            mock_method.assert_called_once_with('/users/1/')

    @istest
    def it_can_use_user_create_for_convenience(self):
        payload = {
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'custom_attributes': {}
        }
        with patch.object(Intercom, 'post', return_value=payload) as mock_method:  # noqa
            user = User.create(email="jo@example.com", user_id="i-1224242")
            eq_(payload, user.to_dict)
            mock_method.assert_called_once_with('/users/', email="jo@example.com", user_id="i-1224242")  # noqa

    @istest
    def it_updates_the_user_with_attributes_set_by_the_server(self):
        payload = {
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'custom_attributes': {},
            'session_count': 4
        }
        with patch.object(Intercom, 'post', return_value=payload) as mock_method:
            user = User.create(email="jo@example.com", user_id="i-1224242")
            eq_(payload, user.to_dict)
            mock_method.assert_called_once_with('/users/', email="jo@example.com", user_id="i-1224242")  # noqa

    @istest
    def it_allows_setting_dates_to_none_without_converting_them_to_0(self):
        payload = {
            'email': 'jo@example.com',
            'custom_attributes': {},
            'remote_created_at': None
        }
        with patch.object(Intercom, 'post', return_value=payload) as mock_method:
            user = User.create(email="jo@example.com", remote_created_at=None)
            ok_(user.remote_created_at is None)
            mock_method.assert_called_once_with('/users/', email="jo@example.com", remote_created_at=None)  # noqa

    @istest
    def it_gets_sets_rw_keys(self):
        created_at = datetime.utcnow()
        payload = {
            'email': 'me@example.com',
            'user_id': 'abc123',
            'name': 'Bob Smith',
            'last_seen_ip': '1.2.3.4',
            'last_seen_user_agent': 'ie6',
            'created_at': time.mktime(created_at.timetuple())
        }
        user = User(**payload)
        expected_keys = ['custom_attributes']
        expected_keys.extend(list(payload.keys()))
        eq_(sorted(expected_keys), sorted(user.to_dict.keys()))
        for key in list(payload.keys()):
            eq_(payload[key], user.to_dict[key])

    @istest
    def it_will_allow_extra_attributes_in_response_from_api(self):
        user = User.from_api({'new_param': 'some value'})
        eq_('some value', user.new_param)

    @istest
    def it_returns_a_collectionproxy_for_all_without_making_any_requests(self):
        with mock.patch('intercom.Request.send_request_to_path', new_callable=mock.NonCallableMock):  # noqa
            res = User.all()
            self.assertIsInstance(res, CollectionProxy)

    @istest
    def it_returns_the_total_number_of_users(self):
        with mock.patch.object(User, 'count') as mock_count:
            mock_count.return_value = 100
            eq_(100, User.count())

    @istest
    def it_raises_a_multiple_matching_users_error_when_receiving_a_conflict(self):  # noqa
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'code': 'conflict',
                    'message': 'Multiple existing users match this email address - must be more specific using user_id'  # noqa
                }
            ]
        }
        # create bytes content
        content = json.dumps(payload).encode('utf-8')
        # create mock response
        resp = mock_response(content)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(MultipleMatchingUsersError):
                Intercom.get('/users')

    @istest
    def it_handles_accented_characters(self):
        # create a user dict with a name that contains accented characters
        payload = get_user(name='Jóe Schmö')
        # create bytes content
        content = json.dumps(payload).encode('utf-8')
        # create mock response
        resp = mock_response(content)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            user = User.find(email='bob@example.com')
            try:
                # Python 2
                eq_(unicode('Jóe Schmö', 'utf-8'), user.name)
            except NameError:
                # Python 3
                eq_('Jóe Schmö', user.name)


class DescribeIncrementingCustomAttributeFields(unittest.TestCase):

    def setUp(self):  # noqa
        created_at = datetime.utcnow()
        params = {
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'custom_attributes': {
                'mad': 123,
                'another': 432,
                'other': time.mktime(created_at.timetuple()),
                'thing': 'yay'
            }
        }
        self.user = User(**params)

    @istest
    def it_increments_up_by_1_with_no_args(self):
        self.user.increment('mad')
        eq_(self.user.to_dict['custom_attributes']['mad'], 124)

    @istest
    def it_increments_up_by_given_value(self):
        self.user.increment('mad', 4)
        eq_(self.user.to_dict['custom_attributes']['mad'], 127)

    @istest
    def it_increments_down_by_given_value(self):
        self.user.increment('mad', -1)
        eq_(self.user.to_dict['custom_attributes']['mad'], 122)

    @istest
    def it_can_increment_new_custom_data_fields(self):
        self.user.increment('new_field', 3)
        eq_(self.user.to_dict['custom_attributes']['new_field'], 3)

    @istest
    def it_can_call_increment_on_the_same_key_twice_and_increment_by_2(self):  # noqa
        self.user.increment('mad')
        self.user.increment('mad')
        eq_(self.user.to_dict['custom_attributes']['mad'], 125)

    @istest
    def it_can_save_after_increment(self):  # noqa
        user = User(
            email=None, user_id="i-1224242",
            companies=[{'company_id': 6, 'name': 'Intercom'}])
        body = {
            'custom_attributes': {},
            'email': "",
            'user_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        }
        with patch.object(Intercom, 'post', return_value=body) as mock_method:  # noqa
            user.increment('mad')
            eq_(user.to_dict['custom_attributes']['mad'], 1)
            user.save()
            ok_('email' not in user.identity_hash)
            ok_('user_id' in user.identity_hash)
