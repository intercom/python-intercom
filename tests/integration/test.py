# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from unittest import TestCase

from intercom import AuthenticationError
from intercom import ResourceNotFound
from intercom import ServerError
from intercom import Intercom
from intercom import User
from intercom import MessageThread
from intercom import Impression

from nose.tools import raises

Intercom.app_id = 'dummy-app-id'
Intercom.api_key = 'dummy-secret-key'

class IntegrationTest(TestCase):

    def test_user(self):
        user = User.find(email='somebody@example.com')
        self.assertEqual('Somebody', user.name)

    def test_delete_user(self):
        user = User.delete(email="to-delete@example.com")
        self.assertEqual("to-delete@example.com", user.email)

    @raises(ResourceNotFound)
    def test_not_found(self):
        User.find(email='not-found@example.com')

    @raises(ServerError)
    def test_server_error(self):
        User.find(email='server-error@example.com')

    @raises(AuthenticationError)
    def test_bad_api_key(self):
        try:
            Intercom.app_id = 'bad-app-id'
            Intercom.api_key = 'bad-secret-key'
            User.find(email='not-found@example.com')
        finally:
            Intercom.app_id = 'dummy-app-id'
            Intercom.api_key = 'dummy-secret-key'

    def test_message_threads(self):
        threads = MessageThread.find_all(email='somebody@example.com')
        self.assertEqual(1, len(threads))

    def test_message_thread(self):
        thread = MessageThread.find(email='somebody@example.com', thread_id=5591)
        self.assertEqual(5591, thread.thread_id)

    def test_impression(self):
        impression = Impression.create(email='somebody@example.com')
        self.assertEqual(1, impression.unread_messages)
