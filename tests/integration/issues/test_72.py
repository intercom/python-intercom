# -*- coding: utf-8 -*-

import os
import unittest
from intercom import Intercom
from intercom import User

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class Issue72Test(unittest.TestCase):

    def test(self):
        User.create(email='me@example.com')
