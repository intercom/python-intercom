# -*- coding: utf-8 -*-

from datetime import datetime
from .errors import (ArgumentError, AuthenticationError, # noqa
    BadGatewayError, BadRequestError, HttpError, IntercomError,
    MultipleMatchingUsersError, RateLimitExceeded, ResourceNotFound,
    ServerError, ServiceUnavailableError, UnexpectedError)
from .lib.setter_property import SetterProperty
from .request import Request
from .admin import Admin  # noqa
from .company import Company  # noqa
from .count import Count  # noqa
from .conversation import Conversation  # noqa
from .event import Event  # noqa
from .message import Message  # noqa
from .note import Note  # noqa
from .notification import Notification  # noqa
from .user import User  # noqa
from .segment import Segment  # noqa
from .subscription import Subscription  # noqa
from .tag import Tag  # noqa

import copy
import random
import re
import six
import time

__version__ = '2.1.1'


RELATED_DOCS_TEXT = "See https://github.com/jkeyes/python-intercom \
for usage examples."
COMPATIBILITY_WARNING_TEXT = "It looks like you are upgrading from \
an older version of python-intercom. Please note that this new version \
(%s) is not backwards compatible." % (__version__)
COMPATIBILITY_WORKAROUND_TEXT = "To get rid of this error please set \
Intercom.app_api_key and don't set Intercom.api_key."
CONFIGURATION_REQUIRED_TEXT = "You must set both Intercom.app_id and \
Intercom.app_api_key to use this client."


class IntercomType(type):  # noqa

    app_id = None
    app_api_key = None
    _hostname = "api.intercom.io"
    _protocol = "https"
    _endpoints = None
    _current_endpoint = None
    _target_base_url = None
    _endpoint_randomized_at = 0
    _rate_limit_details = {}

    @property
    def _auth(self):
        return (self.app_id, self.app_api_key)

    @property
    def _random_endpoint(self):
        if self.endpoints:
            endpoints = copy.copy(self.endpoints)
            random.shuffle(endpoints)
            return endpoints[0]

    @property
    def _alternative_random_endpoint(self):
        endpoints = copy.copy(self.endpoints)
        if self.current_endpoint in endpoints:
            endpoints.remove(self.current_endpoint)
        random.shuffle(endpoints)
        if endpoints:
            return endpoints[0]

    @property
    def target_base_url(self):
        if None in [self.app_id, self.app_api_key]:
            raise ArgumentError('%s %s' % (
                CONFIGURATION_REQUIRED_TEXT, RELATED_DOCS_TEXT))
        if self._target_base_url is None:
            basic_auth_part = '%s:%s@' % (self.app_id, self.app_api_key)
            if self.current_endpoint:
                self._target_base_url = re.sub(
                    r'(https?:\/\/)(.*)',
                    '\g<1>%s\g<2>' % (basic_auth_part),
                    self.current_endpoint)
        return self._target_base_url

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, value):
        self._hostname = value
        self.current_endpoint = None
        self.endpoints = None

    @property
    def rate_limit_details(self):
        return self._rate_limit_details

    @rate_limit_details.setter
    def rate_limit_details(self, value):
        self._rate_limit_details = value

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        self._protocol = value
        self.current_endpoint = None
        self.endpoints = None

    @property
    def current_endpoint(self):
        now = time.mktime(datetime.utcnow().timetuple())
        expired = self._endpoint_randomized_at < (now - (60 * 5))
        if self._endpoint_randomized_at is None or expired:
            self._endpoint_randomized_at = now
            self._current_endpoint = self._random_endpoint
        return self._current_endpoint

    @current_endpoint.setter
    def current_endpoint(self, value):
        self._current_endpoint = value
        self._target_base_url = None

    @property
    def endpoints(self):
        if not self._endpoints:
            return ['%s://%s' % (self.protocol, self.hostname)]
        else:
            return self._endpoints

    @endpoints.setter
    def endpoints(self, value):
        self._endpoints = value
        self.current_endpoint = self._random_endpoint

    @SetterProperty
    def endpoint(self, value):
        self.endpoints = [value]


@six.add_metaclass(IntercomType)
class Intercom(object):
    _class_register = {}

    @classmethod
    def get_url(cls, path):
        if '://' in path:
            url = path
        else:
            url = cls.current_endpoint + path
        return url

    @classmethod
    def request(cls, method, path, params):
        return Request.send_request_to_path(
            method, cls.get_url(path), cls._auth, params)

    @classmethod
    def get(cls, path, **params):
        return cls.request('GET', path, params)

    @classmethod
    def post(cls, path, **params):
        return cls.request('POST', path, params)

    @classmethod
    def put(cls, path, **params):
        return cls.request('PUT', path, params)

    @classmethod
    def delete(cls, path, **params):
        return cls.request('DELETE', path, params)
