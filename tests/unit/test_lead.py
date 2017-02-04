# -*- coding: utf-8 -*-  # noqa

import mock
import unittest

from intercom.collection_proxy import CollectionProxy
from intercom.client import Client
from intercom.lead import Lead
from intercom.user import User
from mock import patch
from nose.tools import istest
from tests.unit import get_user


class LeadTest(unittest.TestCase):  # noqa

    def setUp(self):  # noqa
        self.client = Client()

    @istest
    def it_should_be_listable(self):  # noqa
        proxy = self.client.leads.all()
        self.assertEquals('contacts', proxy.resource_name)
        self.assertEquals('/contacts', proxy.finder_url)
        self.assertEquals(Lead, proxy.resource_class)

    @istest
    def it_should_not_throw_errors_when_there_are_no_parameters(self):  # noqa
        with patch.object(Client, 'post') as mock_method:  # noqa
            self.client.leads.create()

    @istest
    def it_can_update_a_lead_with_an_id(self):  # noqa
        lead = Lead(id="de45ae78gae1289cb")
        with patch.object(Client, 'put') as mock_method:  # noqa
            self.client.leads.save(lead)
            mock_method.assert_called_once_with(
                '/contacts/de45ae78gae1289cb', {'custom_attributes': {}})

    @istest
    def it_can_convert(self):  # noqa
        lead = Lead.from_api({'user_id': 'contact_id'})
        user = User.from_api({'id': 'user_id'})

        with patch.object(Client, 'post', returns=get_user()) as mock_method:  # noqa
            self.client.leads.convert(lead, user)
            mock_method.assert_called_once_with(
                '/contacts/convert',
                {
                    'contact': {'user_id': lead.user_id},
                    'user': {'id': user.id}
                })

    @istest
    def it_returns_a_collectionproxy_for_all_without_making_any_requests(self):  # noqa
        with mock.patch('intercom.request.Request.send_request_to_path', new_callable=mock.NonCallableMock):  # noqa
            res = self.client.leads.all()
            self.assertIsInstance(res, CollectionProxy)

    @istest
    def it_deletes_a_contact(self):  # noqa
        lead = Lead(id="1")
        with patch.object(Client, 'delete') as mock_method:  # noqa
            self.client.leads.delete(lead)
            mock_method.assert_called_once_with('/contacts/1', {})
