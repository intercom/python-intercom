# -*- coding: utf-8 -*-

import os
import time
import unittest
from datetime import datetime
from intercom import Intercom
from intercom.segment import Segment

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class SegmentTest(unittest.TestCase):
    email = "ada@example.com"

    @classmethod
    def setup_class(cls):
        # get user
        cls.segment_id = "5425e77db351e072bb000017"

    def test_find_segment(self):
        # Find a segment
        segment = Segment.find(id=self.segment_id)
        self.assertEqual(segment.id, self.segment_id)

    def test_save_segment(self):
        # Update a segment
        segment = Segment.find(id=self.segment_id)
        now = datetime.utcnow()
        updated_name = 'Updated %s' % (time.mktime(now.timetuple()))
        segment.name = updated_name
        segment.save()
        segment = Segment.find(id=self.segment_id)
        self.assertEqual(segment.name, updated_name)

    def test_iterate(self):
        # Iterate over all segments
        for segment in Segment.all():
            self.assertTrue(segment.id is not None)


    # def test_tag_users(self):
    #     # Tag users
    #     tag = Tag.tag_users("blue", [self.user.id])
    #     self.assertEqual(tag.name, "blue")

    # def test_untag_users(self):
    #     # Untag users
    #     tag = Tag.untag_users("blue", [self.user.id])
    #     self.assertEqual(tag.name, "blue")

    # def test_all(self):
    #     # Iterate over all tags
    #     for tag in Tag.all():
    #         self.assertIsNotNone(tag.id)

    # # def test_all_for_user_by_id(self):
    # #     # Iterate over all tags for user
    # #     tags = Tag.find_all_for_user(id=self.user.id)
    # #     for tag in tags:
    # #         self.assertIsNotNone(tag.id)

    # # def test_all_for_user_by_email(self):
    # #     # Iterate over all tags for user
    # #     tags = Tag.find_all_for_user(email=self.user.email)
    # #     for tag in tags:
    # #         self.assertIsNotNone(tag.id)

    # # def test_all_for_user_by_user_id(self):
    # #     # Iterate over all tags for user
    # #     tags = Tag.find_all_for_user(user_id=self.user.user_id)
    # #     for tag in tags:
    # #         self.assertIsNotNone(tag.id)

    # def test_tag_companies(self):
    #     # Tag companies
    #     tag = Tag.tag_companies("red", [self.user.companies[0].id])
    #     self.assertEqual(tag.name, "red")

    # def test_untag_companies(self):
    #     # Untag companies
    #     tag = Tag.untag_companies("blue", [self.user.companies[0].id])
    #     self.assertEqual(tag.name, "blue")

    # # # Iterate over all tags for company
    # # Tag.find_all_for_company(id='43357e2c3c77661e25000026')
    # # Tag.find_all_for_company(company_id='6')
