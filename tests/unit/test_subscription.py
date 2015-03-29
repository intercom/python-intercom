# -*- coding: utf-8 -*-

import httpretty
import json
import re
import unittest

from intercom import Subscription
from nose.tools import eq_
from nose.tools import istest
from tests.unit import test_subscription

get = httpretty.GET
post = httpretty.POST

r = re.compile


class SubscriptionTest(unittest.TestCase):

    @istest
    @httpretty.activate
    def it_gets_a_subscription(self):
        body = json.dumps(test_subscription)

        httpretty.register_uri(
            get, r(r"/subscriptions/nsub_123456789"),
            body=body)

        subscription = Subscription.find(id="nsub_123456789")
        eq_(subscription.topics[0], "user.created")
        eq_(subscription.topics[1], "conversation.user.replied")
        eq_(subscription.self,
            "https://api.intercom.io/subscriptions/nsub_123456789")

    @istest
    @httpretty.activate
    def it_creates_a_subscription(self):
        body = json.dumps(test_subscription)
        httpretty.register_uri(
            post, r(r"/subscriptions/"),
            body=body, match_querystring=True)

        subscription = Subscription.create(
            url="http://example.com",
            topics=["user.created"]
        )
        eq_(subscription.topics[0], "user.created")
        eq_(subscription.url, "http://example.com")
