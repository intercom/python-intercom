# -*- coding: utf-8 -*-

import intercom
import unittest

from intercom import Company
from intercom import Intercom
from mock import call
from mock import patch
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import istest


class CompanyTest(unittest.TestCase):

    @istest
    def it_raises_error_if_no_response_on_find(self):
        with patch.object(Intercom, 'get', return_value=None) as mock_method:
            with assert_raises(intercom.HttpError):
                Company.find(company_id='4')
            mock_method.assert_called_once_with('/companies', company_id='4')

    @istest
    def it_raises_error_if_no_response_on_find_all(self):
        with patch.object(Intercom, 'get', return_value=None) as mock_method:
            with assert_raises(intercom.HttpError):
                [x for x in Company.all()]
            mock_method.assert_called_once_with('/companies')

    @istest
    def it_raises_error_on_load(self):
        data = {
            'type': 'user',
            'id': 'aaaaaaaaaaaaaaaaaaaaaaaa',
            'company_id': '4',
            'name': 'MyCo'
        }
        side_effect = [data, None]
        with patch.object(Intercom, 'get', side_effect=side_effect) as mock_method:  # noqa
            company = Company.find(company_id='4')
            with assert_raises(intercom.HttpError):
                company.load()
            eq_([call('/companies', company_id='4'), call('/companies/aaaaaaaaaaaaaaaaaaaaaaaa')],  # noqa
                mock_method.mock_calls)
