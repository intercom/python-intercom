# -*- coding: utf-8 -*-

import os
import time
import unittest
from datetime import datetime
from intercom import Intercom
from intercom import Segment

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class SegmentTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.segment = Segment.all()[0]

    def test_find_segment(self):
        # Find a segment
        segment = Segment.find(id=self.segment.id)
        self.assertEqual(segment.id, self.segment.id)

    def test_save_segment(self):
        # Update a segment
        segment = Segment.find(id=self.segment.id)
        now = datetime.utcnow()
        updated_name = 'Updated %s' % (time.mktime(now.timetuple()))
        segment.name = updated_name
        segment.save()
        segment = Segment.find(id=self.segment.id)
        self.assertEqual(segment.name, updated_name)

    def test_iterate(self):
        # Iterate over all segments
        for segment in Segment.all():
            self.assertTrue(segment.id is not None)
