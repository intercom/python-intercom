# -*- coding: utf-8 -*-

import unittest

from intercom import Notification
from intercom.utils import create_class_instance
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
    def it_returns_correct_model_type_for_user(self):
        payload = Notification(**test_user_notification)
        User = create_class_instance('User')  # noqa

        self.assertIsInstance(payload.model, User.__class__)
        eq_(payload.model_type, User.__class__)

    @istest
    def it_returns_correct_user_notification_topic(self):
        payload = Notification(**test_user_notification)
        eq_(payload.topic, "user.created")

    @istest
    def it_returns_instance_of_user(self):
        User = create_class_instance('User')  # noqa
        payload = Notification(**test_user_notification)
        self.assertIsInstance(payload.model, User.__class__)

    @istest
    def it_returns_instance_of_conversation(self):
        Conversation = create_class_instance('Conversation')  # noqa
        payload = Notification(**test_conversation_notification)
        self.assertIsInstance(payload.model, Conversation.__class__)

    @istest
    def it_returns_correct_model_type_for_conversation(self):
        Conversation = create_class_instance('Conversation')  # noqa
        payload = Notification(**test_conversation_notification)
        eq_(payload.model_type, Conversation.__class__)

    @istest
    def it_returns_correct_conversation_notification_topic(self):
        payload = Notification(**test_conversation_notification)
        eq_(payload.topic, "conversation.user.created")

    @istest
    def it_returns_inner_user_object_for_conversation(self):
        User = create_class_instance('User')  # noqa
        payload = Notification(**test_conversation_notification)
        self.assertIsInstance(payload.model.user, User.__class__)

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
