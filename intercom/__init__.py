# -*- coding: utf-8 -*-

from datetime import datetime
from json import JSONEncoder
from .errors import ArgumentError
from .lib.setter_property import SetterProperty

import copy
import json
import random
import re
import requests
import time

__version__ = '2.0-alpha'


RELATED_DOCS_TEXT = "See https://github.com/jkeyes/python-intercom \
for usage examples."
COMPATIBILITY_WARNING_TEXT = "It looks like you are upgrading from \
an older version of python-intercom. Please note that this new version \
(%s) is not backwards compatible." % (__version__)
COMPATIBILITY_WORKAROUND_TEXT = "To get rid of this error please set \
Intercom.app_api_key and don't set Intercom.api_key."
CONFIGURATION_REQUIRED_TEXT = "You must set both Intercom.app_id and \
Intercom.app_api_key to use this client."


class _Config(object):
    app_id = None
    app_api_key = None
    hostname = "api.intercom.io"
    protocol = "https"
    endpoints = None
    current_endpoint = None
    target_base_url = None
    timeout = 10
    endpoint_randomized_at = None


class Intercom(object):
    _config = _Config()
    _class_register = {}

    @classmethod
    def send_request_to_path(cls, method, path, params=None):
        """ Construct an API request, send it to the API, and parse the
        response. """
        req_params = {}
        if '://' in path:
            url = path
        else:
            url = cls.current_endpoint + path

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
            method, url, timeout=cls._config.timeout,
            auth=(Intercom.app_id, Intercom.app_api_key), **req_params)

        if resp.content:
            return json.loads(resp.content)

    @classmethod
    def get(cls, path, **params):
        return cls.send_request_to_path('GET', path, params)

    @classmethod
    def post(cls, path, **params):
        return cls.send_request_to_path('POST', path, params)

    @classmethod
    def put(cls, path, **params):
        return cls.send_request_to_path('PUT', path, params)

    @classmethod
    def delete(cls, path, **params):
        return cls.send_request_to_path('DELETE', path, params)

    class __metaclass__(type):

        @property
        def app_id(cls):
            return cls._config.app_id

        @app_id.setter
        def app_id(cls, value):
            cls._config.app_id = value

        @property
        def app_api_key(cls):
            return cls._config.app_api_key

        @app_api_key.setter
        def app_api_key(cls, value):
            cls._config.app_api_key = value

        @property
        def _random_endpoint(cls):
            if cls.endpoints:
                endpoints = copy.copy(cls.endpoints)
                random.shuffle(endpoints)
                return endpoints[0]

        @property
        def _alternative_random_endpoint(cls):
            endpoints = copy.copy(cls.endpoints)
            if cls.current_endpoint in endpoints:
                endpoints.remove(cls.current_endpoint)
            random.shuffle(endpoints)
            if endpoints:
                return endpoints[0]

        @property
        def _target_base_url(cls):
            if None in [cls.app_id, cls.app_api_key]:
                raise ArgumentError('%s %s' % (
                    CONFIGURATION_REQUIRED_TEXT, RELATED_DOCS_TEXT))
            if cls._config.target_base_url is None:
                basic_auth_part = '%s:%s@' % (cls.app_id, cls.app_api_key)
                if cls.current_endpoint:
                    cls._config.target_base_url = re.sub(
                        r'(https?:\/\/)(.*)',
                        '\g<1>%s\g<2>' % (basic_auth_part),
                        cls.current_endpoint)
            return cls._config.target_base_url

        @property
        def hostname(cls):
            return cls._config.hostname

        @hostname.setter
        def hostname(cls, value):
            cls._config.hostname = value
            cls.current_endpoint = None
            cls.endpoints = None

        @property
        def protocol(cls):
            return cls._config.protocol

        @protocol.setter
        def protocol(cls, value):
            cls._config.protocol = value
            cls.current_endpoint = None
            cls.endpoints = None

        @property
        def current_endpoint(cls):
            now = time.mktime(datetime.utcnow().timetuple())
            expired = cls._config.endpoint_randomized_at < (now - (60 * 5))
            if cls._config.endpoint_randomized_at is None or expired:
                cls._config.endpoint_randomized_at = now
                cls.current_endpoint = cls._random_endpoint
            return cls._config.current_endpoint

        @current_endpoint.setter
        def current_endpoint(cls, value):
            cls._config.current_endpoint = value
            cls._config.target_base_url = None

        @property
        def endpoints(cls):
            if not cls._config.endpoints:
                return ['%s://%s' % (cls.protocol, cls.hostname)]
            else:
                return cls._config.endpoints

        @endpoints.setter
        def endpoints(cls, value):
            cls._config.endpoints = value
            cls.current_endpoint = cls._random_endpoint

        @SetterProperty
        def endpoint(cls, value):
            cls.endpoints = [value]


class ResourceEncoder(JSONEncoder):
    def default(self, o):
        if hasattr(o, 'from_api'):
            # handle API resources
            return o.attributes
        return super(ResourceEncoder, self).default(o)
