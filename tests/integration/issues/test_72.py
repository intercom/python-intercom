# -*- coding: utf-8 -*-

import os
import unittest
import time

from intercom.client import Client

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class Issue72Test(unittest.TestCase):

    def test(self):
        intercom.users.create(email='me@example.com')
        # no exception here as empty response expected
        data = {
            'event_name': 'Eventful 1',
            'created_at': int(time.time()),
            'email': 'me@example.com'
        }
        intercom.events.create(**data)
