# -*- coding: utf-8 -*-

import os
import unittest
from intercom import Intercom
from intercom import Admin
from intercom import Conversation
from intercom import User

Intercom.app_id = os.environ.get('INTERCOM_APP_ID')
Intercom.app_api_key = os.environ.get('INTERCOM_APP_API_KEY')


class ConversationTest(unittest.TestCase):
    email = "ada@example.com"

    @classmethod
    def setup_class(cls):
        # get admin
        cls.admin = Admin.all()[0]
        # get user
        cls.user = User.find(email=cls.email)
        if not hasattr(cls.user, 'user_id'):
            # Create a user
            cls.user = User.create(
                email=cls.email,
                user_id="ada",
                name="Ada Lovelace")
            cls.user.companies = [
                {"company_id": 6, "name": "Intercom"},
                {"company_id": 9, "name": "Test Company"}
            ]
            cls.user.save()

    def test_find_all_admin(self):
        # FINDING CONVERSATIONS FOR AN ADMIN
        # Iterate over all conversations (open and closed) assigned to an admin

        for convo in Conversation.find_all(type='admin', id=self.admin.id):
            self.assertIsNotNone(convo.id)
            self.__class__.convo_id = convo.id

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
            self.assertIsNotNone(part.body)

    # def test_reply(self):
    #     # REPLYING TO CONVERSATIONS
    #     convo_id = Conversation.find_all(type='admin', id=self.admin.id)[0].id
    #     conversation = Conversation.find(id=convo_id)
    #     num_parts = len(conversation.conversation_parts)
    #     # User (identified by email) replies with a comment
    #     conversation.reply(
    #         type='user', email=self.email,
    #         message_type='comment', body='foo')
    #     # Admin (identified by email) replies with a comment
    #     conversation.reply(
    #         type='admin', email=self.admin.email,
    #         message_type='comment', body='bar')
    #     conversation = Conversation.find(id=convo_id)
    #     self.assertEqual(num_parts + 2, len(conversation.conversation_parts))

    def test_mark_read(self):
        # MARKING A CONVERSATION AS READ
        convo_id = Conversation.find_all(type='admin', id=self.admin.id)[0].id
        conversation = Conversation.find(id=convo_id)
        conversation.read = False
        conversation.save()
        conversation = Conversation.find(id=convo_id)
        # CANNOT MARK AS UNREAD VIA API
        # self.assertFalse(conversation.read)
        conversation.read = True
        conversation.save()
        conversation = Conversation.find(id=convo_id)
        self.assertTrue(conversation.read)
