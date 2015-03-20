# -*- coding: utf-8 -*-

import httpretty
import json
import re
import time
from datetime import datetime
from describe import expect
from intercom import User
from intercom import Event

post = httpretty.POST
r = re.compile


class DescribeIntercomEvent:

    def before_each(self, context):
        now = time.mktime(datetime.utcnow().timetuple())
        self.user = User(
            email="jim@example.com",
            user_id="12345",
            created_at=now,
            name="Jim Bob")
        self.created_time = now - 300

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

        expect('Eventful 1') == event.event_name
        expect(event).to.have_attr('metadata')
        expect('pi@example.com') == event.metadata['invitee_email']

    @httpretty.activate
    def it_creates_an_event_without_metadata(self):
        data = {
            'event_name': 'sale of item',
            'email': 'joe@example.com',
        }
        httpretty.register_uri(
            post, r(r'/events/$'), body=json.dumps(data), status=202)
        event = Event.create(**data)

        expect('sale of item') == event.event_name
        expect(event).to_not.have_attr('metadata')
