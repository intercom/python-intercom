# -*- coding: utf-8 -*-

import os
import unittest
from intercom import Intercom
from intercom import Admin

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class AdminTest(unittest.TestCase):

    def test(self):
        # Iterate over all admins
        for admin in Admin.all():
            self.assertIsNotNone(admin.id)
            self.assertIsNotNone(admin.email)
