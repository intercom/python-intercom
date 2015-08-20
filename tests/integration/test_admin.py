# -*- coding: utf-8 -*-

import os
import unittest
from intercom.client import Client

intercom = Client(
    os.environ.get('INTERCOM_APP_ID'),
    os.environ.get('INTERCOM_API_KEY'))


class AdminTest(unittest.TestCase):

    def test(self):
        # Iterate over all admins
        for admin in intercom.admins.all():
            self.assertIsNotNone(admin.id)
            self.assertIsNotNone(admin.email)
