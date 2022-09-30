# -*- coding: utf-8 -*-

import calendar
import json
import time
import unittest
from datetime import datetime

import mock
from mock import patch
from nose.tools import assert_raises, eq_, istest, ok_

from intercom import MultipleMatchingContactsError
from intercom.client import Client
from intercom.collection_proxy import CollectionProxy
from intercom.contact import Contact
from intercom.lib.flat_store import FlatStore
from intercom.utils import define_lightweight_class
from tests.unit import get_contact, mock_response, page_of_contacts


class ContactTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    @istest
    def it_to_dict_itself(self):
        created_at = datetime.utcnow()
        contact = Contact(
            email="jim@example.com", external_id="12345",
            created_at=created_at, name="Jim Bob")
        as_dict = contact.to_dict()
        eq_(as_dict["email"], "jim@example.com")
        eq_(as_dict["external_id"], "12345")
        eq_(as_dict["created_at"], calendar.timegm(created_at.utctimetuple()))
        eq_(as_dict["name"], "Jim Bob")

    @istest
    def it_presents_created_at_and_last_impression_at_as_datetime(self):
        now = datetime.utcnow()
        now_ts = calendar.timegm(now.utctimetuple())
        contact = Contact.from_api(
            {'created_at': now_ts, 'last_impression_at': now_ts})
        self.assertIsInstance(contact.created_at, datetime)
        eq_(now.strftime('%c'), contact.created_at.strftime('%c'))
        self.assertIsInstance(contact.last_impression_at, datetime)
        eq_(now.strftime('%c'), contact.last_impression_at.strftime('%c'))

    @istest
    def it_throws_an_attribute_error_on_trying_to_access_an_attribute_that_has_not_been_set(self):  # noqa
        with assert_raises(AttributeError):
            contact = Contact()
            contact.foo_property

    @istest
    def it_presents_a_complete_contact_record_correctly(self):
        contact = Contact.from_api(get_contact())
        eq_('id-from-customers-app', contact.external_id)
        eq_('bob@example.com', contact.email)
        eq_('Joe Schmoe', contact.name)
        eq_('the-app-id', contact.app_id)
        eq_(123, contact.session_count)
        eq_(1401970114, calendar.timegm(contact.created_at.utctimetuple()))
        eq_(1393613864, calendar.timegm(contact.remote_created_at.utctimetuple()))
        eq_(1401970114, calendar.timegm(contact.updated_at.utctimetuple()))

        Avatar = define_lightweight_class('avatar', 'Avatar')  # noqa
        Company = define_lightweight_class('company', 'Company')  # noqa
        SocialProfile = define_lightweight_class('social_profile', 'SocialProfile')  # noqa
        LocationData = define_lightweight_class('locaion_data', 'LocationData')  # noqa
        self.assertIsInstance(contact.avatar.__class__, Avatar.__class__)
        img_url = 'https://graph.facebook.com/1/picture?width=24&height=24'
        eq_(img_url, contact.avatar.image_url)

        self.assertIsInstance(contact.companies, list)
        eq_(1, len(contact.companies))
        self.assertIsInstance(contact.companies[0].__class__, Company.__class__)
        eq_('123', contact.companies[0].company_id)
        eq_('bbbbbbbbbbbbbbbbbbbbbbbb', contact.companies[0].id)
        eq_('the-app-id', contact.companies[0].app_id)
        eq_('Company 1', contact.companies[0].name)
        eq_(1390936440, calendar.timegm(
            contact.companies[0].remote_created_at.utctimetuple()))
        eq_(1401970114, calendar.timegm(
            contact.companies[0].created_at.utctimetuple()))
        eq_(1401970114, calendar.timegm(
            contact.companies[0].updated_at.utctimetuple()))
        eq_(1401970113, calendar.timegm(
            contact.companies[0].last_request_at.utctimetuple()))
        eq_(0, contact.companies[0].monthly_spend)
        eq_(0, contact.companies[0].session_count)
        eq_(1, contact.companies[0].user_count)
        eq_([], contact.companies[0].tag_ids)

        self.assertIsInstance(contact.custom_attributes, FlatStore)
        eq_('b', contact.custom_attributes["a"])
        eq_(2, contact.custom_attributes["b"])

        eq_(4, len(contact.social_profiles))
        twitter_account = contact.social_profiles[0]
        self.assertIsInstance(twitter_account.__class__, SocialProfile.__class__)
        eq_('twitter', twitter_account.name)
        eq_('abc', twitter_account.username)
        eq_('http://twitter.com/abc', twitter_account.url)

        self.assertIsInstance(contact.location_data.__class__, LocationData.__class__)
        eq_('Dublin', contact.location_data.city_name)
        eq_('EU', contact.location_data.continent_code)
        eq_('Ireland', contact.location_data.country_name)
        eq_('90', contact.location_data.latitude)
        eq_('10', contact.location_data.longitude)
        eq_('IRL', contact.location_data.country_code)

        ok_(contact.unsubscribed_from_emails)
        eq_("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", contact.user_agent_data)  # noqa

    @istest
    def it_allows_easy_setting_of_custom_data(self):
        now = datetime.utcnow()
        now_ts = calendar.timegm(now.utctimetuple())

        contact = Contact()
        contact.custom_attributes["mad"] = 123
        contact.custom_attributes["other"] = now_ts
        contact.custom_attributes["thing"] = "yay"
        attrs = {"mad": 123, "other": now_ts, "thing": "yay"}
        eq_(contact.to_dict()["custom_attributes"], attrs)

    @istest
    def it_allows_easy_setting_of_multiple_companies(self):
        contact = Contact()
        companies = [
            {"name": "Intercom", "company_id": "6"},
            {"name": "Test", "company_id": "9"},
        ]
        contact.companies = companies
        eq_(contact.to_dict()["companies"], companies)

    @istest
    def it_rejects_nested_data_structures_in_custom_attributes(self):
        contact = Contact()
        with assert_raises(ValueError):
            contact.custom_attributes["thing"] = [1]

        with assert_raises(ValueError):
            contact.custom_attributes["thing"] = {1: 2}

        with assert_raises(ValueError):
            contact.custom_attributes = {1: {2: 3}}

        contact = Contact.from_api(get_contact())
        with assert_raises(ValueError):
            contact.custom_attributes["thing"] = [1]

    @istest
    def it_fetches_a_contact(self):
        with patch.object(Client, 'get', return_value=get_contact()) as mock_method:  # noqa
            contact = self.client.contacts.find(email='somebody@example.com')
            eq_(contact.email, 'bob@example.com')
            eq_(contact.name, 'Joe Schmoe')
            mock_method.assert_called_once_with(
                '/contacts', {'email': 'somebody@example.com'})  # noqa

    @istest
    def it_gets_contacts_by_tag(self):
        with patch.object(Client, 'get', return_value=page_of_contacts(False)):
            contacts = self.client.contacts.by_tag(124)
            for contact in contacts:
                ok_(hasattr(contact, 'avatar'))

    @istest
    def it_saves_a_contact_always_sends_custom_attributes(self):

        body = {
            'email': 'jo@example.com',
            'external_id': 'i-1224242',
            'custom_attributes': {}
        }

        with patch.object(Client, 'post', return_value=body) as mock_method:
            contact = Contact(email="jo@example.com", external_id="i-1224242")
            self.client.contacts.save(contact)
            eq_(contact.email, 'jo@example.com')
            eq_(contact.custom_attributes, {})
            mock_method.assert_called_once_with(
                '/contacts',
                {'email': "jo@example.com", 'external_id': "i-1224242",
                 'custom_attributes': {}})

    @istest
    def it_saves_a_contact_with_a_company(self):
        body = {
            'email': 'jo@example.com',
            'external_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        }
        with patch.object(Client, 'post', return_value=body) as mock_method:
            contact = Contact(
                email="jo@example.com", external_id="i-1224242",
                company={'company_id': 6, 'name': 'Intercom'})
            self.client.contacts.save(contact)
            eq_(contact.email, 'jo@example.com')
            eq_(len(contact.companies), 1)
            mock_method.assert_called_once_with(
                '/contacts',
                {
                    'email': "jo@example.com",
                    'external_id': "i-1224242",
                    'company': {'company_id': 6, 'name': 'Intercom'},
                    'custom_attributes': {}
                }
            )

    @istest
    def it_saves_a_contact_with_companies(self):
        body = {
            'email': 'jo@example.com',
            'external_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        }
        with patch.object(Client, 'post', return_value=body) as mock_method:
            contact = Contact(
                email="jo@example.com", external_id="i-1224242",
                companies=[{'company_id': 6, 'name': 'Intercom'}])
            self.client.contacts.save(contact)
            eq_(contact.email, 'jo@example.com')
            eq_(len(contact.companies), 1)
            mock_method.assert_called_once_with(
                '/contacts',
                {'email': "jo@example.com", 'external_id': "i-1224242",
                 'companies': [{'company_id': 6, 'name': 'Intercom'}],
                 'custom_attributes': {}})

    @istest
    def it_can_save_a_contact_with_a_none_email(self):
        contact = Contact(
            email=None, external_id="i-1224242",
            companies=[{'company_id': 6, 'name': 'Intercom'}])
        body = {
            'custom_attributes': {},
            'email': None,
            'external_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        }
        with patch.object(Client, 'post', return_value=body) as mock_method:
            self.client.contacts.save(contact)
            ok_(contact.email is None)
            eq_(contact.external_id, 'i-1224242')
            mock_method.assert_called_once_with(
                '/contacts',
                {'email': None, 'external_id': "i-1224242",
                 'companies': [{'company_id': 6, 'name': 'Intercom'}],
                 'custom_attributes': {}})

    @istest
    def it_deletes_a_contact(self):
        contact = Contact(id="1")
        with patch.object(Client, 'delete', return_value={}) as mock_method:
            contact = self.client.contacts.delete(contact)
            eq_(contact.id, "1")
            mock_method.assert_called_once_with('/contacts/1', {})

    @istest
    def it_can_use_contact_create_for_convenience(self):
        payload = {
            'email': 'jo@example.com',
            'external_id': 'i-1224242',
            'custom_attributes': {}
        }
        with patch.object(Client, 'post', return_value=payload) as mock_method:  # noqa
            contact = self.client.contacts.create(email="jo@example.com", external_id="i-1224242")  # noqa
            eq_(payload, contact.to_dict())
            mock_method.assert_called_once_with(
                '/contacts/', {'email': "jo@example.com", 'external_id': "i-1224242"})  # noqa

    @istest
    def it_updates_the_contact_with_attributes_set_by_the_server(self):
        payload = {
            'email': 'jo@example.com',
            'external_id': 'i-1224242',
            'custom_attributes': {},
            'session_count': 4
        }
        with patch.object(Client, 'post', return_value=payload) as mock_method:  # noqa
            contact = self.client.contacts.create(email="jo@example.com", external_id="i-1224242")  # noqa
            eq_(payload, contact.to_dict())
            mock_method.assert_called_once_with(
                '/contacts/',
                {'email': "jo@example.com", 'external_id': "i-1224242"})  # noqa

    @istest
    def it_allows_setting_dates_to_none_without_converting_them_to_0(self):
        payload = {
            'email': 'jo@example.com',
            'custom_attributes': {},
            'remote_created_at': None
        }
        with patch.object(Client, 'post', return_value=payload) as mock_method:
            contact = self.client.contacts.create(email="jo@example.com", remote_created_at=None)  # noqa
            ok_(contact.remote_created_at is None)
            mock_method.assert_called_once_with('/contacts/', {'email': "jo@example.com", 'remote_created_at': None})  # noqa

    @istest
    def it_gets_sets_rw_keys(self):
        created_at = datetime.utcnow()
        payload = {
            'email': 'me@example.com',
            'external_id': 'abc123',
            'name': 'Bob Smith',
            'last_seen_ip': '1.2.3.4',
            'last_seen_contact_agent': 'ie6',
            'created_at': calendar.timegm(created_at.utctimetuple())
        }
        contact = Contact(**payload)
        expected_keys = ['custom_attributes']
        expected_keys.extend(list(payload.keys()))
        eq_(sorted(expected_keys), sorted(contact.to_dict().keys()))
        for key in list(payload.keys()):
            eq_(payload[key], contact.to_dict()[key])

    @istest
    def it_will_allow_extra_attributes_in_response_from_api(self):
        contact = Contact.from_api({'new_param': 'some value'})
        eq_('some value', contact.new_param)

    @istest
    def it_returns_a_collectionproxy_for_all_without_making_any_requests(self):
        with mock.patch('intercom.request.Request.send_request_to_path', new_callable=mock.NonCallableMock):  # noqa
            res = self.client.contacts.all()
            self.assertIsInstance(res, CollectionProxy)

    @istest
    def it_raises_a_multiple_matching_contacts_error_when_receiving_a_conflict(self):  # noqa
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'code': 'conflict',
                    'message': 'Multiple existing contacts match this email address - must be more specific using external_id'  # noqa
                }
            ]
        }
        # create bytes content
        content = json.dumps(payload).encode('utf-8')
        # create mock response
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(MultipleMatchingContactsError):
                self.client.get('/contacts', {})

    @istest
    def it_handles_accented_characters(self):
        # create a contact dict with a name that contains accented characters
        payload = get_contact(name='Jóe Schmö')
        # create bytes content
        content = json.dumps(payload).encode('utf-8')
        # create mock response
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            contact = self.client.contacts.find(email='bob@example.com')
            eq_('Jóe Schmö', contact.name)


class DescribeIncrementingCustomAttributeFields(unittest.TestCase):

    def setUp(self):  # noqa
        self.client = Client()

        created_at = datetime.utcnow()
        params = {
            'email': 'jo@example.com',
            'external_id': 'i-1224242',
            'custom_attributes': {
                'mad': 123,
                'another': 432,
                'other': time.mktime(created_at.timetuple()),
                'thing': 'yay',
                'logins': None,
            }
        }
        self.contact = Contact(**params)

    @istest
    def it_increments_up_by_1_with_no_args(self):
        self.contact.increment('mad')
        eq_(self.contact.to_dict()['custom_attributes']['mad'], 124)

    @istest
    def it_increments_up_by_given_value(self):
        self.contact.increment('mad', 4)
        eq_(self.contact.to_dict()['custom_attributes']['mad'], 127)

    @istest
    def it_increments_down_by_given_value(self):
        self.contact.increment('mad', -1)
        eq_(self.contact.to_dict()['custom_attributes']['mad'], 122)

    @istest
    def it_can_increment_new_custom_data_fields(self):
        self.contact.increment('new_field', 3)
        eq_(self.contact.to_dict()['custom_attributes']['new_field'], 3)

    @istest
    def it_can_increment_none_values(self):
        self.contact.increment('logins')
        eq_(self.contact.to_dict()['custom_attributes']['logins'], 1)

    @istest
    def it_can_call_increment_on_the_same_key_twice_and_increment_by_2(self):  # noqa
        self.contact.increment('mad')
        self.contact.increment('mad')
        eq_(self.contact.to_dict()['custom_attributes']['mad'], 125)

    @istest
    def it_can_save_after_increment(self):  # noqa
        contact = Contact(
            email=None, external_id="i-1224242",
            companies=[{'company_id': 6, 'name': 'Intercom'}])
        body = {
            'custom_attributes': {},
            'email': "",
            'external_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        }
        with patch.object(Client, 'post', return_value=body) as mock_method:  # noqa
            contact.increment('mad')
            eq_(contact.to_dict()['custom_attributes']['mad'], 1)
            self.client.contacts.save(contact)


class DescribeBulkOperations(unittest.TestCase):  # noqa

    def setUp(self):  # noqa
        self.client = Client()

        self.job = {
            "app_id": "app_id",
            "id": "super_awesome_job",
            "created_at": 1446033421,
            "completed_at": 1446048736,
            "closing_at": 1446034321,
            "updated_at": 1446048736,
            "name": "api_bulk_job",
            "state": "completed",
            "links": {
                "error": "https://api.intercom.io/jobs/super_awesome_job/error",
                "self": "https://api.intercom.io/jobs/super_awesome_job"
            },
            "tasks": [
                {
                    "id": "super_awesome_task",
                    "item_count": 2,
                    "created_at": 1446033421,
                    "started_at": 1446033709,
                    "completed_at": 1446033709,
                    "state": "completed"
                }
            ]
        }

        self.bulk_request = {
            "items": [
                {
                    "method": "post",
                    "data_type": "contact",
                    "data": {
                        "external_id": 25,
                        "email": "alice@example.com"
                    }
                },
                {
                    "method": "delete",
                    "data_type": "contact",
                    "data": {
                        "external_id": 26,
                        "email": "bob@example.com"
                    }
                }
            ]
        }

        self.contacts_to_create = [
            {
                "external_id": 25,
                "email": "alice@example.com"
            }
        ]

        self.contacts_to_delete = [
            {
                "external_id": 26,
                "email": "bob@example.com"
            }
        ]

        created_at = datetime.utcnow()
        params = {
            'email': 'jo@example.com',
            'external_id': 'i-1224242',
            'custom_attributes': {
                'mad': 123,
                'another': 432,
                'other': time.mktime(created_at.timetuple()),
                'thing': 'yay'
            }
        }
        self.contact = Contact(**params)

    @istest
    def it_submits_a_bulk_job(self):  # noqa
        with patch.object(Client, 'post', return_value=self.job) as mock_method:  # noqa
            self.client.contacts.submit_bulk_job(
                create_items=self.contacts_to_create, delete_items=self.contacts_to_delete)
            mock_method.assert_called_once_with('/bulk/contacts', self.bulk_request)

    @istest
    def it_adds_contacts_to_an_existing_bulk_job(self):  # noqa
        self.bulk_request['job'] = {'id': 'super_awesome_job'}
        with patch.object(Client, 'post', return_value=self.job) as mock_method:  # noqa
            self.client.contacts.submit_bulk_job(
                create_items=self.contacts_to_create, delete_items=self.contacts_to_delete,
                job_id='super_awesome_job')
            mock_method.assert_called_once_with('/bulk/contacts', self.bulk_request)
