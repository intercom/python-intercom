from unittest import TestCase

from intercom.intercom import AuthError
from intercom.intercom import APIError
from intercom.intercom import NotFoundError
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

    @raises(NotFoundError)
    def test_not_found(self):
        User.find(email='not-found@example.com')

    @raises(APIError)
    def test_server_error(self):
        User.find(email='server-error@example.com')

    @raises(AuthError)
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

    def test_impression(self):
        impression = Impression.create(email='somebody@example.com')
        self.assertEqual(1, impression.unread_messages)
