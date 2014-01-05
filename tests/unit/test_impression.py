# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from intercom import Impression
from nose.tools import eq_


def test_properties():
    impression = Impression()
    impression.user_ip = '192.168.1.100'
    impression.location = 'http://example.com/profile/'
    impression.user_agent = 'Mozilla/5.0'

    eq_(impression.user_ip, '192.168.1.100')
    eq_(impression.location, 'http://example.com/profile/')
    eq_(impression.user_agent, 'Mozilla/5.0')
