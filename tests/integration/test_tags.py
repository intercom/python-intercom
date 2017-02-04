# -*- coding: utf-8 -*-

import os
import unittest
from intercom.client import Client
from . import delete_user
from . import delete_company
from . import get_or_create_company
from . import get_or_create_user
from . import get_timestamp

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class TagTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        nowstamp = get_timestamp()
        cls.company = get_or_create_company(intercom, nowstamp)
        cls.user = get_or_create_user(intercom, nowstamp)
        cls.user.companies = [
            {"company_id": cls.company.id, "name": cls.company.name}
        ]
        intercom.users.save(cls.user)

    @classmethod
    def teardown_class(cls):
        delete_company(intercom, cls.company)
        delete_user(intercom, cls.user)

    def test_tag_users(self):
        # Tag users
        tag = intercom.tags.tag(name='blue', users=[{'id': self.user.id}])
        self.assertEqual(tag.name, 'blue')
        user = intercom.users.find(email=self.user.email)
        self.assertEqual(1, len(user.tags))

    def test_untag_users(self):
        # Untag users
        tag = intercom.tags.untag(name='blue', users=[{'id': self.user.id}])
        self.assertEqual(tag.name, 'blue')
        user = intercom.users.find(email=self.user.email)
        self.assertEqual(0, len(user.tags))

    def test_all(self):
        # Iterate over all tags
        for tag in intercom.tags.all():
            self.assertIsNotNone(tag.id)

    def test_tag_companies(self):
        # Tag companies
        tag = intercom.tags.tag(
            name="blue", companies=[{'id': self.user.companies[0].id}])
        self.assertEqual(tag.name, "blue")
        company = intercom.companies.find(id=self.user.companies[0].id)
        self.assertEqual(1, len(company.tags))

    def test_untag_companies(self):
        # Untag companies
        tag = intercom.tags.untag(
            name="blue", companies=[{'id': self.user.companies[0].id}])
        self.assertEqual(tag.name, "blue")
        company = intercom.companies.find(id=self.user.companies[0].id)
        self.assertEqual(0, len(company.tags))
