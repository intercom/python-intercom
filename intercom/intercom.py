# coding=utf-8
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

__version__ = '0.2.10'

import functools
import json
import requests

DEFAULT_TIMEOUT = 10  # seconds


class IntercomError(Exception):
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
    """ Raised when the API returns an error other than an auth or not found.
    """
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
        """ Construct an API request, send it to the API, and parse the
        response. """
        req_params = {}
        headers = {
            'User-Agent': 'python-intercom/' + __version__,
            'Accept': 'application/json'
        }
        if method in ('POST', 'PUT', 'DELETE'):
            headers['content-type'] = 'application/json'
            req_params['data'] = json.dumps(params)
        elif method == 'GET':
            req_params['params'] = params
        req_params['headers'] = headers

        resp = requests.request(
            method, url, timeout=Intercom.timeout,
            auth=(Intercom.app_id, Intercom.api_key), **req_params)
        return resp

    @classmethod
    def _create_or_update_user(cls, method, **kwargs):
        """ Used by create_user and update_user. """
        user_dict = Intercom._call(
            method, Intercom.api_endpoint + 'users', params=kwargs)
        return user_dict

    @classmethod
    def get_users(cls, **kwargs):
        """ Returns a paginated list of all users in your application on Intercom.

        **Arguments**

        * ``page``: optional (defaults to 1)
        * ``per_page``: optional (defaults to 500, max value of 500)
        * ``tag_id``: optional — query for users that are tagged with a specific tag.
        * ``tag_name``: optional — query for users that are tagged with a specific tag.

        **Response**

        * ``users``: an array of User objects (same as returned by getting a single User)
        * ``total_count``: the total number of Users tracked in your Intercom application
        * ``page``: the current requested page
        * ``next_page``: the next page number, if any
        * ``previous_page``: the previous page number, if any
        * ``total_pages``: the total number of pages

        >>> result = Intercom.get_users()
        >>> type(result)
        <type 'dict'>
        >>> len(result['users'])
        3

        """
        return Intercom._call('GET', Intercom.api_endpoint + 'users', params=kwargs)

    @classmethod
    def get_user(cls, email=None, user_id=None):
        """ Return a dict for the user represented by the specified email
        or user_id.

        >>> user = Intercom.get_user(user_id='123')
        >>> user['name']
        u'Bob'

        """

        params = {'email': email, 'user_id': user_id}
        user_dict = Intercom._call(
            'GET', Intercom.api_endpoint + 'users', params=params)
        return user_dict

    @classmethod
    def create_user(cls, **kwargs):
        """ Creates a user.

        N.B. Social and geo location data is fetched asynchronously, so a
        secondary call to users will be required to fetch it.

        **Arguments**

        - ``user_id``: required (if no email) — a unique string identifier
          for the user
        - ``email``: required (if no user_id) — the user's email address
        - ``name``: The user's full name
        - ``created_at``: A UNIX timestamp representing the date the user was
          created
        - ``custom_data``: A hash of key/value pairs containing any other data
          about the user you want Intercom to store.
        - ``last_seen_ip``: An ip address (e.g. "1.2.3.4") representing the
          last ip address the user visited your application from. (Used for
          updating location_data)
        - ``last_seen_user_agent``: The user agent the user last visited your
          application with.
        - ``companies``: An array of hashes describing the companies this user
          belongs to. Currently companies are not returned in the response.
        - ``last_request_at or last_impression_at``: A UNIX timestamp
          representing the date the user last visited your application.
        - ``unsubscribed_from_emails``: A boolean value representing the users
          unsubscribed status.


        >>> from datetime import datetime
        >>> import time
        >>> now = time.mktime(datetime.now().timetuple())
        >>> user = Intercom.create_user(user_id='7902', email='ben@intercom.io',
        ... name='Ben McRedmond', created_at=now, last_seen_ip='1.2.3.4',
        ... custom_data={ 'plan': 'pro'}, last_request_at=1300000000)
        >>> user['name']
        u'Ben McRedmond'
        >>> user['custom_data']['plan']
        u'pro'
        >>> user['last_impression_at']
        1300000000

        """
        return Intercom._create_or_update_user('POST', **kwargs)

    @classmethod
    def update_user(cls, **kwargs):
        """ Update a user with the available parameters.

        >>> user = Intercom.get_user(user_id='123')
        >>> user['name']
        u'Bob'
        >>> user = Intercom.update_user(user_id='123', name='Han')
        >>> user['name']
        u'Han'

        """
        return Intercom._create_or_update_user('PUT', **kwargs)

    @classmethod
    def delete_user(cls, user_id=None, email=None):
        """ Delete a user.

        >>> user = Intercom.get_user(user_id='7902')
        >>> user['email']
        u'bob@example.com'

        """
        params = {
            'email': email,
            'user_id': user_id
        }
        user_dict = Intercom._call(
            'DELETE', Intercom.api_endpoint + 'users', params)
        return user_dict

    @classmethod
    def create_impression(
            cls, user_id=None, email=None, user_ip=None,
            user_agent=None, location=None):
        """ Create an impression.

        >>> result = Intercom.create_impression(email="somebody@example.com",
        ... user_agent="MyApp/1.0", user_ip="2.3.4.5")
        >>> result['unread_messages']
        1

        """
        params = {
            'email': email,
            'user_id': user_id,
            'user_ip': user_ip,
            'user_agent': user_agent,
            'location': location
        }
        user_dict = Intercom._call(
            'POST', Intercom.api_endpoint + 'users/impressions', params=params)
        return user_dict

    @classmethod
    def create_note(cls, user_id=None, email=None, body=None):
        """ Create a note.

        >>> result = Intercom.create_note(email="somebody@example.com",
        ... body="This is the text of my note.")
        >>> result['html']
        u'<p>This is the text of my note.</p>'
        >>> result['user']['email']
        u'somebody@example.com'

        """
        params = {
            'email': email,
            'user_id': user_id,
            'body': body
        }
        user_dict = Intercom._call(
            'POST', Intercom.api_endpoint + 'users/notes', params=params)
        return user_dict

    @classmethod
    def get_message_threads(cls, user_id=None, email=None, thread_id=None):
        """ If a thread_id is specified, this returns a specific MessageThread
        (if it can find one), otherwise it returns all MessageThreads for the
        particular user.

        >>> message_threads = Intercom.get_message_threads(
        ... email="somebody@example.com")
        >>> type(message_threads)
        <type 'list'>
        >>> message_thread = Intercom.get_message_threads(
        ... email="somebody@example.com", thread_id=5591)
        >>> type(message_thread)
        <type 'dict'>

        """
        params = {
            'email': email,
            'user_id': user_id,
            'thread_id': thread_id
        }
        msg_dict = Intercom._call(
            'GET', Intercom.api_endpoint + 'users/message_threads',
            params=params)
        return msg_dict

    @classmethod
    def create_message_thread(cls, user_id=None, email=None, body=None):
        """ Create a MessageThread.

        >>> message_thread = Intercom.create_message_thread(
        ... email="somebody@example.com",
        ... body="Uh, everything's under control. Situation normal.")
        >>> message_thread['thread_id']
        5591
        >>> len(message_thread['messages'])
        1
        >>> message_thread['messages'][0]['html']
        u"<p>Uh, everything's under control. Situation normal.</p>"

        """
        params = {
            'email': email,
            'user_id': user_id,
            'body': body
        }
        user_dict = Intercom._call(
            'POST', Intercom.api_endpoint + 'users/message_threads',
            params=params)
        return user_dict

    @classmethod
    def reply_message_thread(
            cls, user_id=None, email=None, thread_id=None, body=None,
            read=None):
        """ Reply to the specific thread.

        >>> message_thread = Intercom.reply_message_thread(
        ... email="somebody@example.com",
        ... thread_id=5591,
        ... body="If you're not talking to me you must be talking to someone")
        >>> len(message_thread)
        9
        >>> message_thread['thread_id']
        5591
        >>> len(message_thread['messages'])
        3

        """
        params = {
            'email': email,
            'user_id': user_id,
            'thread_id': thread_id,
            'body': body,
            'read': read
        }
        user_dict = Intercom._call(
            'PUT', Intercom.api_endpoint + 'users/message_threads',
            params=params)
        return user_dict

    @classmethod
    def create_tag(
            cls, name, tag_or_untag, user_ids=None, emails=None):
        """ Create a tag (and maybe tag users).

        >>> tag = Intercom.create_tag("Free Trial", "tag",
        ... user_ids=["abc123", "def456"])
        >>> tag['id'] != None
        True
        >>> tag['name']
        u'Free Trial'
        >>> tag['tagged_user_count']
        2

        """

        params = {
            'name': name,
            'tag_or_untag': tag_or_untag,
            'user_ids': user_ids,
            'emails': emails
        }
        tag_dict = Intercom._call(
            'POST', Intercom.api_endpoint + 'tags', params=params)
        return tag_dict

    @classmethod
    def update_tag(
            cls, name, tag_or_untag, user_ids=None, emails=None):
        """ Update a tag (and maybe tag users).

        >>> tag = Intercom.update_tag("Free Trial", "tag",
        ... user_ids=["abc123", "def456"])
        >>> tag['id'] != None
        True
        >>> tag['name']
        u'Free Trial'
        >>> tag['tagged_user_count']
        2

        """

        params = {
            'name': name,
            'tag_or_untag': tag_or_untag,
            'user_ids': user_ids,
            'emails': emails
        }
        tag_dict = Intercom._call(
            'PUT', Intercom.api_endpoint + 'tags', params=params)
        return tag_dict

    @classmethod
    def get_tag(cls, name=None):
        """ Return a dict for the tag by the specified name.

        >>> tag = Intercom.get_tag(name="Free Trial")
        >>> tag['id'] != None
        True
        >>> tag['name']
        u'Free Trial'
        >>> tag['tagged_user_count']
        2

        """

        params = {'name': name}
        tag_dict = Intercom._call(
            'GET', Intercom.api_endpoint + 'tags', params=params)
        return tag_dict
