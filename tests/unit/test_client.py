# -*- coding: utf-8 -*-  # noqa

import time
import unittest

from datetime import datetime
from datetime import timedelta
from intercom.client import Client
from intercom.request import Request
from mock import Mock
from mock import patch
from nose.tools import istest
from pytz import utc


class ClientTest(unittest.TestCase):  # noqa

    def setUp(self):  # noqa
        self.client = Client()
        now = datetime.utcnow().replace(tzinfo=utc)
        reset_at = now + timedelta(seconds=2)
        # set the reset to be in 2 seconds
        self.rate_limit_details = {
            'remaining': 0,
            'limit': 20,
            'reset_at': reset_at
        }
        headers = {
            'x-ratelimit-limit': 20,
            'x-ratelimit-remaining': 0,
            'x-ratelimit-reset': time.mktime(reset_at.timetuple())
        }
        payload = """{
            "user_id": "1224242",
            "update_last_request_at": true,
            "custom_attributes": {}
        }"""

        if not hasattr(payload, 'decode'):
            # python 3
            payload = payload.encode('utf-8')

        self.response = Mock(
            content=payload,
            encoding='utf-8',
            headers=headers)
        self.started_at = now

    @istest
    def it_can_control_throttle_on_creation(self):  # noqa
        client = Client()
        self.assertFalse(client.throttle)
        client = Client(throttle=True)
        self.assertTrue(client.throttle)

    @istest
    def it_will_sleep_if_throttle_is_on(self):  # noqa
        client = Client(throttle=True)
        client.rate_limit_details = self.rate_limit_details
        with patch.object(Request, 'send_request_to_path', return_value=self.response):
            # this call should take approximately 2 seconds
            client.users.find(email="john@example.com")
        finished_at = datetime.utcnow().replace(tzinfo=utc)
        self.assertEqual(2, int((finished_at - self.started_at).seconds))

    @istest
    def it_wont_sleep_if_throttle_is_off(self):  # noqa
        client = Client()
        client.rate_limit_details = self.rate_limit_details
        with patch.object(Request, 'send_request_to_path', return_value=self.response):
            # this call should take approximately 2 seconds
            client.users.find(email="john@example.com")
        finished_at = datetime.utcnow().replace(tzinfo=utc)
        self.assertEqual(0, int((finished_at - self.started_at).seconds))
