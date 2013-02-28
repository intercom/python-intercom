# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import time

from datetime import datetime
from mock import patch
from nose.tools import raises
from unittest import TestCase

from . import create_response

from intercom.message_thread import MessageThread
from intercom import AuthenticationError

class MessageThreadTest(TestCase):

    @raises(AuthenticationError)
    @patch('requests.request', create_response(401))
    def test_get_message_threads_identifiers(self):
        MessageThread.find_all()

    @patch('requests.request', create_response(200, 
            'get_message_threads_valid.json'))
    def test_find_all(self):
        threads = MessageThread.find_all(email="xxx@example.com")
        self.assertEqual(2, len(threads))

        thread_1 = threads[0]
        messages_1 = thread_1.messages
        self.assertEqual(2, len(messages_1))
        self.assertEqual('xxx@example.com', messages_1[0].author.email)
        self.assertEqual(None, messages_1[0].author.name)

        thread_2 = threads[1]
        messages_2 = thread_2.messages
        self.assertEqual(1, len(messages_2))
        self.assertEqual('yyy@example.com', messages_2[0]['from']['email'])

    @patch('requests.request', create_response(200, 
            'get_message_thread_valid.json'))
    def test_find(self):
        message_thread = MessageThread.find(email="xxx@example.com", 
                thread_id=17565)
        self.assertEqual(17565, message_thread.thread_id)

        messages = message_thread.messages
        self.assertEqual('xxx@example.com', messages[0].author.email)
        self.assertEqual(False, messages[0].author.admin)
        self.assertEqual(None, messages[0].author.name)

        self.assertEqual(None, messages[1].author.email)
        self.assertEqual(None, messages[1].author.user_id)
        self.assertEqual(True, messages[1].author.admin)
        self.assertEqual('Joe', messages[1].author.name)
        self.assertEqual('https://example.com/avatar.jpg', 
                messages[1].author.avatar_path_50)

        self.assertTrue('Hi' in messages[1].html)
        self.assertTrue(isinstance(messages[1].created_at, datetime))
        self.assertEqual(1331767859, 
                time.mktime(messages[1].created_at.timetuple()))

    @raises(ValueError)
    def test_find_no_thread_id(self):
        message_thread = MessageThread.find(email="xxx@example.com")

    @patch('requests.request', create_response(200, 
            'get_message_thread_valid.json'))
    def test_create(self):
        message_thread = MessageThread.create(email='xxx@example.com', body="Hi!")

        messages = message_thread.messages
        self.assertEqual('xxx@example.com', messages[0].author.email)
        self.assertEqual(False, messages[0].author.admin)
        self.assertEqual(None, messages[0].author.name)

        self.assertEqual(None, messages[1].author.email)
        self.assertEqual(True, messages[1].author.admin)
        self.assertEqual('Joe', messages[1].author.name)

        self.assertTrue(isinstance(message_thread.created_at, datetime))
        self.assertEqual(1331764588, 
                time.mktime(message_thread.created_at.timetuple()))

        self.assertTrue(isinstance(message_thread.updated_at, datetime))
        self.assertEqual(1331767859, 
                time.mktime(message_thread.updated_at.timetuple()))

    @patch('requests.request', create_response(200, 
            'get_message_thread_valid.json'))
    def test_reply(self):
        message_thread = MessageThread.reply(email='xxx@example.com', 
                body="blah", thread_id=17565)
        self.assertTrue(isinstance(message_thread.created_at, datetime))
        self.assertEqual(1331764588, 
                time.mktime(message_thread.created_at.timetuple()))


    def test_properties(self):
        message_thread = MessageThread()
        message_thread.thread_id = 12345
        message_thread.read = False
        message_thread.body = 'ABCDE'

        self.assertEqual(12345, message_thread.thread_id)
        self.assertEqual(False, message_thread.read)

        try:
            message_thread.body
        except AttributeError:
            pass
