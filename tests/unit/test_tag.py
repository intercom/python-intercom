# -*- coding: utf-8 -*-

import httpretty
import json
import re
import unittest

from intercom import Tag
from nose.tools import eq_
from nose.tools import istest
from tests.unit import test_tag

get = httpretty.GET
post = httpretty.POST
r = re.compile


class TagTest(unittest.TestCase):

    @istest
    @httpretty.activate
    def it_gets_a_tag(self):
        httpretty.register_uri(
            get, r(r'/tags'), body=json.dumps(test_tag))
        tag = Tag.find(name="Test Tag")
        eq_(tag.name, "Test Tag")

    @istest
    @httpretty.activate
    def it_creates_a_tag(self):
        httpretty.register_uri(
            post, r(r'/tags'), body=json.dumps(test_tag))
        tag = Tag.create(name="Test Tag")
        eq_(tag.name, "Test Tag")

    @istest
    @httpretty.activate
    def it_tags_users(self):
        params = {
            'name': 'Test Tag',
            'user_ids': ['abc123', 'def456'],
            'tag_or_untag': 'tag'
        }
        httpretty.register_uri(
            post, r(r'/tags'), body=json.dumps(test_tag))
        tag = Tag.create(**params)
        eq_(tag.name, "Test Tag")
        eq_(tag.tagged_user_count, 2)
