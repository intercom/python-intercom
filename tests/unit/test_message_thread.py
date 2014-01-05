# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from intercom.message_thread import MessageThread
from nose.tools import eq_
from nose.tools import raises


@raises(ValueError)
def test_find_no_thread_id():
    MessageThread.find(email='xxx@example.com')


def test_properties():
    message_thread = MessageThread()
    message_thread.thread_id = 12345
    message_thread.read = False
    message_thread.body = 'ABCDE'

    eq_(message_thread.thread_id, 12345)
    eq_(message_thread.read, False)

    try:
        message_thread.body
    except AttributeError:
        pass
