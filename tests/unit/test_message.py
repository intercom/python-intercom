# -*- coding: utf-8 -*-

import time
import unittest

from datetime import datetime
from intercom import Intercom
from intercom import User
from intercom import Message
from mock import patch
from nose.tools import eq_
from nose.tools import istest


class MessageTest(unittest.TestCase):

    def setUp(self):  # noqa
        now = time.mktime(datetime.utcnow().timetuple())
        self.user = User(
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
        with patch.object(Intercom, 'post', return_value=data) as mock_method:
            message = Message.create(**data)
            mock_method.assert_called_once_with('/messages/', **data)
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

        with patch.object(Intercom, 'post', return_value=data) as mock_method:
            message = Message.create(**data)
            mock_method.assert_called_once_with('/messages/', **data)
            eq_('halp', message.body)
            eq_('inapp', message.message_type)
