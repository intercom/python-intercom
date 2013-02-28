# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from mock import patch
from nose.tools import raises
from unittest import TestCase

from . import create_response

from intercom.intercom import AuthenticationError
from intercom import Impression

class ImpressionTest(TestCase):

    @raises(AuthenticationError)
    @patch('requests.request', create_response(401))
    def test_create_impression_identifiers(self):
        Impression.create()

    @patch('requests.request', create_response(200, 'create_impression_valid.json'))
    def test_create_impression_valid(self):
        impression = Impression.create(email='xxx@example.com')
        self.assertEqual(0, impression.unread_messages)

        # check params
        impression = Impression.create(email='xxx@example.com', location="home",
            user_ip='1.2.3.4', user_agent='Mozilla/5.0')
        self.assertEqual(0, impression.unread_messages)

    def test_properties(self):
        impression = Impression()
        impression.user_ip = '192.168.1.100'
        impression.location = 'http://example.com/profile/'
        impression.user_agent = 'Mozilla/5.0'

        self.assertEquals('192.168.1.100', impression.user_ip)
        self.assertEquals('http://example.com/profile/', impression.location)
        self.assertEquals('Mozilla/5.0', impression.user_agent)

    @patch('requests.request', create_response(200, 'create_impression_valid.json'))
    def test_save(self):
        impression = Impression(email='xxx@example.com')
        impression.save()        
        self.assertEqual(0, impression.unread_messages)
