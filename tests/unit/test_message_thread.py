# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from intercom.message_thread import MessageThread
from sure import expect


def test_find_no_thread_id():
    MessageThread.find.when.called_with(email='xxx@example.com')\
        .should.throw(ValueError)


def test_properties():
    message_thread = MessageThread()
    message_thread.thread_id = 12345
    message_thread.read = False
    message_thread.body = 'ABCDE'

    expect(message_thread.thread_id).to.equal(12345)
    expect(message_thread.read).to.equal(False)

    try:
        message_thread.body
    except AttributeError:
        pass
