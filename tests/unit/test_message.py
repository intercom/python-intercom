# -*- coding: utf-8 -*-

import time
import unittest

from datetime import datetime
from intercom.client import Client
from intercom.contact import Contact
from mock import patch
from nose.tools import eq_
from nose.tools import istest


class MessageTest(unittest.TestCase):

    def setUp(self):  # noqa
        self.client = Client()
        now = time.mktime(datetime.utcnow().timetuple())
        self.user = Contact(
            email="jim@example.com",
            user_id="12345",
            created_at=now,
            name="Jim Bob")
        self.created_time = now - 300

    @istest
    def it_creates_a_user_message_with_string_keys(self):
        data = {
            'from': {
                'type': 'user',
                'email': 'jim@example.com',
            },
            'body': 'halp'
        }
        with patch.object(Client, 'post', return_value=data) as mock_method:
            message = self.client.messages.create(**data)
            mock_method.assert_called_once_with('/messages/', data)
            eq_('halp', message.body)

    @istest
    def it_creates_an_admin_message(self):
        data = {
            'from': {
                'type': 'admin',
                'id': '1234',
            },
            'to': {
                'type': 'user',
                'id': '5678',
            },
            'body': 'halp',
            'message_type': 'inapp'
        }

        with patch.object(Client, 'post', return_value=data) as mock_method:
            message = self.client.messages.create(**data)
            mock_method.assert_called_once_with('/messages/', data)
            eq_('halp', message.body)
            eq_('inapp', message.message_type)
