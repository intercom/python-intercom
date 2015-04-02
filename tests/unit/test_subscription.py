# -*- coding: utf-8 -*-

import unittest

from intercom import Intercom
from intercom import Subscription
from mock import patch
from nose.tools import eq_
from nose.tools import istest
from tests.unit import test_subscription


class SubscriptionTest(unittest.TestCase):

    @istest
    def it_gets_a_subscription(self):
        with patch.object(Intercom, 'get', return_value=test_subscription) as mock_method:  # noqa
            subscription = Subscription.find(id="nsub_123456789")
            eq_(subscription.topics[0], "user.created")
            eq_(subscription.topics[1], "conversation.user.replied")
            eq_(subscription.self,
                "https://api.intercom.io/subscriptions/nsub_123456789")
            mock_method.assert_called_once_with('/subscriptions/nsub_123456789')  # noqa

    @istest
    def it_creates_a_subscription(self):
        with patch.object(Intercom, 'post', return_value=test_subscription) as mock_method:  # noqa
            subscription = Subscription.create(
                url="http://example.com",
                topics=["user.created"]
            )
            eq_(subscription.topics[0], "user.created")
            eq_(subscription.url, "http://example.com")
            mock_method.assert_called_once_with(
                '/subscriptions/', url="http://example.com", topics=["user.created"])  # noqa
