# -*- coding: utf-8 -*-

import httpretty
import json
import re
import unittest

from intercom import User
from nose.tools import eq_
from nose.tools import istest
from tests.unit import page_of_users

get = httpretty.GET
r = re.compile


class CollectionProxyTest(unittest.TestCase):

    @istest
    @httpretty.activate
    def it_stops_iterating_if_no_next_link(self):
        body = json.dumps(page_of_users(include_next_link=False))
        httpretty.register_uri(get, r(r"/users"), body=body)
        emails = [user.email for user in User.all()]
        eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'])  # noqa

    @istest
    @httpretty.activate
    def it_keeps_iterating_if_next_link(self):
        page1 = json.dumps(page_of_users(include_next_link=True))
        page2 = json.dumps(page_of_users(include_next_link=False))
        httpretty.register_uri(get, r(r"/users$"), body=page1)
        httpretty.register_uri(
            get, r(r'/users\?per_page=50&page=2$'),
            body=page2, match_querystring=True)
        emails = [user.email for user in User.all()]
        eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'] * 2)  # noqa

    @istest
    @httpretty.activate
    def it_supports_indexed_array_access(self):
        body = json.dumps(page_of_users(include_next_link=False))
        httpretty.register_uri(get, r(r"/users$"), body=body)
        eq_(User.all()[0].email, 'user1@example.com')

    @istest
    @httpretty.activate
    def it_supports_querying(self):
        body = json.dumps(page_of_users(include_next_link=False))
        httpretty.register_uri(get, r(r"/users$"), body=body)
        emails = [user.email for user in User.find_all(tag_name='Taggart J')]
        eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'])  # noqa
