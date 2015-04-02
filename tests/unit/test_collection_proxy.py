# -*- coding: utf-8 -*-

import unittest

from intercom import Intercom
from intercom import User
from mock import call
from mock import patch
from nose.tools import eq_
from nose.tools import istest
from tests.unit import page_of_users


class CollectionProxyTest(unittest.TestCase):

    @istest
    def it_stops_iterating_if_no_next_link(self):
        body = page_of_users(include_next_link=False)
        with patch.object(Intercom, 'get', return_value=body) as mock_method:
            emails = [user.email for user in User.all()]
            mock_method.assert_called_once_with('/users')
            eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'])  # noqa

    @istest
    def it_keeps_iterating_if_next_link(self):
        page1 = page_of_users(include_next_link=True)
        page2 = page_of_users(include_next_link=False)
        side_effect = [page1, page2]
        with patch.object(Intercom, 'get', side_effect=side_effect) as mock_method:  # noqa
            emails = [user.email for user in User.all()]
            eq_([call('/users'), call('https://api.intercom.io/users?per_page=50&page=2')],  # noqa
                mock_method.mock_calls)
            eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'] * 2)  # noqa

    @istest
    def it_supports_indexed_array_access(self):
        body = page_of_users(include_next_link=False)
        with patch.object(Intercom, 'get', return_value=body) as mock_method:
            eq_(User.all()[0].email, 'user1@example.com')
            mock_method.assert_called_once_with('/users')

    @istest
    def it_supports_querying(self):
        body = page_of_users(include_next_link=False)
        with patch.object(Intercom, 'get', return_value=body) as mock_method:
            emails = [user.email for user in User.find_all(tag_name='Taggart J')]  # noqa
            eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'])  # noqa
            mock_method.assert_called_once_with('/users', tag_name='Taggart J')
