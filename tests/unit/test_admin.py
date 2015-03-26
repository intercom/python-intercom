# -*- coding: utf-8 -*-

import unittest

from intercom import Request
from intercom import Admin
from intercom.collection_proxy import CollectionProxy
from mock import patch
from nose.tools import assert_raises
from nose.tools import istest


def send_request(*args, **kwargs):
    # empty impl
    raise (AssertionError)


class AdminTest(unittest.TestCase):

    @istest
    @patch.object(Request, 'send_request_to_path', send_request)
    def it_returns_a_collection_proxy_for_all_without_making_any_requests(self):  # noqa
        # prove a call to send_request_to_path will raise an error
        with assert_raises(AssertionError):
            send_request()
        all = Admin.all()
        self.assertIsInstance(all, CollectionProxy)
