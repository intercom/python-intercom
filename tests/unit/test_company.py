# -*- coding: utf-8 -*-

import httpretty
import json
import re
import intercom
import unittest

from intercom import Company
from nose.tools import assert_raises
from nose.tools import istest

get = httpretty.GET
r = re.compile


class CompanyTest(unittest.TestCase):

    @istest
    @httpretty.activate
    def it_raises_error_if_no_response_on_find(self):
        httpretty.register_uri(
            get, r(r'/companies$'), body=None, status=200)
        with assert_raises(intercom.HttpError):
            Company.find(company_id='4')

    @istest
    @httpretty.activate
    def it_raises_error_if_no_response_on_find_all(self):
        httpretty.register_uri(
            get, r(r'/companies$'), body=None, status=200)
        with assert_raises(intercom.HttpError):
            [x for x in Company.all()]

    @istest
    @httpretty.activate
    def it_raises_error_on_load(self):
        data = {
            'type': 'user',
            'id': 'aaaaaaaaaaaaaaaaaaaaaaaa',
            'company_id': '4',
            'name': 'MyCo'
        }
        httpretty.register_uri(
            get, r(r'/companies$'), body=json.dumps(data), status=200)
        company = Company.find(company_id='4')
        httpretty.register_uri(
            get, r(r'/companies/aaaaaaaaaaaaaaaaaaaaaaaa$'), body=None, status=200)  # noqa
        with assert_raises(intercom.HttpError):
            company.load()
