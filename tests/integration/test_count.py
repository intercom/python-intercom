# -*- coding: utf-8 -*-

import os
import unittest
from intercom import Intercom
from intercom import Company
from intercom import Count
from intercom import Segment
from intercom import Tag
from intercom import User
from nose.tools import eq_
from nose.tools import ok_
from . import get_timestamp
from . import get_or_create_company
from . import get_or_create_user
from . import delete

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class CountTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        nowstamp = get_timestamp()
        cls.company = get_or_create_company(nowstamp)
        cls.user = get_or_create_user(nowstamp)

    @classmethod
    def teardown_class(cls):
        delete(cls.company)
        delete(cls.user)
        print(Intercom.rate_limit_details)

    def test_user_counts_for_each_tag(self):
        # Get User Tag Count Object
        Tag.tag_users('blue', [self.user.id])
        counts = Count.user_counts_for_each_tag
        Tag.untag_users('blue', [self.user.id])
        for count in counts:
            if 'blue' in count:
                eq_(count['blue'], 1)

    def test_user_counts_for_each_segment(self):
        # Get User Segment Count Object
        counts = Count.user_counts_for_each_segment
        ok_(counts)

    def test_company_counts_for_each_segment(self):
        # Get Company Segment Count Object
        counts = Count.company_counts_for_each_segment
        ok_(counts)

    def test_company_counts_for_each_tag(self):
        # Get Company Tag Count Object
        Tag.tag_companies('blue', [self.company.id])
        counts = Count.company_counts_for_each_tag
        Tag.untag_companies('blue', [self.company.id])
        # for count in counts:
        #     if 'blue' in count:
        #         eq_(count['blue'], 1)

    def test_company_counts_for_each_user(self):
        # Get Company User Count Object
        self.user.companies = [
            {"company_id": self.company.company_id}
        ]
        self.user.save()
        counts = Count.company_counts_for_each_user
        for count in counts:
            if self.company.name in count:
                eq_(count[self.company.name], 1)

    def test_total_company_count(self):
        ok_(Company.count() >= 0)

    def test_total_user_count(self):
        ok_(User.count() >= 0)

    def test_total_segment_count(self):
        ok_(Segment.count() >= 0)

    def test_total_tag_count(self):
        ok_(Tag.count() >= 0)
