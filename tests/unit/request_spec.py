# -*- coding: utf-8 -*-

import httpretty
import intercom
import re
from describe import expect
from intercom import Intercom

get = httpretty.GET
post = httpretty.POST
r = re.compile


class DescribeRequest:

    @httpretty.activate
    def it_raises_resource_not_found(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=404)
        with expect.to_raise_error(intercom.ResourceNotFound):
            Intercom.get('/notes')

    @httpretty.activate
    def it_raises_authentication_error_unauthorized(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=401)
        with expect.to_raise_error(intercom.AuthenticationError):
            Intercom.get('/notes')

    @httpretty.activate
    def it_raises_authentication_error_forbidden(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=403)
        with expect.to_raise_error(intercom.AuthenticationError):
            Intercom.get('/notes')

    @httpretty.activate
    def it_raises_server_error(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=500)
        with expect.to_raise_error(intercom.ServerError):
            Intercom.get('/notes')

    @httpretty.activate
    def it_raises_bad_gateway_error(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=502)
        with expect.to_raise_error(intercom.BadGatewayError):
            Intercom.get('/notes')

    @httpretty.activate
    def it_raises_service_unavailable_error(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=503)
        with expect.to_raise_error(intercom.ServiceUnavailableError):
            Intercom.get('/notes')
