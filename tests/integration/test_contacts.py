# -*- coding: utf-8 -*-

import os
import unittest
from intercom.client import Client
from . import get_timestamp
from . import get_or_create_contact

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class ContactsTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        nowstamp = get_timestamp()
        cls.user = get_or_create_contact(intercom, nowstamp)
        cls.email = cls.user.email

    @classmethod
    def teardown_class(cls):
        delete_user(intercom, cls.user)

    def test_find_by_email(self):
        # Find user by email
        contact = intercom.contacts.find(email=self.email)
        self.assertEqual(self.email, contact.email)
