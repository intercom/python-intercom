# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from intercom.tag import Tag
from sure import expect
from nose.tools import raises


@raises(AttributeError)
def test_writeonly_emails():
    tag = Tag()
    tag.emails


def test_write_emails():
    tag = Tag()
    tag.emails = ["joe@example.com"]
    expect(tag['emails']).to.equal(["joe@example.com"])


@raises(AttributeError)
def test_writeonly_user_ids():
    tag = Tag()
    tag.user_ids


def test_write_user_ids():
    tag = Tag()
    tag.user_ids = ["abc123"]
    expect(tag['user_ids']).to.equal(["abc123"])


@raises(AttributeError)
def test_writeonly_tag_or_untag():
    tag = Tag()
    tag.tag_or_untag


def test_write_tag_or_untag():
    tag = Tag()
    tag.tag_or_untag = "tag"
    expect(tag['tag_or_untag']).to.equal("tag")


@raises(AttributeError)
def test_readonly_segment():
    tag = Tag()
    tag.segment = "segment"


def test_segment():
    tag = Tag(segment="segment")
    tag.segment


@raises(AttributeError)
def test_readonly_user_count():
    tag = Tag()
    tag.tagged_user_count = 0


@raises(AttributeError)
def test_readonly_id():
    tag = Tag()
    tag.id = 0


def test_accessor():
    tag = Tag()
    tag.name = "xyz"
    expect(tag.name).to.equal("xyz")
