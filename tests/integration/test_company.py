# -*- coding: utf-8 -*-

import os
import unittest
from intercom.client import Client
from . import delete_company
from . import delete_user
from . import get_or_create_user
from . import get_or_create_company
from . import get_timestamp

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class CompanyTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        nowstamp = get_timestamp()
        cls.company = get_or_create_company(intercom, nowstamp)
        cls.user = get_or_create_user(intercom, nowstamp)

    @classmethod
    def teardown_class(cls):
        delete_company(intercom, cls.company)
        delete_user(intercom, cls.user)

    def test_add_user(self):
        user = intercom.users.find(email=self.user.email)
        user.companies = [
            {"company_id": 6, "name": "Intercom"},
            {"company_id": 9, "name": "Test Company"}
        ]
        intercom.users.save(user)
        user = intercom.users.find(email=self.user.email)
        self.assertEqual(len(user.companies), 2)
        self.assertEqual(user.companies[0].company_id, "9")

    def test_add_user_custom_attributes(self):
        user = intercom.users.find(email=self.user.email)
        user.companies = [
            {
                "id": 6,
                "name": "Intercom",
                "custom_attributes": {
                    "referral_source": "Google"
                }
            }
        ]
        intercom.users.save(user)
        user = intercom.users.find(email=self.user.email)
        self.assertEqual(len(user.companies), 2)
        self.assertEqual(user.companies[0].company_id, "9")

        # check the custom attributes
        company = intercom.companies.find(company_id=6)
        self.assertEqual(
            company.custom_attributes['referral_source'], "Google")

    def test_find_by_company_id(self):
        # Find a company by company_id
        company = intercom.companies.find(company_id=self.company.company_id)
        self.assertEqual(company.company_id, self.company.company_id)

    def test_find_by_company_name(self):
        # Find a company by name
        company = intercom.companies.find(name=self.company.name)
        self.assertEqual(company.name, self.company.name)

    def test_find_by_id(self):
        # Find a company by _id
        company = intercom.companies.find(id=self.company.id)
        self.assertEqual(company.company_id, self.company.company_id)

    def test_update(self):
        # Find a company by id
        company = intercom.companies.find(id=self.company.id)
        # Update a company
        now = get_timestamp()
        updated_name = 'Company %s' % (now)
        company.name = updated_name
        intercom.companies.save(company)
        company = intercom.companies.find(id=self.company.id)
        self.assertEqual(company.name, updated_name)

    def test_iterate(self):
        # Iterate over all companies
        for company in intercom.companies.all():
            self.assertTrue(company.id is not None)

    def test_users(self):
        company = intercom.companies.find(id=self.company.id)
        # Get a list of users in a company
        for user in intercom.companies.users(company.id):
            self.assertIsNotNone(user.email)
