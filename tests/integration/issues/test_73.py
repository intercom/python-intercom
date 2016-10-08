# -*- coding: utf-8 -*-
"""
How do I record when a User has started a new session?
"""

import os
import unittest

from intercom.client import Client

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class Issue73Test(unittest.TestCase):

    def test(self):
        user = intercom.users.create(email='bingo@example.com')
        # store current session count
        session_count = user.session_count

        # register a new session
        user.new_session = True
        intercom.users.save(user)

        # count has increased by 1
        self.assertEquals(session_count + 1, user.session_count)

        # register a new session
        user.new_session = True
        intercom.users.save(user)

        # count has increased by 1
        self.assertEquals(session_count + 2, user.session_count)
