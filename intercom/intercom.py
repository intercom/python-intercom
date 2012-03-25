#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import functools
import json
import requests
import sys

DEFAULT_TIMEOUT = 10 # seconds

class IntercomError(StandardError):
    def __init__(self, message, result=None):
        super(IntercomError, self).__init__(message)
        self.result = result

class AuthenticationError(IntercomError):
    pass

class ResourceNotFound(IntercomError):
    pass

class ServerError(IntercomError):
    pass

def api_call(func_to_decorate):
    """ Decorator for handling AWS credentials. """
    @functools.wraps(func_to_decorate)
    def wrapper(*args, **kwargs):
        """ Decorator closure. """
        response = func_to_decorate(*args, **kwargs)
        if response.status_code == 401:
            raise AuthenticationError("Invalid API key/username provided.")
        result = json.loads(response.content)
        if response.status_code in (200, 201):
            pass
        else:
            message = result['error']['message']
            if response.status_code == 404:
                raise ResourceNotFound(message, result)
            else:
                raise ServerError(message, result)
        return result
    return wrapper

class Intercom(object):
    """ Intercom API Wrapper """

    app_id = None
    api_key = None
    api_version = 1
    api_endpoint = 'https://api.intercom.io/v' + str(api_version) + '/'
    timeout = DEFAULT_TIMEOUT

    @classmethod
    @api_call
    def _call(cls, method, url, params=None):
        req_params = {}
        headers = { 'User-Agent': 'python-intercom/0.1', 'Accept': 'application/json' }
        if method in ('POST', 'PUT'):
            headers['content-type'] = 'application/json'
            req_params['data'] = json.dumps(params)
        elif method == 'GET':
            req_params['params'] = params
        req_params['headers'] = headers

        resp = requests.request(method, url, timeout=Intercom.timeout, \
                auth=(Intercom.app_id, Intercom.api_key), 
                **req_params)
        return resp

    @classmethod
    def _create_or_update_user(cls, method, **kwargs):
        """ Used by create_user and update_user. """
        user_dict = Intercom._call(method, Intercom.api_endpoint + 'users', 
                params=kwargs)
        return user_dict

    @classmethod
    def get_users(cls):
        """ Return a dict for the user represented by the specified
        email or user_id. """
        user_dict = Intercom._call('GET', '%susers' % (Intercom.api_endpoint))
        return user_dict

    @classmethod
    def get_user(cls, email=None, user_id=None):
        """ Return a dict for the user represented by the specified
        email or user_id. """

        params = { 'email': email, 'user_id': user_id }
        user_dict = Intercom._call('GET', '%susers' % (Intercom.api_endpoint), params=params)
        return user_dict

    @classmethod
    def create_user(cls, user_id=None, email=None, name=None, created_at=None, 
            custom_data=None, last_seen_ip=None, last_seen_user_agent=None):
        """ Create a user. """
        return Intercom._create_or_update_user('POST', user_id=user_id, email=email, 
            name=name, created_at=created_at, custom_data=custom_data, 
            last_seen_ip=last_seen_ip, last_seen_user_agent=last_seen_user_agent)

    @classmethod
    def update_user(cls, user_id=None, email=None, name=None, created_at=None, 
            custom_data=None, last_seen_ip=None, last_seen_user_agent=None):
        """ Update a user. """
        return Intercom._create_or_update_user('PUT', user_id=user_id, email=email,
            name=name, created_at=created_at, custom_data=custom_data, 
            last_seen_ip=last_seen_ip, last_seen_user_agent=last_seen_user_agent)

    @classmethod
    def create_impression(cls, user_id=None, email=None, user_ip=None,
        user_agent=None, location=None):
        """ Create an impression. """
        params = { 'email': email, 'user_id': user_id, 'user_ip': user_ip, 
                'user_agent': user_agent, 'location': location }
        user_dict = Intercom._call('POST', Intercom.api_endpoint + 'users/impressions', 
                params=params)
        return user_dict

    @classmethod
    def get_message_threads(cls, user_id=None, email=None, thread_id=None):
        params = { 'email': email, 'user_id': user_id }
        msg_dict = Intercom._call('GET', Intercom.api_endpoint + 'users/message_threads', 
                params=params)        
        return msg_dict

    @classmethod
    def create_message_thread(cls, user_id=None, email=None, body=None):
        """ Create an impression. """
        params = { 'email': email, 'user_id': user_id, 'body': body }
        user_dict = Intercom._call('POST', Intercom.api_endpoint + 'users/message_threads', 
                params=params)        
        return user_dict

    @classmethod
    def reply_message_thread(cls, user_id=None, email=None, thread_id=None, 
            body=None, read=None):
        """ Create an impression. """
        params = { 'email': email, 'user_id': user_id, 'thread_id': thread_id, 
            'body': body, 'read': read }
        user_dict = Intercom._call('PUT', Intercom.api_endpoint + 'users/message_threads', 
                params=params)
        return user_dict
