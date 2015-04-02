# -*- coding: utf-8 -*-

import time
import unittest

from datetime import datetime
from intercom import User
from intercom import Intercom
from intercom import Event
from mock import patch
from nose.tools import istest


class EventTest(unittest.TestCase):

    def setUp(self):  # noqa
        now = time.mktime(datetime.utcnow().timetuple())
        self.user = User(
            email="jim@example.com",
            user_id="12345",
            created_at=now,
            name="Jim Bob")
        self.created_time = now - 300

    @istest
    def it_creates_an_event_with_metadata(self):
        data = {
            'event_name': 'Eventful 1',
            'created_at': self.created_time,
            'email': 'joe@example.com',
            'metadata': {
                'invitee_email': 'pi@example.com',
                'invite_code': 'ADDAFRIEND',
                'found_date': 12909364407
            }
        }

        with patch.object(Intercom, 'post', return_value=data) as mock_method:
            Event.create(**data)
            mock_method.assert_called_once_with('/events/', **data)

    @istest
    def it_creates_an_event_without_metadata(self):
        data = {
            'event_name': 'sale of item',
            'email': 'joe@example.com',
        }
        with patch.object(Intercom, 'post', return_value=data) as mock_method:
            Event.create(**data)
            mock_method.assert_called_once_with('/events/', **data)
