# -*- coding: utf-8 -*-

from . import errors

import json
import requests


class Request(object):

    timeout = 10

    @classmethod
    def send_request_to_path(cls, method, url, auth, params=None):
        """ Construct an API request, send it to the API, and parse the
        response. """
        from intercom import __version__
        req_params = {}

        headers = {
            'User-Agent': 'python-intercom/' + __version__,
            'Accept': 'application/json'
        }
        if method in ('POST', 'PUT', 'DELETE'):
            headers['content-type'] = 'application/json'
            req_params['data'] = json.dumps(params, cls=ResourceEncoder)
        elif method == 'GET':
            req_params['params'] = params
        req_params['headers'] = headers

        resp = requests.request(
            method, url, timeout=cls.timeout,
            auth=auth, **req_params)

        cls.raise_errors_on_failure(resp)

        if resp.content:
            return json.loads(resp.content)

    @classmethod
    def raise_errors_on_failure(cls, resp):
        if resp.status_code == 404:
            raise errors.ResourceNotFound('Resource Not Found')
        elif resp.status_code == 401:
            raise errors.AuthenticationError('Unauthorized')
        elif resp.status_code == 403:
            raise errors.AuthenticationError('Forbidden')
        elif resp.status_code == 500:
            raise errors.ServerError('Server Error')
        elif resp.status_code == 502:
            raise errors.BadGatewayError('Bad Gateway Error')
        elif resp.status_code == 503:
            raise errors.ServiceUnavailableError('Service Unavailable')


class ResourceEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'attributes'):
            # handle API resources
            return o.attributes
        return super(ResourceEncoder, self).default(o)
