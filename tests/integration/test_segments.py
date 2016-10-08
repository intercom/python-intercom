# -*- coding: utf-8 -*-

import os
import unittest
from intercom.client import Client

intercom = Client(
    os.environ.get('INTERCOM_PERSONAL_ACCESS_TOKEN'))


class SegmentTest(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.segment = intercom.segments.all()[0]

    def test_find_segment(self):
        # Find a segment
        segment = intercom.segments.find(id=self.segment.id)
        self.assertEqual(segment.id, self.segment.id)

    def test_iterate(self):
        # Iterate over all segments
        for segment in intercom.segments.all():
            self.assertTrue(segment.id is not None)
