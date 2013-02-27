#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#
""" intercom module

All of the API requests are created, and the API responses are parsed here.

>>> from intercom import Intercom
>>> Intercom.app_id = 'dummy-app-id'
>>> Intercom.api_key = 'dummy-api-key'

"""

import functools
import json
import requests

DEFAULT_TIMEOUT = 10 # seconds

class IntercomError(StandardError):
    """ Base error. """
    def __init__(self, message, result=None):
        super(IntercomError, self).__init__(message)
        self.result = result

class AuthenticationError(IntercomError):
    """ Raised when a request cannot be authenticated by the API. """
    pass

class ResourceNotFound(IntercomError):
    """ Raised when a resource cannot be found e.g. a non-existant User. """
    pass

class ServerError(IntercomError):
    """ Raised when the API returns an error other than an auth or not found. """
    pass

def api_call(func_to_decorate):
    """ Decorator for handling AWS credentials. """
    @functools.wraps(func_to_decorate)
    def wrapper(*args, **kwargs):
        """ Decorator closure. """
        response = func_to_decorate(*args, **kwargs)
        if response.status_code == 401:
            raise AuthenticationError("Invalid API key/username provided.")
        try:
            result = json.loads(response.content)
        except ValueError as err:
            raise ServerError(err.message)
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
        """ Construct an API request, send it to the API, and parse the response. """
        req_params = {}
        headers = { 'User-Agent': 'python-intercom/0.2.5', 'Accept': 'application/json' }
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
        """ Return a dict for the user represented by the specified email or user_id.

        >>> result = Intercom.get_users()
        >>> type(result)
        <type 'dict'>
        >>> len(result['users'])
        3

        """
        user_dict = Intercom._call('GET', '%susers' % (Intercom.api_endpoint))
        return user_dict

    @classmethod
    def get_user(cls, email=None, user_id=None):
        """ Return a dict for the user represented by the specified email or user_id.

        >>> user = Intercom.get_user(user_id='123')
        >>> user['name']
        u'Bob'

        """

        params = { 'email': email, 'user_id': user_id }
        user_dict = Intercom._call('GET', '%susers' % (Intercom.api_endpoint), params=params)
        return user_dict

    @classmethod
    def create_user(cls, user_id=None, email=None, name=None, created_at=None,
            custom_data=None, last_seen_ip=None, last_seen_user_agent=None):
        """ Create a user from the available parameters.

        >>> from datetime import datetime
        >>> import time
        >>> now = time.mktime(datetime.now().timetuple())
        >>> user = Intercom.create_user(user_id='987', email='joe@example.com',
        ... name='Joe Example', created_at=now, last_seen_ip='10.10.10.10',
        ... custom_data={ 'job_type': 'smuggler'})
        >>> user['name']
        u'Joe Example'
        >>> user['custom_data']['job_type']
        u'smuggler'

        """
        return Intercom._create_or_update_user('POST', user_id=user_id, email=email,
            name=name, created_at=created_at, custom_data=custom_data,
            last_seen_ip=last_seen_ip, last_seen_user_agent=last_seen_user_agent)

    @classmethod
    def update_user(cls, user_id=None, email=None, name=None, created_at=None,
            custom_data=None, last_seen_ip=None, last_seen_user_agent=None):
        """ Update a user with the available parameters.

        >>> user = Intercom.get_user(user_id='123')
        >>> user['name']
        u'Bob'
        >>> user = Intercom.update_user(user_id='123', name='Han')
        >>> user['name']
        u'Han'

        """
        return Intercom._create_or_update_user('PUT', user_id=user_id, email=email,
            name=name, created_at=created_at, custom_data=custom_data,
            last_seen_ip=last_seen_ip, last_seen_user_agent=last_seen_user_agent)

    @classmethod
    def create_impression(cls, user_id=None, email=None, user_ip=None,
        user_agent=None, location=None):
        """ Create an impression.

        >>> result = Intercom.create_impression(email="somebody@example.com",
        ... user_agent="MyApp/1.0", user_ip="2.3.4.5")
        >>> result['unread_messages']
        1

        """
        params = { 'email': email, 'user_id': user_id, 'user_ip': user_ip,
                'user_agent': user_agent, 'location': location }
        user_dict = Intercom._call('POST', Intercom.api_endpoint + 'users/impressions',
                params=params)
        return user_dict

    @classmethod
    def get_message_threads(cls, user_id=None, email=None, thread_id=None):
        """ If a thread_id is specified, this returns a specific MessageThread
        (if it can find one), otherwise it returns all MessageThreads for the
        particular user.

        >>> message_threads = Intercom.get_message_threads(email="somebody@example.com")
        >>> type(message_threads)
        <type 'list'>
        >>> message_thread = Intercom.get_message_threads(email="somebody@example.com",
        ... thread_id=5591)
        >>> type(message_thread)
        <type 'dict'>

        """
        params = { 'email': email, 'user_id': user_id, 'thread_id': thread_id }
        msg_dict = Intercom._call('GET', Intercom.api_endpoint + 'users/message_threads',
                params=params)
        return msg_dict

    @classmethod
    def create_message_thread(cls, user_id=None, email=None, body=None):
        """ Create a MessageThread.

        >>> message_thread = Intercom.create_message_thread(email="somebody@example.com",
        ... body="Uh, everything's under control. Situation normal.")
        >>> message_thread['thread_id']
        5591
        >>> len(message_thread['messages'])
        1
        >>> message_thread['messages'][0]['html']
        u"<p>Uh, everything's under control. Situation normal.</p>"

        """
        params = { 'email': email, 'user_id': user_id, 'body': body }
        user_dict = Intercom._call('POST', Intercom.api_endpoint + 'users/message_threads',
                params=params)
        return user_dict

    @classmethod
    def reply_message_thread(cls, user_id=None, email=None, thread_id=None,
            body=None, read=None):
        """ Reply to the specific thread.

        >>> message_thread = Intercom.reply_message_thread(email="somebody@example.com",
        ... thread_id=5591, body="If you're not talking to me you must be talking to someone")
        >>> len(message_thread)
        6
        >>> message_thread['thread_id']
        5591
        >>> len(message_thread['messages'])
        2

        """
        params = { 'email': email, 'user_id': user_id, 'thread_id': thread_id,
            'body': body, 'read': read }
        user_dict = Intercom._call('PUT', Intercom.api_endpoint + 'users/message_threads',
                params=params)
        return user_dict
