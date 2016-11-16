# -*- coding: utf-8 -*-

import os
import unittest
from intercom.client import Client
from . import get_timestamp
from . import get_or_create_user
from . import delete_user

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class UserTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        nowstamp = get_timestamp()
        cls.user = get_or_create_user(intercom, nowstamp)
        cls.email = cls.user.email

    @classmethod
    def teardown_class(cls):
        delete_user(intercom, cls.user)

    def test_find_by_email(self):
        # Find user by email
        user = intercom.users.find(email=self.email)
        self.assertEqual(self.email, user.email)

    def test_find_by_user_id(self):
        # Find user by user id
        user = intercom.users.find(user_id=self.user.user_id)
        self.assertEqual(self.email, user.email)

    def test_find_by_id(self):
        # Find user by id
        user = intercom.users.find(id=self.user.id)
        self.assertEqual(self.email, user.email)

    def test_custom_attributes(self):
        # Update custom_attributes for a user
        user = intercom.users.find(id=self.user.id)
        user.custom_attributes["average_monthly_spend"] = 1234.56
        intercom.users.save(user)
        user = intercom.users.find(id=self.user.id)
        self.assertEqual(
            user.custom_attributes["average_monthly_spend"], 1234.56)

    def test_increment(self):
        # Perform incrementing
        user = intercom.users.find(id=self.user.id)
        karma = user.custom_attributes.get('karma', 0)
        user.increment('karma')
        intercom.users.save(user)
        self.assertEqual(user.custom_attributes["karma"], karma + 1)
        user.increment('karma')
        intercom.users.save(user)
        self.assertEqual(user.custom_attributes["karma"], karma + 2)

    def test_iterate(self):
        # Iterate over all users
        for user in intercom.users.all():
            self.assertTrue(user.id is not None)
