import httpretty
import json
import re
from describe import expect
from intercom import Tag
from tests.unit import test_tag

get = httpretty.GET
post = httpretty.POST
r = re.compile


class DescribeIntercomTag:

    @httpretty.activate
    def it_gets_a_tag(self):
        httpretty.register_uri(
            get, r(r'/tags'), body=json.dumps(test_tag))
        tag = Tag.find(name="Test Tag")
        expect(tag.name) == "Test Tag"

    @httpretty.activate
    def it_creates_a_tag(self):
        httpretty.register_uri(
            post, r(r'/tags'), body=json.dumps(test_tag))
        tag = Tag.create(name="Test Tag")
        expect(tag.name) == "Test Tag"

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
        expect(tag.name) == "Test Tag"
        expect(tag.tagged_user_count) == 2
