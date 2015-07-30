# -*- coding: utf-8 -*-

import os
import unittest
from intercom import Intercom
from intercom import Admin
from intercom import Conversation
from intercom import Message
from . import delete
from . import get_or_create_user
from . import get_timestamp

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class ConversationTest(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        # get admin
        cls.admin = Admin.all()[1]

        # get user
        timestamp = get_timestamp()
        cls.user = get_or_create_user(timestamp)
        cls.email = cls.user.email

        # send user message
        message_data = {
            'from': {
                'type': "user",
                'id': cls.user.id
            },
            'body': "Hey"
        }
        cls.user_message = Message.create(**message_data)

        conversations = Conversation.find_all()
        user_init_conv = conversations[0]
        # send admin reply
        cls.admin_conv = user_init_conv.reply(
            type='admin', admin_id=cls.admin.id,
            message_type='comment', body='There')

    @classmethod
    def teardown_class(cls):
        delete(cls.user)

    def test_find_all_admin(self):
        # FINDING CONVERSATIONS FOR AN ADMIN
        # Iterate over all conversations (open and closed) assigned to an admin
        for convo in Conversation.find_all(type='admin', id=self.admin.id):
            self.assertIsNotNone(convo.id)
            self.admin_conv.id = convo.id

    def test_find_all_open_admin(self):
        # Iterate over all open conversations assigned to an admin
        for convo in Conversation.find_all(
                type='admin', id=self.admin.id, open=True):
            self.assertIsNotNone(convo.id)

    def test_find_all_closed_admin(self):
        # Iterate over closed conversations assigned to an admin
        for convo in Conversation.find_all(
                type='admin', id=self.admin.id, open=False):
            self.assertIsNotNone(convo.id)

    def test_find_all_closed_before_admin(self):
        for convo in Conversation.find_all(
                type='admin', id=self.admin.id, open=False,
                before=1374844930):
            self.assertIsNotNone(convo.id)

    def test_find_all_user(self):
        # FINDING CONVERSATIONS FOR A USER
        # Iterate over all conversations (read + unread, correct) with a
        # user based on the users email
        for convo in Conversation.find_all(email=self.email, type='user'):
            self.assertIsNotNone(convo.id)

    def test_find_all_read(self):
        # Iterate over through all conversations (read + unread) with a
        # user based on the users email
        for convo in Conversation.find_all(
                email=self.email, type='user', unread=False):
            self.assertIsNotNone(convo.id)

    def test_find_all_unread(self):
        # Iterate over all unread conversations with a user based on the
        # users email
        for convo in Conversation.find_all(
                email=self.email, type='user', unread=True):
            self.assertIsNotNone(convo.id)

    def test_find_single_conversation(self):
        # FINDING A SINGLE CONVERSATION
        convo_id = Conversation.find_all(type='admin', id=self.admin.id)[0].id
        conversation = Conversation.find(id=convo_id)
        self.assertEqual(conversation.id, convo_id)

    def test_conversation_parts(self):
        # INTERACTING WITH THE PARTS OF A CONVERSATION
        convo_id = Conversation.find_all(type='admin', id=self.admin.id)[0].id
        conversation = Conversation.find(id=convo_id)

        # Getting the subject of a part (only applies to email-based
        # conversations)
        self.assertEqual(conversation.conversation_message.subject, "")
        for part in conversation.conversation_parts:
            # There is a part_type
            self.assertIsNotNone(part.part_type)
            # There is a body
            if not part.part_type == 'assignment':
                self.assertIsNotNone(part.body)

    def test_reply(self):
        # REPLYING TO CONVERSATIONS
        conversation = Conversation.find(id=self.admin_conv.id)
        num_parts = len(conversation.conversation_parts)
        # User (identified by email) replies with a comment
        conversation.reply(
            type='user', email=self.email,
            message_type='comment', body='foo')
        # Admin (identified by admin_id) replies with a comment
        conversation.reply(
            type='admin', admin_id=self.admin.id,
            message_type='comment', body='bar')
        conversation = Conversation.find(id=self.admin_conv.id)
        self.assertEqual(num_parts + 2, len(conversation.conversation_parts))

    def test_open(self):
        # OPENING CONVERSATIONS
        conversation = Conversation.find(id=self.admin_conv.id)
        conversation.close_conversation(admin_id=self.admin.id, body='Closing message')
        self.assertFalse(conversation.open)
        conversation.open_conversation(admin_id=self.admin.id, body='Opening message')
        conversation = Conversation.find(id=self.admin_conv.id)
        self.assertTrue(conversation.open)

    def test_close(self):
        # CLOSING CONVERSATIONS
        conversation = Conversation.find(id=self.admin_conv.id)
        self.assertTrue(conversation.open)
        conversation.close_conversation(admin_id=self.admin.id, body='Closing message')
        conversation = Conversation.find(id=self.admin_conv.id)
        self.assertFalse(conversation.open)

    def test_assignment(self):
        # ASSIGNING CONVERSATIONS
        conversation = Conversation.find(id=self.admin_conv.id)
        num_parts = len(conversation.conversation_parts)
        conversation.assign(assignee_id=self.admin.id, admin_id=self.admin.id)
        conversation = Conversation.find(id=self.admin_conv.id)
        self.assertEqual(num_parts + 1, len(conversation.conversation_parts))
        self.assertEqual("assignment", conversation.conversation_parts[-1].part_type)

    def test_mark_read(self):
        # MARKING A CONVERSATION AS READ
        conversation = Conversation.find(id=self.admin_conv.id)
        conversation.read = False
        conversation.save()
        conversation = Conversation.find(id=self.admin_conv.id)
        self.assertFalse(conversation.read)
        conversation.read = True
        conversation.save()
        conversation = Conversation.find(id=self.admin_conv.id)
        self.assertTrue(conversation.read)
