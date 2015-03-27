# -*- coding: utf-8 -*-

import httpretty
import intercom
import json
import re
import unittest

from intercom import Intercom
from intercom import UnexpectedError
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import istest

get = httpretty.GET
post = httpretty.POST
r = re.compile


class RequestTest(unittest.TestCase):

    @istest
    @httpretty.activate
    def it_raises_resource_not_found(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=404)
        with assert_raises(intercom.ResourceNotFound):
            Intercom.get('/notes')

    @istest
    @httpretty.activate
    def it_raises_authentication_error_unauthorized(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=401)
        with assert_raises(intercom.AuthenticationError):
            Intercom.get('/notes')

    @istest
    @httpretty.activate
    def it_raises_authentication_error_forbidden(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=403)
        with assert_raises(intercom.AuthenticationError):
            Intercom.get('/notes')

    @istest
    @httpretty.activate
    def it_raises_server_error(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=500)
        with assert_raises(intercom.ServerError):
            Intercom.get('/notes')

    @istest
    @httpretty.activate
    def it_raises_bad_gateway_error(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=502)
        with assert_raises(intercom.BadGatewayError):
            Intercom.get('/notes')

    @istest
    @httpretty.activate
    def it_raises_service_unavailable_error(self):
        httpretty.register_uri(
            get, r(r'/notes$'), body='', status=503)
        with assert_raises(intercom.ServiceUnavailableError):
            Intercom.get('/notes')

    @istest
    @httpretty.activate
    def it_raises_an_unexpected_typed_error(self):
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'type': 'hopper',
                    'message': 'The first compiler.'
                }
            ]
        }
        httpretty.register_uri(get, r("/users"), body=json.dumps(payload))
        try:
            Intercom.get('/users')
        except (UnexpectedError) as err:
            ok_("The error of type 'hopper' is not recognized" in err.message)  # noqa
            eq_(err.context['http_code'], 200)
            eq_(err.context['application_error_code'], 'hopper')

    @istest
    @httpretty.activate
    def it_raises_an_unexpected_untyped_error(self):
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'message': 'UNIVAC'
                }
            ]
        }
        httpretty.register_uri(get, r("/users"), body=json.dumps(payload))
        try:
            Intercom.get('/users')
        except (UnexpectedError) as err:
            ok_("An unexpected error occured." in err.message)
            eq_(err.context['application_error_code'], None)

    @istest
    @httpretty.activate
    def it_raises_a_bad_request_error(self):
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'type': None,
                    'message': 'email is required'
                }
            ]
        }

        for code in ['missing_parameter', 'parameter_invalid', 'bad_request']:
            payload['errors'][0]['type'] = code
            httpretty.register_uri(get, r("/users"), body=json.dumps(payload))
            with assert_raises(intercom.BadRequestError):
                Intercom.get('/users')

    @istest
    @httpretty.activate
    def it_raises_an_authentication_error(self):
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'type': 'unauthorized',
                    'message': 'Your name\'s not down.'
                }
            ]
        }
        for code in ['unauthorized', 'forbidden']:
            payload['errors'][0]['type'] = code
            httpretty.register_uri(get, r("/users"), body=json.dumps(payload))
            with assert_raises(intercom.AuthenticationError):
                Intercom.get('/users')

    @istest
    @httpretty.activate
    def it_raises_resource_not_found_by_type(self):
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'type': 'not_found',
                    'message': 'Waaaaally?'
                }
            ]
        }
        httpretty.register_uri(get, r("/users"), body=json.dumps(payload))
        with assert_raises(intercom.ResourceNotFound):
            Intercom.get('/users')

    @istest
    @httpretty.activate
    def it_raises_rate_limit_exceeded(self):
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'type': 'rate_limit_exceeded',
                    'message': 'Fair use please.'
                }
            ]
        }
        httpretty.register_uri(get, r("/users"), body=json.dumps(payload))
        with assert_raises(intercom.RateLimitExceeded):
            Intercom.get('/users')

    @istest
    @httpretty.activate
    def it_raises_a_service_unavailable_error(self):
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'type': 'service_unavailable',
                    'message': 'Zzzzz.'
                }
            ]
        }
        httpretty.register_uri(get, r("/users"), body=json.dumps(payload))
        with assert_raises(intercom.ServiceUnavailableError):
            Intercom.get('/users')

    @istest
    @httpretty.activate
    def it_raises_a_multiple_matching_users_error(self):
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'type': 'conflict',
                    'message': 'Two many cooks.'
                }
            ]
        }
        httpretty.register_uri(get, r("/users"), body=json.dumps(payload))
        with assert_raises(intercom.MultipleMatchingUsersError):
            Intercom.get('/users')
