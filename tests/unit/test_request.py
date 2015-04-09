# -*- coding: utf-8 -*-

import intercom
import json
import unittest

from intercom import Intercom
from intercom import Request
from intercom import UnexpectedError
from mock import Mock
from mock import patch
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import istest

headers = {
    'x-ratelimit-limit': 500,
    'x-ratelimit-remaining': 500,
    'x-ratelimit-reset': 1427932858
}


class RequestTest(unittest.TestCase):

    @istest
    def it_raises_resource_not_found(self):
        resp = Mock(text='{}', status_code=404)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.ResourceNotFound):
                Request.send_request_to_path('GET', 'notes', ('x', 'y'), resp)

    @istest
    def it_raises_authentication_error_unauthorized(self):
        resp = Mock(text='{}', status_code=401)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.AuthenticationError):
                Request.send_request_to_path('GET', 'notes', ('x', 'y'), resp)

    @istest
    def it_raises_authentication_error_forbidden(self):
        resp = Mock(text='{}', status_code=403)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.AuthenticationError):
                Request.send_request_to_path('GET', 'notes', ('x', 'y'), resp)

    @istest
    def it_raises_server_error(self):
        resp = Mock(text='{}', status_code=500)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.ServerError):
                Request.send_request_to_path('GET', 'notes', ('x', 'y'), resp)

    @istest
    def it_raises_bad_gateway_error(self):
        resp = Mock(text='{}', status_code=502)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.BadGatewayError):
                Request.send_request_to_path('GET', 'notes', ('x', 'y'), resp)

    @istest
    def it_raises_service_unavailable_error(self):
        resp = Mock(text='{}', status_code=503)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.ServiceUnavailableError):
                Request.send_request_to_path('GET', 'notes', ('x', 'y'), resp)

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
        resp = Mock(text=content, status_code=200, headers=headers)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            try:
                Intercom.get('/users')
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
        resp = Mock(text=content, status_code=200, headers=headers)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            try:
                Intercom.get('/users')
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
            resp = Mock(text=content, status_code=200, headers=headers)
            with patch('requests.request') as mock_method:
                mock_method.return_value = resp
                with assert_raises(intercom.BadRequestError):
                    Intercom.get('/users')

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
            resp = Mock(text=content, status_code=200, headers=headers)
            with patch('requests.request') as mock_method:
                mock_method.return_value = resp
                with assert_raises(intercom.AuthenticationError):
                    Intercom.get('/users')

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
        resp = Mock(text=content, status_code=200, headers=headers)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.ResourceNotFound):
                Intercom.get('/users')

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
        resp = Mock(text=content, status_code=200, headers=headers)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.RateLimitExceeded):
                Intercom.get('/users')

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
        resp = Mock(text=content, status_code=200, headers=headers)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.ServiceUnavailableError):
                Intercom.get('/users')

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
        resp = Mock(text=content, status_code=200, headers=headers)
        with patch('requests.request') as mock_method:
            mock_method.return_value = resp
            with assert_raises(intercom.MultipleMatchingUsersError):
                Intercom.get('/users')
