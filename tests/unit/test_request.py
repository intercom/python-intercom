# -*- coding: utf-8 -*-

import intercom
import json
import unittest

from intercom.client import Client
from intercom.request import Request
from intercom import UnexpectedError
from mock import patch
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import istest
from tests.unit import mock_response


class RequestTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    @istest
    def it_raises_resource_not_found(self):
        resp = mock_response(None, status_code=404)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.ResourceNotFound):
                request = Request('GET', 'notes')
                request.send_request_to_path('', ('x', 'y'), resp)

    @istest
    def it_raises_authentication_error_unauthorized(self):
        resp = mock_response(None, status_code=401)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.AuthenticationError):
                request = Request('GET', 'notes')
                request.send_request_to_path('', ('x', 'y'), resp)

    @istest
    def it_raises_authentication_error_forbidden(self):
        resp = mock_response(None, status_code=403)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.AuthenticationError):
                request = Request('GET', 'notes')
                request.send_request_to_path('', ('x', 'y'), resp)

    @istest
    def it_raises_server_error(self):
        resp = mock_response(None, status_code=500)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.ServerError):
                request = Request('GET', 'notes')
                request.send_request_to_path('', ('x', 'y'), resp)

    @istest
    def it_raises_bad_gateway_error(self):
        resp = mock_response(None, status_code=502)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.BadGatewayError):
                request = Request('GET', 'notes')
                request.send_request_to_path('', ('x', 'y'), resp)

    @istest
    def it_raises_service_unavailable_error(self):
        resp = mock_response(None, status_code=503)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.ServiceUnavailableError):
                request = Request('GET', 'notes')
                request.send_request_to_path('', ('x', 'y'), resp)

    @istest
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
        content = json.dumps(payload).encode('utf-8')
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            try:
                self.client.get('/users', {})
                self.fail('UnexpectedError not raised.')
            except (UnexpectedError) as err:
                ok_("The error of type 'hopper' is not recognized" in err.message)  # noqa
                eq_(err.context['http_code'], 200)
                eq_(err.context['application_error_code'], 'hopper')

    @istest
    def it_raises_an_unexpected_untyped_error(self):
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'message': 'UNIVAC'
                }
            ]
        }
        content = json.dumps(payload).encode('utf-8')
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            try:
                self.client.get('/users', {})
                self.fail('UnexpectedError not raised.')
            except (UnexpectedError) as err:
                ok_("An unexpected error occured." in err.message)
                eq_(err.context['application_error_code'], None)

    @istest
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

            content = json.dumps(payload).encode('utf-8')
            resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
                mock_method.return_value = resp
                with assert_raises(intercom.BadRequestError):
                    self.client.get('/users', {})

    @istest
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

            content = json.dumps(payload).encode('utf-8')
            resp = mock_response(content)
            with patch('requests.sessions.Session.request') as mock_method:
                mock_method.return_value = resp
                with assert_raises(intercom.AuthenticationError):
                    self.client.get('/users', {})

    @istest
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
        content = json.dumps(payload).encode('utf-8')
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.ResourceNotFound):
                self.client.get('/users', {})

    @istest
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
        content = json.dumps(payload).encode('utf-8')
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.RateLimitExceeded):
                self.client.get('/users', {})

    @istest
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
        content = json.dumps(payload).encode('utf-8')
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.ServiceUnavailableError):
                self.client.get('/users', {})

    @istest
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
        content = json.dumps(payload).encode('utf-8')
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.MultipleMatchingUsersError):
                self.client.get('/users', {})

    @istest
    def it_raises_token_unauthorized(self):
        payload = {
            'type': 'error.list',
            'errors': [
                {
                    'type': 'token_unauthorized',
                    'message': 'The PAT is not authorized for this action.'
                }
            ]
        }
        content = json.dumps(payload).encode('utf-8')
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.TokenUnauthorizedError):
                self.client.get('/users', {})

    @istest
    def it_handles_no_error_type(self):
        payload = {
            'errors': [
                {
                    'code': 'unique_user_constraint',
                    'message': 'User already exists.'
                }
            ],
            'request_id': '00000000-0000-0000-0000-000000000000',
            'type': 'error.list'
        }
        content = json.dumps(payload).encode('utf-8')
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.MultipleMatchingUsersError):
                self.client.get('/users', {})

        payload = {
            'errors': [
                {
                    'code': 'parameter_not_found',
                    'message': 'missing data parameter'
                }
            ],
            'request_id': None,
            'type': 'error.list'
        }
        content = json.dumps(payload).encode('utf-8')
        resp = mock_response(content)
        with patch('requests.sessions.Session.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.BadRequestError):
                self.client.get('/users', {})

    @istest
    def it_handles_empty_responses(self):
        resp = mock_response('', status_code=202)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            request = Request('GET', 'events')
            request.send_request_to_path('', ('x', 'y'), resp)

        resp = mock_response(' ', status_code=202)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            request = Request('GET', 'events')
            request.send_request_to_path('', ('x', 'y'), resp)

    @istest
    def it_handles_no_encoding(self):
        resp = mock_response(
            ' ', status_code=200, encoding=None, headers=None)
        resp.apparent_encoding = 'utf-8'

        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            request = Request('GET', 'events')
            request.send_request_to_path('', ('x', 'y'), resp)

    @istest
    def it_needs_encoding_or_apparent_encoding(self):
        payload = '{}'

        if not hasattr(payload, 'decode'):
            # python 3
            payload = payload.encode('utf-8')

        resp = mock_response(
            payload, status_code=200, encoding=None, headers=None)

        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(TypeError):
                request = Request('GET', 'events')
                request.send_request_to_path('', ('x', 'y'), resp)

    @istest
    def it_allows_the_timeout_to_be_changed(self):
        from intercom.request import Request
        try:
            eq_(90, Request.timeout)
            Request.timeout = 3
            eq_(3, Request.timeout)
        finally:
            Request.timeout = 90

    @istest
    def it_allows_the_timeout_to_be_configured(self):
        import os
        from intercom.request import configure_timeout

        # check the default
        eq_(90, configure_timeout())

        # override the default
        os.environ['INTERCOM_REQUEST_TIMEOUT'] = '20'
        eq_(20, configure_timeout())

        # ignore bad timeouts, reset to default 90
        os.environ['INTERCOM_REQUEST_TIMEOUT'] = 'abc'
        eq_(90, configure_timeout())
