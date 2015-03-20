# -*- coding: utf-8 -*-

from describe import expect
from describe import patch
from intercom import Request
from intercom import Admin
from intercom.collection_proxy import CollectionProxy


class DescribeIntercomAdmin:

    @patch.object(Request, 'send_request_to_path')
    def it_returns_a_collection_proxy_for_all_without_making_any_requests(send_request, self):
        send_request.expects().and_raises(AssertionError)
        all = Admin.all()
        expect(all).to.be_instance_of(CollectionProxy)
