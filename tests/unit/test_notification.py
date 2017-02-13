# -*- coding: utf-8 -*-

import unittest

from intercom.notification import Notification
from intercom.utils import define_lightweight_class
from nose.tools import eq_
from nose.tools import istest
from tests.unit import test_conversation_notification
from tests.unit import test_user_notification


class NotificationTest(unittest.TestCase):

    @istest
    def it_converts_notification_hash_to_object(self):
        payload = Notification(**test_user_notification)
        self.assertIsInstance(payload, Notification)

    @istest
    def it_returns_correct_resource_type_for_part(self):
        payload = Notification(**test_user_notification)
        User = define_lightweight_class('user', 'User')  # noqa

        self.assertIsInstance(payload.model.__class__, User.__class__)
        eq_(payload.model_type.__class__, User.__class__)

    @istest
    def it_returns_correct_user_notification_topic(self):
        payload = Notification(**test_user_notification)
        eq_(payload.topic, "user.created")

    @istest
    def it_returns_instance_of_user(self):
        User = define_lightweight_class('user', 'User')  # noqa
        payload = Notification(**test_user_notification)
        self.assertIsInstance(payload.model.__class__, User.__class__)

    @istest
    def it_returns_instance_of_conversation(self):
        Conversation = define_lightweight_class('conversation', 'Conversation')  # noqa
        payload = Notification(**test_conversation_notification)
        self.assertIsInstance(payload.model.__class__, Conversation.__class__)

    @istest
    def it_returns_correct_model_type_for_conversation(self):
        Conversation = define_lightweight_class('conversation', 'Conversation')  # noqa
        payload = Notification(**test_conversation_notification)
        eq_(payload.model_type.__class__, Conversation.__class__)

    @istest
    def it_returns_correct_conversation_notification_topic(self):
        payload = Notification(**test_conversation_notification)
        eq_(payload.topic, "conversation.user.created")

    @istest
    def it_returns_inner_user_object_for_conversation(self):
        User = define_lightweight_class('user', 'User')  # noqa
        payload = Notification(**test_conversation_notification)
        self.assertIsInstance(payload.model.user.__class__, User.__class__)

    @istest
    def it_returns_inner_conversation_parts_for_conversation(self):
        payload = Notification(**test_conversation_notification)
        conversation_parts = payload.data.item.conversation_parts
        eq_(1, len(conversation_parts))
        eq_('conversation_part', conversation_parts[0].resource_type)

    @istest
    def it_returns_inner_user_object_with_nil_tags(self):
        user_notification = {
            "type": "notification_event",
            "app_id": "aa11aa",
            "data": {
                "type": "notification_event_data",
                "item": {
                    "type": "user",
                    "id": "abc123def",
                    "user_id": "666",
                    "email": "joe@example.com",
                    "name": "Joe",
                    "tags": {
                        "type": "tag.list",
                        "tags": None
                    }
                }
            }
        }
        payload = Notification(**user_notification)
        eq_(payload.model.tags, [])

    @istest
    def it_has_self_attribute(self):
        payload = Notification(**test_conversation_notification)
        eq_('http://example.com/resource/url/', payload.self)
