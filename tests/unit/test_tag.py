# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from intercom.tag import Tag
from nose.tools import eq_
from nose.tools import raises
from mock import patch
from unittest import TestCase

from . import create_response


class TagTest(TestCase):

    @raises(AttributeError)
    def test_writeonly_emails(self):
        tag = Tag()
        tag.emails

    def test_write_emails(self):
        tag = Tag()
        tag.emails = ["joe@example.com"]
        eq_(["joe@example.com"], tag['emails'])

    @raises(AttributeError)
    def test_writeonly_user_ids(self):
        tag = Tag()
        tag.user_ids

    def test_write_user_ids(self):
        tag = Tag()
        tag.user_ids = ["abc123"]
        eq_(["abc123"], tag['user_ids'])

    @raises(AttributeError)
    def test_writeonly_tag_or_untag(self):
        tag = Tag()
        tag.tag_or_untag

    def test_write_tag_or_untag(self):
        tag = Tag()
        tag.tag_or_untag = "tag"
        eq_('tag', tag['tag_or_untag'])

    @raises(AttributeError)
    def test_readonly_segment(self):
        tag = Tag()
        tag.segment = "xyz"

    @raises(AttributeError)
    def test_readonly_user_count(self):
        tag = Tag()
        tag.tagged_user_count = 0

    @raises(AttributeError)
    def test_readonly_id(self):
        tag = Tag()
        tag.id = 0

    def test_accessor(self):
        tag = Tag()

        tag.name = "xyz"
        eq_("xyz", tag.name)

    @patch('requests.request', create_response(200, 'create_tag_valid.json'))
    def test_create(self):
        tag = Tag.create(name="Poweruser", tag_or_untag="tag")
        eq_(None, tag.id)
        eq_(False, tag.segment)
        eq_(None, tag.tagged_user_count)

    @patch('requests.request', create_response(200, 'create_tag_valid.json'))
    def test_update(self):
        tag = Tag()
        tag.save()
        eq_(None, tag.id)

    @patch('requests.request', create_response(200, 'get_tag_valid.json'))
    def test_find(self):
        tag = Tag.find(name="Poweruser")
        eq_(None, tag.id)

    @patch('requests.request', create_response(200, 'get_tag_valid.json'))
    def test_find_by_name(self):
        tag = Tag.find_by_name("Poweruser")
        eq_(None, tag.id)
