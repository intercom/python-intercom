# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#
""" User module.

>>> from intercom import Intercom
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
        'user_id', 'email', 'name', 'signed_up_at', 'custom_attributes',
        'last_seen_ip', 'user_agent_data', 'companies', 'last_request_at', 'update_last_request_at', 'last_seen_user_agent', 'unsubscribed_from_emails')

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
        u'somebody@example.com'
        >>> user.name
        u'Somebody'

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
        u'somebody@example.com'
        >>> user.name
        u'Somebody'

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
        2011

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
        u'somebody@example.com'

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
    def user_agent_data(self):
        """ Returns the last seen User Agent. """
        return dict.get(self, 'user_agent_data', None)

    @user_agent_data.setter
    def user_agent_data(self, user_agent_data):
        """ Sets the last seen User Agent. """
        self['user_agent_data'] = user_agent_data
        
    @property
    def last_seen_user_agent(self):
        """ Returns the last seen User Agent. """
        return dict.get(self, 'last_seen_user_agent', None)

    @last_seen_user_agent.setter
    def last_seen_user_agent(self, last_seen_user_agent):
        """ Sets the last seen User Agent. """
        self['last_seen_user_agent'] = last_seen_user_agent

    @property
    def update_last_request_at(self):
        """ Returns the last seen User Agent. """
        return dict.get(self, 'update_last_request_at', None)

    @update_last_request_at.setter
    def update_last_request_at(self, update_last_request_at):
        """ Sets the last seen User Agent. """
        self['update_last_request_at'] = update_last_request_at
        
    @property
    @from_timestamp_property
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
        return dict.get(self, 'session_count', 0)

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
    @from_timestamp_property
    def signed_up_at(self):
        """ Returns the datetime this User started using your application. """
        return dict.get(self, 'signed_up_at', None)

    @signed_up_at.setter
    @to_timestamp_property
    def signed_up_at(self, value):
        """ Sets the timestamp when this User started using your
        application. """
        self['signed_up_at'] = value

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
    def company(self):
        """ Get the company of a user. Currently unsupported by the Intercom
        API so an AttributeError is raised.

        >>> user = User(email="somebody@example.com")
        >>> user.company
        Traceback (most recent call last):
            ...
        AttributeError: company is a write-only property

        """
        raise AttributeError("company is a write-only property")

    @company.setter
    def company(self, company):
        """ Sets the company for a user.

        >>> user = User(email="somebody@example.com")
        >>> user.company = {'id':6, 'name': 'Intercom', 'created_at': 103201}

        """
        if isinstance(company, Company):
            self['companies'] = [company]
        elif isinstance(company, dict):
            self['companies'] = [Company(**company)]
        else:
            raise ValueError("company must be set as a dict or Company object")

    @property
    def companies(self):
        """ Get the companies of a user. Currently unsupported by the Intercom
        API so an AttributeError is raised.

        >>> user = User(email="somebody@example.com")
        >>> user.companies
        Traceback (most recent call last):
            ...
        AttributeError: companies is a write-only property

        """
        raise AttributeError("companies is a write-only property")

    @companies.setter
    def companies(self, companies):
        """ Sets the companies for the user

        >>> user = User(email="somebody@example.com")
        >>> user.companies = [{'id': 6, 'name': 'Intercom', 'created_at': 103201}]

        """
        #Ensure a companies is set as a list.
        if isinstance(companies, list):
            self['companies'] = [Company(**c) for c in companies]
        else:
            raise ValueError("companies must be set as a list")

    @property
    def custom_attributes(self):
        """ Returns a CustomAttributes object for this User.

        >>> users = User.all()
        >>> custom_data = users[0].custom_data
        >>> type(custom_data)
        <class 'intercom.user.CustomData'>
        >>> custom_data['monthly_spend']
        155.5

        """
        data = dict.get(self, 'custom_attributes', None)
        if not isinstance(data, CustomAttributes):
            data = CustomAttributes(data)
            dict.__setitem__(self, 'custom_attributes', data)
        return data

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """ Sets the CustomAttributes for this User.

        >>> user = User(email="somebody@example.com")
        >>> user.custom_data = { 'max_monthly_spend': 200 }
        >>> type(user.custom_data)
        <class 'intercom.user.CustomData'>
        >>> user.save()
        >>> len(user.custom_data)
        3

        """
        if not isinstance(custom_attributes, CustomAttributes):
            custom_attributes = CustomAttributes(custom_attributes)
        self['custom_attributes'] = custom_attributes


class CustomAttributes(dict):
    """ A dict that limits keys to strings, and values to real numbers
    and strings.

    >>> from intercom.user import CustomAttributes
    >>> data = CustomAttributes()
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
            isinstance(value, basestring) or
            isinstance(value, bool)
        ):
            raise ValueError(
                "custom attributes only allows string and real number values")
        if not isinstance(key, basestring):
            raise ValueError("custom attributes only allows string keys")
        super(CustomAttributes, self).__setitem__(key, value)


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

class Company(dict):
    """ Object represents an Intercom Company """

    @property
    def id(self):
        """ Returns the company's id. """
        return dict.get(self, 'id', None)

    @id.setter
    def id(self, company_id):
        """ Sets thecompany's id. """
        self['id'] = company_id

    @property
    def name(self):
        """ Returns the company name e.g. Intercom. """
        return dict.get(self, 'name', None)

    @name.setter
    def name(self, name):
        """ Sets the company name. """
        self['name'] = name

    @property
    @from_timestamp_property
    def created_at(self):
        """ Returns the datetime this Company was created. """
        return dict.get(self, 'created_at', None)

    @created_at.setter
    @to_timestamp_property
    def created_at(self, value):
        """ Sets the timestamp when this Company was created. """
        self['created_at'] = value

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
