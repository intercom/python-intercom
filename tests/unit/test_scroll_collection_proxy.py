# -*- coding: utf-8 -*-
"""Test module for Scroll Collection Proxy."""
import unittest

from intercom import HttpError
from intercom.client import Client
from mock import call
from mock import patch
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import istest
from tests.unit import users_scroll


class CollectionProxyTest(unittest.TestCase):  # noqa

    def setUp(self):  # noqa
        self.client = Client()

    @istest
    def it_stops_iterating_if_no_users_returned(self):  # noqa
        body = users_scroll(include_users=False)
        with patch.object(Client, 'get', return_value=body) as mock_method:
            emails = [user.email for user in self.client.users.scroll()]
            mock_method.assert_called('/users/scroll', {})
            eq_(emails, [])  # noqa

    @istest
    def it_keeps_iterating_if_users_returned(self):  # noqa
        page1 = users_scroll(include_users=True)
        page2 = users_scroll(include_users=False)
        side_effect = [page1, page2]
        with patch.object(Client, 'get', side_effect=side_effect) as mock_method:  # noqa
            emails = [user.email for user in self.client.users.scroll()]
            eq_([call('/users/scroll', {}), call('/users/scroll', {'scroll_param': 'da6bbbac-25f6-4f07-866b-b911082d7'})],  # noqa
                mock_method.mock_calls)
            eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'])  # noqa

    @istest
    def it_supports_indexed_array_access(self):  # noqa
        body = users_scroll(include_users=True)
        with patch.object(Client, 'get', return_value=body) as mock_method:
            eq_(self.client.users.scroll()[0].email, 'user1@example.com')
            mock_method.assert_called_once_with('/users/scroll', {})
            eq_(self.client.users.scroll()[1].email, 'user2@example.com')

    @istest
    def it_returns_one_page_scroll(self):  # noqa
        body = users_scroll(include_users=True)
        with patch.object(Client, 'get', return_value=body):
            scroll = self.client.users.scroll()
            scroll.get_next_page()
            emails = [user['email'] for user in scroll.resources]
            eq_(emails, ['user1@example.com', 'user2@example.com', 'user3@example.com'])  # noqa

    @istest
    def it_keeps_iterating_if_called_with_scroll_param(self):  # noqa
        page1 = users_scroll(include_users=True)
        page2 = users_scroll(include_users=False)
        side_effect = [page1, page2]
        with patch.object(Client, 'get', side_effect=side_effect) as mock_method:  # noqa
            scroll = self.client.users.scroll()
            scroll.get_page()
            scroll.get_page('da6bbbac-25f6-4f07-866b-b911082d7')
            emails = [user['email'] for user in scroll.resources]
            eq_(emails, [])  # noqa

    @istest
    def it_works_with_an_empty_list(self):  # noqa
        body = users_scroll(include_users=False)
        with patch.object(Client, 'get', return_value=body) as mock_method:  # noqa
            scroll = self.client.users.scroll()
            scroll.get_page()
            emails = [user['email'] for user in scroll.resources]
            eq_(emails, []) # noqa

    @istest
    def it_raises_an_http_error(self):  # noqa
        with patch.object(Client, 'get', return_value=None) as mock_method:  # noqa
            scroll = self.client.users.scroll()
            with assert_raises(HttpError):
                scroll.get_page()
