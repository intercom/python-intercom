# -*- coding: utf-8 -*-

import os
import unittest
from intercom import Intercom
from intercom import Tag
from intercom import User
from intercom import Company
from . import delete
from . import get_or_create_company
from . import get_or_create_user
from . import get_timestamp

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class TagTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        nowstamp = get_timestamp()
        cls.company = get_or_create_company(nowstamp)
        cls.user = get_or_create_user(nowstamp)
        cls.user.companies = [
            {"company_id": cls.company.id, "name": cls.company.name}
        ]
        cls.user.save()

    @classmethod
    def teardown_class(cls):
        delete(cls.company)
        delete(cls.user)

    def test_tag_users(self):
        # Tag users
        tag = Tag.tag_users('blue', [self.user.id])
        self.assertEqual(tag.name, 'blue')
        user = User.find(email=self.user.email)
        self.assertEqual(1, len(user.tags))

    def test_untag_users(self):
        # Untag users
        tag = Tag.untag_users('blue', [self.user.id])
        self.assertEqual(tag.name, 'blue')
        user = User.find(email=self.user.email)
        self.assertEqual(0, len(user.tags))

    def test_all(self):
        # Iterate over all tags
        for tag in Tag.all():
            self.assertIsNotNone(tag.id)

    def test_all_for_user_by_id(self):
        # Iterate over all tags for user
        tags = Tag.find_all_for_user(id=self.user.id)
        for tag in tags:
            self.assertIsNotNone(tag.id)

    def test_all_for_user_by_email(self):
        # Iterate over all tags for user
        tags = Tag.find_all_for_user(email=self.user.email)
        for tag in tags:
            self.assertIsNotNone(tag.id)

    def test_all_for_user_by_user_id(self):
        # Iterate over all tags for user
        tags = Tag.find_all_for_user(user_id=self.user.user_id)
        for tag in tags:
            self.assertIsNotNone(tag.id)

    def test_tag_companies(self):
        # Tag companies
        tag = Tag.tag_companies("red", [self.user.companies[0].id])
        self.assertEqual(tag.name, "red")
        company = Company.find(id=self.user.companies[0].id)
        self.assertEqual(1, len(company.tags))

    def test_untag_companies(self):
        # Untag companies
        tag = Tag.untag_companies("red", [self.user.companies[0].id])
        self.assertEqual(tag.name, "red")
        company = Company.find(id=self.user.companies[0].id)
        self.assertEqual(0, len(company.tags))

    # Iterate over all tags for company
    def test_all_for_company_by_id(self):
        # Iterate over all tags for user
        red_tag = Tag.tag_companies("red", [self.company.id])
        tags = Tag.find_all_for_company(id=self.company.id)
        for tag in tags:
            self.assertEqual(red_tag.id, tag.id)
        Tag.untag_companies("red", [self.company.id])

    def test_all_for_company_by_company_id(self):
        # Iterate over all tags for user
        red_tag = Tag.tag_companies("red", [self.company.id])
        tags = Tag.find_all_for_company(company_id=self.company.id)
        for tag in tags:
            self.assertEqual(red_tag.id, tag.id)
        Tag.untag_companies("red", [self.company.id])
