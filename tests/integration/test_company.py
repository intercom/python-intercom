# -*- coding: utf-8 -*-

import os
import unittest
from intercom import Company
from intercom import Intercom
from intercom import User
from . import delete
from . import get_or_create_user
from . import get_or_create_company
from . import get_timestamp

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class CompanyTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        nowstamp = get_timestamp()
        cls.company = get_or_create_company(nowstamp)
        cls.user = get_or_create_user(nowstamp)

    @classmethod
    def teardown_class(cls):
        delete(cls.company)
        delete(cls.user)

    def test_add_user(self):
        user = User.find(email=self.user.email)
        user.companies = [
            {"company_id": 6, "name": "Intercom"},
            {"company_id": 9, "name": "Test Company"}
        ]
        user.save()
        user = User.find(email=self.user.email)
        self.assertEqual(len(user.companies), 2)
        self.assertEqual(user.companies[0].company_id, "9")

    def test_add_user_custom_attributes(self):
        user = User.find(email=self.user.email)
        user.companies = [
            {
                "id": 6,
                "name": "Intercom",
                "custom_attributes": {
                    "referral_source": "Google"
                }
            }
        ]
        user.save()
        user = User.find(email=self.user.email)
        self.assertEqual(len(user.companies), 2)
        self.assertEqual(user.companies[0].company_id, "9")

        # check the custom attributes
        company = Company.find(company_id=6)
        self.assertEqual(
            company.custom_attributes['referral_source'], "Google")

    def test_find_by_company_id(self):
        # Find a company by company_id
        company = Company.find(company_id=self.company.company_id)
        self.assertEqual(company.company_id, self.company.company_id)

    def test_find_by_company_name(self):
        # Find a company by name
        company = Company.find(name=self.company.name)
        self.assertEqual(company.name, self.company.name)

    def test_find_by_id(self):
        # Find a company by _id
        company = Company.find(id=self.company.id)
        self.assertEqual(company.company_id, self.company.company_id)

    def test_update(self):
        # Find a company by id
        company = Company.find(id=self.company.id)
        # Update a company
        now = get_timestamp()
        updated_name = 'Company %s' % (now)
        company.name = updated_name
        company.save()
        company = Company.find(id=self.company.id)
        self.assertEqual(company.name, updated_name)

    def test_iterate(self):
        # Iterate over all companies
        for company in Company.all():
            self.assertTrue(company.id is not None)

    def test_users(self):
        company = Company.find(id=self.company.id)
        # Get a list of users in a company
        for user in company.users:
            self.assertIsNotNone(user.email)
