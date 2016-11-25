# -*- coding: utf-8 -*-

import mock
import time
import unittest

from datetime import datetime
from intercom import Intercom
from intercom import Contact
from mock import patch
from nose.tools import istest
from nose.tools import eq_
from nose.tools import ok_
from tests.unit import get_contact


class ContactTest(unittest.TestCase):
    """
    Contacts are so similar to users that we only perform some basic coverage
    """
    @istest
    def it_to_dict_itself(self):
        created_at = datetime.utcnow()
        contact = Contact(
            email="jim@example.com", user_id="12345",
            created_at=created_at, name="Jim Bob")
        as_dict = contact.to_dict
        eq_(as_dict["email"], "jim@example.com")
        ok_(as_dict["user_id"])
        eq_(as_dict["created_at"], time.mktime(created_at.timetuple()))
        eq_(as_dict["name"], "Jim Bob")

    @istest
    def it_allows_update_last_request_at(self):
        payload = {
            'user_id': '1224242',
            'update_last_request_at': True,
            'custom_attributes': {}
        }
        with patch.object(Intercom, 'post', return_value=payload) as mock_method:
            Contact.create(update_last_request_at=True)
            mock_method.assert_called_once_with(
                '/contacts/', update_last_request_at=True)

    @istest
    def it_fetches_a_contact(self):
        with patch.object(Intercom, 'get', return_value=get_contact()) as mock_method:  # noqa
            contact = Contact.find(email='somebody@example.com')
            eq_(contact.email, 'bob@example.com')
            eq_(contact.name, 'Joe Schmoe')
            mock_method.assert_called_once_with('/contacts', email='somebody@example.com')  # noqa

    @istest
    # @httpretty.activate
    def it_saves_a_contact_always_sends_custom_attributes(self):
        contact = Contact(email="jo@example.com")

        body = {
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'custom_attributes': {}
        }

        with patch.object(Intercom, 'post', return_value=body) as mock_method:
            contact.save()
            eq_(contact.email, 'jo@example.com')
            eq_(contact.custom_attributes, {})
            mock_method.assert_called_once_with(
                '/contacts',
                email="jo@example.com",
                custom_attributes={})

    @istest
    def it_can_save_a_contact_with_a_none_email(self):
        contact = Contact(
            email=None,
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
            contact.save()
            ok_(contact.email is None)
            eq_(contact.user_id, 'i-1224242')
            mock_method.assert_called_once_with(
                '/contacts',
                email=None,
                companies=[{'company_id': 6, 'name': 'Intercom'}],
                custom_attributes={})

    @istest
    def it_deletes_a_contact(self):
        contact = Contact(id="1")
        with patch.object(Intercom, 'delete', return_value={}) as mock_method:
            contact = contact.delete()
            eq_(contact.id, "1")
            mock_method.assert_called_once_with('/contacts/1/')

    @istest
    def it_returns_the_total_number_of_contacts(self):
        with mock.patch.object(Contact, 'count') as mock_count:
            mock_count.return_value = 100
            eq_(100, Contact.count())
