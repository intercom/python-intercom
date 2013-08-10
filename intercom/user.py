# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#
""" User module.

>>> from intercom import Intercom
>>> Intercom.app_id = 'dummy-app-id'
>>> Intercom.api_key = 'dummy-api-key'
>>> from intercom import User

"""

from . import Intercom
from . import from_timestamp_property
from . import to_timestamp_property

import numbers


class UserId(dict):
    """ Base class for objects that required user_id and email properties. """

    @property
    def user_id(self):
        """ Returns the user_id. """
        return dict.get(self, 'user_id', None)

    @user_id.setter
    def user_id(self, user_id):
        """ Sets the user_id. """
        self['user_id'] = user_id

    @property
    def email(self):
        """ Returns the email address. """
        return dict.get(self, 'email', None)

    @email.setter
    def email(self, email):
        """ Sets the email address. """
        self['email'] = email


class User(UserId):
    """ Object representing http://docs.intercom.io/#UserData).  """

    attributes = (
        'user_id', 'email', 'name', 'created_at', 'custom_data',
        'last_seen_ip', 'last_seen_user_agent', 'last_impression_at',
        'last_request_at', 'unsubscribed_from_emails')

    @classmethod
    def find(cls, user_id=None, email=None):
        """ Find a user by email or user_id.

        >>> user = User.find(email="somebody@example.com")
        >>> user.user_id
        u'123'
        >>> user.name
        u'Somebody'
        >>> user = User.find(user_id=123)
        >>> user.email
        u'bob@example.com'
        >>> user.name
        u'Bob'

        """
        resp = Intercom.get_user(user_id=user_id, email=email)
        return cls(resp)

    @classmethod
    def find_by_email(cls, email):
        """ Find a user by email.

        >>> user = User.find_by_email("somebody@example.com")
        >>> user.user_id
        u'123'
        >>> user.name
        u'Somebody'

        """
        resp = Intercom.get_user(email=email)
        return cls(resp)

    @classmethod
    def find_by_user_id(cls, user_id):
        """ Find a user by user_id.

        >>> user = User.find(user_id=123)
        >>> user.email
        u'bob@example.com'
        >>> user.name
        u'Bob'

        """
        resp = Intercom.get_user(user_id=user_id)
        return cls(resp)

    @classmethod
    def create(cls, **kwargs):
        """ Create or update a user.

        >>> user = User.create(email="somebody@example.com",last_impression_at=1400000000)
        >>> user.name
        u'Somebody'
        >>> user.last_impression_at.year
        2014

        """
        resp = Intercom.create_user(**kwargs)
        return cls(resp)

    @classmethod
    def delete(cls, user_id=None, email=None):
        """ Deletes a user.

        >>> user = User.delete(email="somebody@example.com")
        >>> user.user_id
        u'123'
        >>> user = User.delete(user_id="123")
        >>> user.email
        u'bob@example.com'

        """
        resp = Intercom.delete_user(user_id=user_id, email=email)
        return cls(resp)

    @classmethod
    def all(cls):
        """ Return all of the Users.

        >>> users = User.all()
        >>> len(users)
        3
        >>> users[0].email
        u'first.user@example.com'

        """
        page = 1
        total_pages = 1
        users = []
        while page <= total_pages:
            resp = Intercom.get_users(page=page)
            page += 1
            total_pages = resp.get('total_pages', 0)
            users.extend([cls(u) for u in resp['users']])
        return users

    def save(self):
        """ Creates or updates a User.

        >>> user = User()
        >>> user.email = "somebody@example.com"
        >>> user.save()
        >>> user.name
        u'Somebody'

        """
        attrs = {}
        for key in User.attributes:
            value = dict.get(self, key)
            if value is not None:
                attrs[key] = value
        resp = Intercom.update_user(**attrs)
        self.update(resp)

    @property
    def name(self):
        """ Returns the name e.g. Joe Bloggs. """
        return dict.get(self, 'name', None)

    @name.setter
    def name(self, name):
        """ Sets the name. """
        self['name'] = name

    @property
    def last_seen_ip(self):
        """ Returns the last seen IP address. """
        return dict.get(self, 'last_seen_ip', None)

    @last_seen_ip.setter
    def last_seen_ip(self, last_seen_ip):
        """ Sets the last seen IP address. """
        self['last_seen_ip'] = last_seen_ip

    @property
    def last_seen_user_agent(self):
        """ Returns the last seen User Agent. """
        return dict.get(self, 'last_seen_user_agent', None)

    @last_seen_user_agent.setter
    def last_seen_user_agent(self, last_seen_user_agent):
        """ Sets the last seen User Agent. """
        self['last_seen_user_agent'] = last_seen_user_agent

    @property
    def last_request_at(self):
        """ Get last time this User interacted with your application. """
        return dict.get(self, 'last_request_at', None)

    @last_request_at.setter
    @to_timestamp_property
    def last_request_at(self, last_request_at):
        """ Set time at which this User last made a request your application.
        """
        self['last_request_at'] = last_request_at

    @property
    def relationship_score(self):
        """ Returns the relationship score. """
        return dict.get(self, 'relationship_score', None)

    @property
    def session_count(self):
        """ Returns how many sessions this User has used on your
        application. """
        return dict.get(self, 'session_count', None)

    @property
    @from_timestamp_property
    def last_impression_at(self):
        """ Returns the datetime this User last used your application. """
        return dict.get(self, 'last_impression_at', None)

    @last_impression_at.setter
    @to_timestamp_property
    def last_impression_at(self, last_impression_at):
        """ Set time at which this User last made a request your application.
        """
        self['last_impression_at'] = last_impression_at

    @property
    @from_timestamp_property
    def created_at(self):
        """ Returns the datetime this User started using your application. """
        return dict.get(self, 'created_at', None)

    @created_at.setter
    @to_timestamp_property
    def created_at(self, value):
        """ Sets the timestamp when this User started using your
        application. """
        self['created_at'] = value

    @property
    def social_profiles(self):
        """ Returns a list of SocialProfile objects for this User.

        >>> users = User.all()
        >>> social_profiles = users[0].social_profiles
        >>> len(social_profiles)
        2
        >>> type(social_profiles[0])
        <class 'intercom.user.SocialProfile'>
        >>> social_profiles[0].type
        u'twitter'
        >>> social_profiles[0].url
        u'http://twitter.com/abc'

        """
        profiles = dict.get(self, 'social_profiles', None)
        if profiles:
            return [SocialProfile(**p) for p in profiles]

    @property
    def location_data(self):
        """ Returns a LocationData object for this User.

        >>> users = User.all()
        >>> location_data = users[0].location_data
        >>> type(location_data)
        <class 'intercom.user.LocationData'>
        >>> location_data.country_name
        u'Chile'
        >>> location_data.city_name
        u'Santiago'

        """
        data = dict.get(self, 'location_data', None)
        if not isinstance(data, LocationData):
            data = LocationData(data)
            dict.__setitem__(self, 'location_data', data)
        return data

    @property
    def unsubscribed_from_emails(self):
        """ Returns whether or not the user has unsubscribed from emails """
        return dict.get(self, 'unsubscribed_from_emails', None)

    @unsubscribed_from_emails.setter
    def unsubscribed_from_emails(self, unsubscribed_from_emails):
        """  Sets whether or not the user has unsubscribed from email """
        self['unsubscribed_from_emails'] = unsubscribed_from_emails

    @property
    def custom_data(self):
        """ Returns a CustomData object for this User.

        >>> users = User.all()
        >>> custom_data = users[0].custom_data
        >>> type(custom_data)
        <class 'intercom.user.CustomData'>
        >>> custom_data['monthly_spend']
        155.5

        """
        data = dict.get(self, 'custom_data', None)
        if not isinstance(data, CustomData):
            data = CustomData(data)
            dict.__setitem__(self, 'custom_data', data)
        return data

    @custom_data.setter
    def custom_data(self, custom_data):
        """ Sets the CustomData for this User.

        >>> user = User(email="somebody@example.com")
        >>> user.custom_data = { 'max_monthly_spend': 200 }
        >>> type(custom_data)
        <class 'intercom.user.CustomData'>
        >>> user.save()
        >>> len(user.custom_data)
        1
        >>> user.custom_data['avg_monthly_spend'] = 102
        >>> user.save()
        >>> len(user.custom_data)
        2

        """
        if not isinstance(custom_data, CustomData):
            custom_data = CustomData(custom_data)
        self['custom_data'] = custom_data


class CustomData(dict):
    """ A dict that limits keys to strings, and values to real numbers
    and strings.

    >>> from intercom.user import CustomData
    >>> data = CustomData()
    >>> data['a_dict'] = {}
    Traceback (most recent call last):
        ...
    ValueError: custom data only allows string and real number values
    >>> data[1] = "a string"
    Traceback (most recent call last):
        ...
    ValueError: custom data only allows string keys

    """

    def __setitem__(self, key, value):
        """ Limits the keys and values. """
        if not (
            isinstance(value, numbers.Real) or
            isinstance(value, basestring)
        ):
            raise ValueError(
                "custom data only allows string and real number values")
        if not isinstance(key, basestring):
            raise ValueError("custom data only allows string keys")
        super(CustomData, self).__setitem__(key, value)


class SocialProfile(dict):
    """ Object representing http://docs.intercom.io/#SocialProfiles)

    This object is read-only, and to hint at this __setitem__ is disabled.

    >>> from intercom.user import SocialProfile
    >>> profile = SocialProfile(type=u'twitter')
    >>> profile.type
    u'twitter'
    >>> profile['type'] = 'facebook'
    Traceback (most recent call last):
        ...
    NotImplementedError

    """

    @property
    def type(self):
        """ The type e.g. twitter, facebook, flickr, etc. """
        return self.get('type', None)

    @property
    def id(self):
        """ The id """
        return self.get('id', None)

    @property
    def url(self):
        """ The profile url e.g. http://twitter.com/somebody """
        return self.get('url', None)

    @property
    def username(self):
        """ The profile username e.g. somebody """
        return self.get('username', None)

    def __setitem__(self, key, value):
        """ Do not allow items to be set. """
        raise NotImplementedError


class LocationData(dict):
    """ Object representing a user's location data

    This object is read-only, and to hint at this __setitem__ is disabled.

    >>> from intercom.user import SocialProfile
    >>> profile = SocialProfile(type=u'twitter')
    >>> profile.type
    u'twitter'
    >>> profile['type'] = 'facebook'
    Traceback (most recent call last):
        ...
    NotImplementedError

    """

    @property
    def city_name(self):
        """ The city name. """
        return self.get('city_name', None)

    @property
    def continent_code(self):
        """ The continent code. """
        return self.get('continent_code', None)

    @property
    def country_name(self):
        """ The country name. """
        return self.get('country_name', None)

    @property
    def latitude(self):
        """ Latitude. """
        return self.get('latitude', None)

    @property
    def longitude(self):
        """ Longitude. """
        return self.get('longitude', None)

    @property
    def postal_code(self):
        """ The postal code. """
        return self.get('postal_code', None)

    @property
    def region_name(self):
        """ The region name. """
        return self.get('region_name', None)

    @property
    def timezone(self):
        """ The timezone. """
        return self.get('timezone', None)

    @property
    def country_code(self):
        """ The country code. """
        return self.get('country_code', None)

    def __setitem__(self, key, value):
        """ Do not allow items to be set. """
        raise NotImplementedError
