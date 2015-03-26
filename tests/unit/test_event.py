# -*- coding: utf-8 -*-

import httpretty
import json
import re
import time
import unittest

from datetime import datetime
from intercom import User
from intercom import Event
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import istest

post = httpretty.POST
r = re.compile


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
    @httpretty.activate
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
        httpretty.register_uri(
            post, r(r'/events/$'), body=json.dumps(data), status=202)
        event = Event.create(**data)

        eq_('Eventful 1', event.event_name)
        ok_(hasattr(event, 'metadata'))
        eq_('pi@example.com', event.metadata['invitee_email'])

    @istest
    @httpretty.activate
    def it_creates_an_event_without_metadata(self):
        data = {
            'event_name': 'sale of item',
            'email': 'joe@example.com',
        }
        httpretty.register_uri(
            post, r(r'/events/$'), body=json.dumps(data), status=202)
        event = Event.create(**data)

        eq_('sale of item', event.event_name)
        ok_(not hasattr(event, 'metadata'))
