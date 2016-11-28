# -*- coding: utf-8 -*-  # noqa

import intercom
import unittest

from intercom.client import Client
from intercom.company import Company
from mock import call
from mock import patch
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import istest
from tests.unit import page_of_companies


class CompanyTest(unittest.TestCase):  # noqa

    def setUp(self):  # noqa
        self.client = Client()

    @istest
    def it_raises_error_if_no_response_on_find(self):  # noqa
        with patch.object(Client, 'get', return_value=None) as mock_method:
            with assert_raises(intercom.HttpError):
                self.client.companies.find(company_id='4')
            mock_method.assert_called_once_with('/companies', {'company_id': '4'})

    @istest
    def it_raises_error_if_no_response_on_find_all(self):  # noqa
        with patch.object(Client, 'get', return_value=None) as mock_method:
            with assert_raises(intercom.HttpError):
                [x for x in self.client.companies.all()]
            mock_method.assert_called_once_with('/companies', {})

    @istest
    def it_raises_error_on_load(self):  # noqa
        company = Company()
        company.id = '4'
        side_effect = [None]
        with patch.object(Client, 'get', side_effect=side_effect) as mock_method:
            with assert_raises(intercom.HttpError):
                self.client.companies.load(company)
            eq_([call('/companies/4', {})], mock_method.mock_calls)

    @istest
    def it_gets_companies_by_tag(self):  # noqa
        with patch.object(Client, 'get', return_value=page_of_companies(False)) as mock_method:
            companies = self.client.companies.by_tag(124)
            for company in companies:
                ok_(hasattr(company, 'company_id'))
            eq_([call('/companies?tag_id=124', {})], mock_method.mock_calls)
