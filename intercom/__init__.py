#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#
""" Intercom API wrapper. """

import functools
import json
import numbers
import os
import requests
import sys
import time

from datetime import datetime

ENDPOINT = 'https://api.intercom.io/'
ENV = os.environ
DEFAULT_TIMEOUT = 10 # seconds

ENV_APP_ID = 'INTERCOM_APP_ID'
ENV_API_KEY = 'INTERCOM_API_KEY'
ENV_API_VERSION = '1'
ENV_TIMEOUT = 'INTERCOM_API_TIMEOUT'

class IntercomError(StandardError):
    def __init__(self, message, result=None):
        super(StandardError, self).__init__(message)
        self.result = result

class AuthConfigError(IntercomError):
    pass

class AuthError(IntercomError):
    pass

class NotFoundError(IntercomError):
    pass

class APIError(IntercomError):
    pass

def api_call(func_to_decorate):
    """ Decorator for handling AWS credentials. """
    @functools.wraps(func_to_decorate)
    def wrapper(*args, **kwargs):
        """ Decorator closure. """
        response = func_to_decorate(*args, **kwargs)
        if response.status_code == 401:
            raise AuthError("Invalid API key/username provided.")
        result = json.loads(response.content)
#        print json.dumps(result, indent=4)
        if response.status_code in (200, 201):
            pass
        else:
            message = result['error']['message']
            if response.status_code == 404:
                raise NotFoundError(message, result)
            else:
                raise APIError(message, result)
        return result
    return wrapper

def check_auth_params(func_to_decorate):
    """ Decorator for checking authentication parameters are valid. """
    @functools.wraps(func_to_decorate)
    def wrapper(*args, **kwargs):
        """ Decorator closure. """

        # no user_id or email
        if 'email' not in kwargs and 'user_id' not in kwargs:
            raise ValueError("An email address or a user_id must be present.")

        # a user_id and an email
        if 'email' in kwargs and kwargs['email'] and 'user_id' in kwargs and kwargs['user_id']:
            raise ValueError("An email address and a user_id cannot be present.")
        return func_to_decorate(*args, **kwargs)
    return wrapper

class Intercom(object):
    """ Intercom API Wrapper """

    app_id = None
    api_key = None

    def __init__(self):
        """ Initialise the wrapper.

        If a username is not specified, the environment variable
        INTERCOM_API_USER is used. If neither are specified, an
        AuthConfigError is raised.

        If an api_key is not specified, the environment variable
        INTERCOM_API_KEY is used. If neither are specified, an
        AuthConfigError is raised.
        """
        if Intercom.app_id is None:
            if ENV_APP_ID in ENV:
                Intercom.app_id = ENV[ENV_APP_ID]
            else:
                raise AuthConfigError("No username available.")
        if Intercom.api_key is None:
            if ENV_API_KEY in ENV:
                Intercom.api_key = ENV[ENV_API_KEY]
            else:
                raise AuthConfigError("No API key available.")
        self._api_version = ENV.get(ENV_API_VERSION, '1')
        self._api_endpoint = ENDPOINT + 'v' + self._api_version + '/'
        self._timeout = ENV.get(ENV_TIMEOUT, DEFAULT_TIMEOUT)

    @api_call
    def _call(self, method, url, params=None):
        req_params = {}
        headers = { 'User-Agent': 'python-intercom/0.1' }
        if method in ('POST', 'PUT'):
            headers['content-type'] = 'application/json'
            req_params['data'] = json.dumps(params)
        elif method == 'GET':
            req_params['params'] = params
        req_params['headers'] = headers

        resp = requests.request(method, url, timeout=self._timeout, \
                auth=(Intercom.app_id, Intercom.api_key), config={'verbose': sys.stderr}, **req_params)
        return resp

    def _create_or_update_user(self, method, **kwargs):
        """ Used by create_user and update_user. """
        user_dict = self._call(method, self._api_endpoint + 'users', params=kwargs)
        return user_dict

    def get_users(self):
        """ Return a dict for the user represented by the specified
        email or user_id. """
        user_dict = self._call('GET', '%susers' % (self._api_endpoint))
        return user_dict

    @check_auth_params
    def get_user(self, email=None, user_id=None):
        """ Return a dict for the user represented by the specified
        email or user_id. """

        params = { 'email': email, 'user_id': user_id }
        user_dict = self._call('GET', '%susers' % (self._api_endpoint), params=params)
        return user_dict

    @check_auth_params
    def create_user(self, user_id=None, email=None, name=None, created_at=None, 
            custom_data=None, last_seen_ip=None, last_seen_user_agent=None):
        """ Create a user. """
        return self._create_or_update_user('POST', user_id=user_id, email=email, 
            name=name, created_at=created_at, custom_data=custom_data, 
            last_seen_ip=last_seen_ip, last_seen_user_agent=last_seen_user_agent)

    @check_auth_params
    def update_user(self, user_id=None, email=None, name=None, created_at=None, 
            custom_data=None, last_seen_ip=None, last_seen_user_agent=None):
        """ Update a user. """
        return self._create_or_update_user('PUT', user_id=user_id, email=email,
            name=name, created_at=created_at, custom_data=custom_data, 
            last_seen_ip=last_seen_ip, last_seen_user_agent=last_seen_user_agent)

    @check_auth_params
    def create_impression(self, user_id=None, email=None, user_ip=None,
        user_agent=None):
        """ Create an impression. """
        params = { 'email': email, 'user_id': user_id, 'user_ip': user_ip, 
                'user_agent': user_agent }
        user_dict = self._call('POST', self._api_endpoint + 'users/impressions', params=params)        
        return user_dict

    @check_auth_params
    def get_message_threads(self, user_id=None, email=None, thread_id=None):
        params = { 'email': email, 'user_id': user_id }
        msg_dict = self._call('GET', self._api_endpoint + 'users/message_threads', params=params)        
        return msg_dict

    @check_auth_params
    def create_message_thread(self, user_id=None, email=None, body=None):
        """ Create an impression. """
        params = { 'email': email, 'user_id': user_id, 'body': body }
        user_dict = self._call('POST', self._api_endpoint + 'users/message_threads', params=params)        
        return user_dict

    @check_auth_params
    def reply_message_thread(self, user_id=None, email=None, thread_id=None, 
            body=None, read=None):
        """ Create an impression. """
        params = { 'email': email, 'user_id': user_id, 'thread_id': thread_id, 
            'body': body, 'read': read }
        user_dict = self._call('PUT', self._api_endpoint + 'users/message_threads', params=params)
        return user_dict

def from_timestamp_property(func_to_decorate):
    @functools.wraps(func_to_decorate)
    def wrapper(instance):
        value = func_to_decorate(instance)
        return datetime.fromtimestamp(value)
    return wrapper

def to_timestamp_property(func_to_decorate):
    @functools.wraps(func_to_decorate)
    def wrapper(instance, value):
        value = time.mktime(value.timetuple())
        func_to_decorate(instance, value)
    return wrapper

class UserId(dict):

    @property
    def user_id(self):
        return dict.get(self, 'user_id', None)

    @user_id.setter
    def user_id(self, user_id):
        self['user_id'] = user_id

    @property
    def email(self):
        return dict.get(self, 'email', None)

    @email.setter
    def email(self, email):
        self['email'] = email

class User(UserId):
    attributes = ('user_id', 'email', 'name', 'created_at', 'custom_data',
            'last_seen_ip', 'last_seen_user_agent')

    _custom_data = None

    @classmethod
    def find(cls, user_id=None, email=None):
        resp = Intercom().get_user(user_id=user_id, email=email)
        return cls(resp)

    @classmethod
    def find_by_email(cls, email):
        resp = Intercom().get_user(email=email)
        return cls(resp)

    @classmethod
    def find_by_user_id(cls, user_id):
        resp = Intercom().get_user(user_id=user_id)
        return cls(resp)

    @classmethod
    def create(cls, user_id=None, email=None, name=None, created_at=None, 
            custom_data=None, last_seen_ip=None, last_seen_user_agent=None):

        resp = Intercom().create_user(user_id=user_id, email=email, name=name, 
                created_at=created_at, custom_data=custom_data, 
                last_seen_ip=last_seen_ip, last_seen_user_agent=last_seen_user_agent)
        return cls(resp)

    @classmethod
    def all(cls):
        resp = Intercom().get_users()
        return [cls(u) for u in resp['users']]


    def save(self):
        attrs = { key: dict.get(self, key) for key in User.attributes }
        resp = Intercom().update_user(**attrs)
        self.__dict__.update(resp)

    @property
    def name(self):
        return dict.get(self, 'name', None)

    @name.setter
    def name(self, name):
        self['name'] = name

    @property
    def last_seen_ip(self):
        return dict.get(self, 'last_seen_ip', None)

    @last_seen_ip.setter
    def last_seen_ip(self, last_seen_ip):
        self['last_seen_ip'] = last_seen_ip

    @property
    def last_seen_user_agent(self):
        return dict.get(self, 'last_seen_user_agent', None)

    @last_seen_user_agent.setter
    def last_seen_user_agent(self, last_seen_user_agent):
        self['last_seen_user_agent'] = last_seen_user_agent

    @property
    def relationship_score(self):
        return dict.get(self, 'relationship_score', None)

    @property
    def session_count(self):
        return dict.get(self, 'session_count', None)

    @property
    @from_timestamp_property
    def last_impression_at(self):
        return dict.get(self, 'last_impression_at', None)

    @property
    @from_timestamp_property
    def created_at(self):
        return dict.get(self, 'created_at', None)

    @created_at.setter
    @to_timestamp_property
    def created_at(self, value):
        self['created_at'] = value

    @property
    def social_profiles(self):
        profiles = dict.get(self, 'social_profiles', None)
        if profiles:
            return [SocialProfile(**p) for p in profiles]

    @property
    def location_data(self):
        return dict.get(self, 'location_data', None)

    @property
    def custom_data(self):
        data = dict.get(self, 'custom_data', None)
        if not isinstance(data, CustomData):
            data = CustomData(data)
            dict.__setitem__(self, 'custom_data', data)
        return data

    @custom_data.setter
    def custom_data(self, custom_data):
        if not isinstance(custom_data, CustomData):
            custom_data = CustomData(custom_data)
        self['custom_data'] = custom_data


class Impression(UserId):

    @classmethod
    def create(cls, user_id=None, email=None, user_ip=None, user_agent=None):
        resp = Intercom().create_impression(user_id=user_id, email=email, 
            user_ip=user_ip, user_agent=user_agent)
        return cls(resp)

    def save(self):
        print "Impression save..."
        print_dict(**self)
        resp = Intercom().create_impression(**self)
        self.update(resp)

    @property
    def user_ip(self):
        return dict.get(self, 'user_ip', None)

    @user_ip.setter
    def user_ip(self, user_ip):
        self['user_ip'] = user_ip

    @property
    def location(self):
        return dict.get(self, 'location', None)

    @location.setter
    def location(self, location):
        self['location'] = location

    @property
    def user_agent(self):
        return dict.get(self, 'user_agent', None)

    @user_agent.setter
    def user_agent(self, user_agent):
        self['user_agent'] = user_agent

    @property
    def unread_messages(self):
        return dict.get(self, 'unread_messages', None)

class MessageThread(dict):
    _get = dict.get

    @classmethod
    def find(cls, user_id=None, email=None, thread_id=None):
        resp = Intercom().get_message_threads(user_id=user_id, email=email, 
                thread_id=thread_id)
        return [cls(mt) for mt in resp]

    @classmethod
    def find_all(cls, user_id=None, email=None):
        resp = Intercom().get_message_threads(user_id=user_id, email=email)
        return [cls(mt) for mt in resp]

    @classmethod
    def create(cls, user_id=None, email=None, body=None):
        resp = Intercom().create_message_thread(user_id=user_id, email=email, 
                body=body)
        return cls(resp)

    @classmethod
    def reply(cls, user_id=None, email=None, thread_id=None, 
            body=None, read=None):
        resp = Intercom().reply_message_thread(user_id=user_id, email=email, 
                thread_id=thread_id, read=None, body=body)
        return cls(resp)

    @property
    @from_timestamp_property
    def updated_at(self):
        return dict.get(self, 'updated_at', None)

    @property
    @from_timestamp_property
    def created_at(self):
        return dict.get(self, 'created_at', None)

    @property
    def body(self):
        return dict.get(self, 'body', None)

    @property
    def thread_id(self):
        return dict.get(self, 'thread_id', None)

    @thread_id.setter
    def thread_id(self, value):
        self['thread_id'] = value

    @property
    def read(self):
        return dict.get(self, 'read', None)

    @thread_id.setter
    def read(self, value):
        self['read'] = value

    @property
    def messages(self):
        messages = dict.get(self, 'messages', None)
        if messages:
            return [Message(m) for m in messages]

class Message(dict):

    @property
    def author(self):
        _from = self.get('from', None)
        if _from:
            return MessageAuthor(_from)

    @property
    def html(self):
        return dict.get(self, 'html', None)

    @property
    def created_at(self):
        return dict.get(self, 'created_at', None)

class MessageAuthor(dict):

    @property
    def admin(self):
        return dict.get(self, 'admin', None)

    @property
    def email(self):
        return dict.get(self, 'email', None)

    @property
    def user_id(self):
        return dict.get(self, 'user_id', None)

    @property
    def avatar_path_50(self):
        return dict.get(self, 'avatar_path_50', None)

    @property
    def name(self):
        return dict.get(self, 'name', None)

class CustomData(dict):

    def __setitem__(self, key, value):
        if not (isinstance(value, numbers.Number) or isinstance(value, basestring)):
            raise ValueError("custom data only allows non-nested values")
        if not isinstance(key, basestring):
            raise ValueError("custom data only allows string keys")
        super(CustomData, self).__setitem__(key, value)

class SocialProfile(object):

    def __init__(self, **kwargs):
        self._type = kwargs.get('type', None)
        self._id = kwargs.get('id', None)
        self._url = kwargs.get('url', None)
        self._username = kwargs.get('username', None)

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id

    @property
    def url(self):
        return self._url

    @property
    def username(self):
        return self._username
