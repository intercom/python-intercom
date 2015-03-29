# -*- coding: utf-8 -*-

import os
import unittest
from intercom import Intercom
from intercom import User
from . import get_timestamp
from . import get_or_create_user
from . import delete

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class UserTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        nowstamp = get_timestamp()
        cls.user = get_or_create_user(nowstamp)
        cls.email = cls.user.email

    @classmethod
    def teardown_class(cls):
        delete(cls.user)

    def test_find_by_email(self):
        # Find user by email
        user = User.find(email=self.email)
        self.assertEqual(self.email, user.email)

    def test_find_by_user_id(self):
        # Find user by user id
        user = User.find(user_id=self.user.user_id)
        self.assertEqual(self.email, user.email)

    def test_find_by_id(self):
        # Find user by id
        user = User.find(id=self.user.id)
        self.assertEqual(self.email, user.email)

    def test_custom_attributes(self):
        # Update custom_attributes for a user
        user = User.find(id=self.user.id)
        user.custom_attributes["average_monthly_spend"] = 1234.56
        user.save()
        user = User.find(id=self.user.id)
        self.assertEqual(
            user.custom_attributes["average_monthly_spend"], 1234.56)

    def test_increment(self):
        # Perform incrementing
        user = User.find(id=self.user.id)
        karma = user.custom_attributes.get('karma', 0)
        user.increment('karma')
        user.save()
        self.assertEqual(user.custom_attributes["karma"], karma + 1)
        user.increment('karma')
        user.save()
        self.assertEqual(user.custom_attributes["karma"], karma + 2)

    def test_iterate(self):
        # Iterate over all users
        for user in User.all():
            self.assertTrue(user.id is not None)
