# -*- coding: utf-8 -*-

from describe import expect
from intercom.notification import Notification
from intercom.utils import create_class_instance
from tests.unit import test_conversation_notification
from tests.unit import test_user_notification


class DescribeIntercomNotification:

    def it_converts_notification_hash_to_object(self):
        payload = Notification(**test_user_notification)
        expect(payload).to.be_instance_of(Notification)

    def it_returns_correct_model_type_for_user(self):
        payload = Notification(**test_user_notification)
        User = create_class_instance('User')  # noqa

        expect(payload.model).to.be_instance_of(User.__class__)
        expect(payload.model_type) == User.__class__

    def it_returns_correct_user_notification_topic(self):
        payload = Notification(**test_user_notification)
        expect(payload.topic) == "user.created"

    def it_returns_instance_of_user(self):
        User = create_class_instance('User')  # noqa
        payload = Notification(**test_user_notification)
        expect(payload.model).to.be_instance_of(User.__class__)

    def it_returns_instance_of_conversation(self):
        Conversation = create_class_instance('Conversation')  # noqa
        payload = Notification(**test_conversation_notification)
        expect(payload.model).to.be_instance_of(Conversation.__class__)

    def it_returns_correct_model_type_for_conversation(self):
        Conversation = create_class_instance('Conversation')  # noqa
        payload = Notification(**test_conversation_notification)
        expect(payload.model_type) == Conversation.__class__

    def it_returns_correct_conversation_notification_topic(self):
        payload = Notification(**test_conversation_notification)
        expect(payload.topic) == "conversation.user.created"

    def it_returns_inner_user_object_for_conversation(self):
        User = create_class_instance('User')  # noqa
        payload = Notification(**test_conversation_notification)
        expect(payload.model.user).to.be_instance_of(User.__class__)

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
        expect(payload.model.tags) == []
