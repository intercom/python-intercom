# -*- coding: utf-8 -*-

from datetime import datetime
from .errors import ArgumentError
from .errors import HttpError  # noqa
from .lib.setter_property import SetterProperty
from .request import Request
from .admin import Admin
from .company import Company
from .event import Event
from .message import Message
from .note import Note
from .notification import Notification
from .user import User
from .subscription import Subscription
from .tag import Tag

import copy
import random
import re
import time

__version__ = '2.0.alpha'

__all__ = (
    Admin, Company, Event, Message, Note, Notification, Subscription, Tag, User
)


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
    endpoint_randomized_at = None


class IntercomType(type):  # noqa

    @property
    def app_id(self):
        return self._config.app_id

    @app_id.setter
    def app_id(self, value):
        self._config.app_id = value

    @property
    def app_api_key(self):
        return self._config.app_api_key

    @app_api_key.setter
    def app_api_key(self, value):
        self._config.app_api_key = value

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
    def _target_base_url(self):
        if None in [self.app_id, self.app_api_key]:
            raise ArgumentError('%s %s' % (
                CONFIGURATION_REQUIRED_TEXT, RELATED_DOCS_TEXT))
        if self._config.target_base_url is None:
            basic_auth_part = '%s:%s@' % (self.app_id, self.app_api_key)
            if self.current_endpoint:
                self._config.target_base_url = re.sub(
                    r'(https?:\/\/)(.*)',
                    '\g<1>%s\g<2>' % (basic_auth_part),
                    self.current_endpoint)
        return self._config.target_base_url

    @property
    def hostname(self):
        return self._config.hostname

    @hostname.setter
    def hostname(self, value):
        self._config.hostname = value
        self.current_endpoint = None
        self.endpoints = None

    @property
    def protocol(self):
        return self._config.protocol

    @protocol.setter
    def protocol(self, value):
        self._config.protocol = value
        self.current_endpoint = None
        self.endpoints = None

    @property
    def current_endpoint(self):
        now = time.mktime(datetime.utcnow().timetuple())
        expired = self._config.endpoint_randomized_at < (now - (60 * 5))
        if self._config.endpoint_randomized_at is None or expired:
            self._config.endpoint_randomized_at = now
            self.current_endpoint = self._random_endpoint
        return self._config.current_endpoint

    @current_endpoint.setter
    def current_endpoint(self, value):
        self._config.current_endpoint = value
        self._config.target_base_url = None

    @property
    def endpoints(self):
        if not self._config.endpoints:
            return ['%s://%s' % (self.protocol, self.hostname)]
        else:
            return self._config.endpoints

    @endpoints.setter
    def endpoints(self, value):
        self._config.endpoints = value
        self.current_endpoint = self._random_endpoint

    @SetterProperty
    def endpoint(self, value):
        self.endpoints = [value]


class Intercom(object):
    _config = _Config()
    _class_register = {}
    __metaclass__ = IntercomType

    @classmethod
    def get_url(cls, path):
        if '://' in path:
            url = path
        else:
            url = cls.current_endpoint + path
        return url

    @classmethod
    def get(cls, path, **params):
        return Request.send_request_to_path('GET', cls.get_url(path), cls._auth, params)

    @classmethod
    def post(cls, path, **params):
        return Request.send_request_to_path('POST', cls.get_url(path), cls._auth, params)

    @classmethod
    def put(cls, path, **params):
        return Request.send_request_to_path('PUT', cls.get_url(path), cls._auth, params)

    @classmethod
    def delete(cls, path, **params):
        return Request.send_request_to_path('DELETE', cls.get_url(path), cls._auth, params)
