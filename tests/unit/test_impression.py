# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from intercom import Impression
from sure import expect


def test_properties():
    impression = Impression()
    impression.user_ip = '192.168.1.100'
    impression.location = 'http://example.com/profile/'
    impression.user_agent = 'Mozilla/5.0'

    expect(impression.user_ip).to.equal('192.168.1.100')
    expect(impression.location).to.equal('http://example.com/profile/')
    expect(impression.user_agent).to.equal('Mozilla/5.0')
