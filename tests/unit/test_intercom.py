# -*- coding: utf-8 -*-

import intercom
import mock
import time
import unittest

from datetime import datetime
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import istest


class ExpectingArgumentsTest(unittest.TestCase):

    def setUp(self):  # noqa
        self.intercom = intercom.Intercom
        self.intercom.app_id = 'abc123'
        self.intercom.app_api_key = 'super-secret-key'

    @istest
    def it_raises_argumenterror_if_no_app_id_or_app_api_key_specified(self):  # noqa
        self.intercom.app_id = None
        self.intercom.app_api_key = None
        with assert_raises(intercom.ArgumentError):
            self.intercom.target_base_url

    @istest
    def it_returns_the_app_id_and_app_api_key_previously_set(self):
        eq_(self.intercom.app_id, 'abc123')
        eq_(self.intercom.app_api_key, 'super-secret-key')

    @istest
    def it_defaults_to_https_to_api_intercom_io(self):
        eq_(self.intercom.target_base_url,
            'https://abc123:super-secret-key@api.intercom.io')


class OverridingProtocolHostnameTest(unittest.TestCase):
    def setUp(self):  # noqa
        self.intercom = intercom.Intercom
        self.protocol = self.intercom.protocol
        self.hostname = self.intercom.hostname
        self.intercom.endpoints = None

    def tearDown(self):  # noqa
        self.intercom.protocol = self.protocol
        self.intercom.hostname = self.hostname
        self.intercom.endpoints = ["https://api.intercom.io"]

    @istest
    def it_allows_overriding_of_the_endpoint_and_protocol(self):
        self.intercom.protocol = "http"
        self.intercom.hostname = "localhost:3000"
        eq_(
            self.intercom.target_base_url,
            "http://abc123:super-secret-key@localhost:3000")

    @istest
    def it_prefers_endpoints(self):
        self.intercom.endpoint = "https://localhost:7654"
        eq_(self.intercom.target_base_url,
            "https://abc123:super-secret-key@localhost:7654")

        # turn off the shuffle
        with mock.patch("random.shuffle") as mock_shuffle:
            mock_shuffle.return_value = ["http://example.com", "https://localhost:7654"]  # noqa
            self.intercom.endpoints = ["http://example.com", "https://localhost:7654"]  # noqa
            eq_(self.intercom.target_base_url,
                'http://abc123:super-secret-key@example.com')

    @istest
    def it_has_endpoints(self):
        eq_(self.intercom.endpoints, ["https://api.intercom.io"])
        self.intercom.endpoints = ["http://example.com", "https://localhost:7654"]  # noqa
        eq_(self.intercom.endpoints, ["http://example.com", "https://localhost:7654"])  # noqa

    @istest
    def it_should_randomize_endpoints_if_last_checked_endpoint_is_gt_5_minutes_ago(self):  # noqa
        now = time.mktime(datetime.utcnow().timetuple())
        self.intercom._endpoint_randomized_at = now
        self.intercom.endpoints = ["http://alternative"]
        self.intercom.current_endpoint = "http://start"

        self.intercom._endpoint_randomized_at = now - 120
        eq_(self.intercom.current_endpoint, "http://start")
        self.intercom._endpoint_randomized_at = now - 360
        eq_(self.intercom.current_endpoint, "http://alternative")
