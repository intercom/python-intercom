# -*- coding: utf-8 -*-

from .errors import HttpError  # noqa

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

        if resp.content:
            return json.loads(resp.content)


class ResourceEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'attributes'):
            # handle API resources
            return o.attributes
        return super(ResourceEncoder, self).default(o)
