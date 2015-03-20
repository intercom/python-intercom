import httpretty
import json
import re

from describe import expect
from intercom import Subscription
from tests.unit import test_subscription


get = httpretty.GET
post = httpretty.POST

r = re.compile


class DescribeIntercomSubscription:

    @httpretty.activate
    def it_gets_a_subscription(self):
        body = json.dumps(test_subscription)

        httpretty.register_uri(
            get, r(r"/subscriptions/nsub_123456789"),
            body=body)

        subscription = Subscription.find(id="nsub_123456789")
        expect(subscription.topics[0]) == "user.created"
        expect(subscription.topics[1]) == "conversation.user.replied"
        expect(subscription.self) == \
            "https://api.intercom.io/subscriptions/nsub_123456789"

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
        expect(subscription.topics[0]) == "user.created"
        expect(subscription.url) == "http://example.com"
