# -*- coding: utf-8 -*-
"""Integration test for Intercom Counts."""

import os
import unittest
from intercom.client import Client
from nose.tools import eq_
from nose.tools import ok_
from . import delete_company
from . import delete_user
from . import get_timestamp
from . import get_or_create_company
from . import get_or_create_user

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class CountTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        nowstamp = get_timestamp()
        cls.company = get_or_create_company(intercom, nowstamp)
        cls.user = get_or_create_user(intercom, nowstamp)

    @classmethod
    def teardown_class(cls):
        delete_company(intercom, cls.company)
        delete_user(intercom, cls.user)

    def test_user_counts_for_each_tag(self):
        # Get User Tag Count Object
        intercom.tags.tag(name='blue', users=[{'id': self.user.id}])
        counts = intercom.counts.for_type(type='user', count='tag')
        intercom.tags.untag(name='blue', users=[{'id': self.user.id}])
        for count in counts.user['tag']:
            if 'blue' in count:
                eq_(count['blue'], 1)

    def test_user_counts_for_each_segment(self):
        # Get User Segment Count Object
        counts = intercom.counts.for_type(type='user', count='segment')
        ok_(counts)

    def test_company_counts_for_each_segment(self):
        # Get Company Segment Count Object
        counts = intercom.counts.for_type(type='company', count='segment')
        ok_(counts)

    def test_company_counts_for_each_tag(self):
        # Get Company Tag Count Object
        intercom.tags.tag(name='blue', companies=[{'id': self.company.id}])
        intercom.counts.for_type(type='company', count='tag')
        intercom.tags.untag(name='blue', companies=[{'id': self.company.id}])

    def test_company_counts_for_each_user(self):
        # Get Company User Count Object
        self.user.companies = [
            {"company_id": self.company.company_id}
        ]
        intercom.users.save(self.user)
        counts = intercom.counts.for_type(type='company', count='user')
        for count in counts.company['user']:
            if self.company.name in count:
                eq_(count[self.company.name], 1)

    def test_global(self):
        counts = intercom.counts.for_app()
        ok_(counts.company >= 0)
        ok_(counts.tag >= 0)
        ok_(counts.segment >= 0)
        ok_(counts.user >= 0)
        ok_(counts.lead >= 0)
