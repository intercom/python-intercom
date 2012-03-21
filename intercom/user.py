#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from . import Intercom
from . import from_timestamp_property
from . import to_timestamp_property

import numbers

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
    """ Object representing http://docs.intercom.io/#UserData) """

    attributes = ('user_id', 'email', 'name', 'created_at', 'custom_data',
            'last_seen_ip', 'last_seen_user_agent')

    @classmethod
    def find(cls, user_id=None, email=None):
        resp = Intercom.get_user(user_id=user_id, email=email)
        return cls(resp)

    @classmethod
    def find_by_email(cls, email):
        resp = Intercom.get_user(email=email)
        return cls(resp)

    @classmethod
    def find_by_user_id(cls, user_id):
        resp = Intercom.get_user(user_id=user_id)
        return cls(resp)

    @classmethod
    def create(cls, user_id=None, email=None, name=None, created_at=None, 
            custom_data=None, last_seen_ip=None, last_seen_user_agent=None):

        resp = Intercom.create_user(user_id=user_id, email=email, name=name, 
                created_at=created_at, custom_data=custom_data, 
                last_seen_ip=last_seen_ip, last_seen_user_agent=last_seen_user_agent)
        return cls(resp)

    @classmethod
    def all(cls):
        resp = Intercom().get_users()
        return [cls(u) for u in resp['users']]

    def save(self):
        attrs = {}
        for key in User.attributes:
            value = dict.get(self, key) 
            if value:
                attrs[key] = value
        resp = Intercom.update_user(**attrs)
        self.update(resp)

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
        data = dict.get(self, 'location_data', None)
        if not isinstance(data, LocationData):
            data = LocationData(data)
            dict.__setitem__(self, 'location_data', data)
        return data

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

class CustomData(dict):
    """ A dict that limits keys to strings, and values to real numbers
    and strings. """

    def __setitem__(self, key, value):
        """ Limits the keys and values. """
        if not (isinstance(value, numbers.Real) or isinstance(value, basestring)):
            raise ValueError("custom data only allows string and real number values")
        if not isinstance(key, basestring):
            raise ValueError("custom data only allows string keys")
        super(CustomData, self).__setitem__(key, value)

class SocialProfile(dict):
    """ Object representing http://docs.intercom.io/#SocialProfiles) """

    @property
    def type(self):
        """ type e.g. twitter, facebook, flickr, etc. """
        return self.get('type', None)

    @property
    def id(self):
        """ id """
        return self.get('id', None)

    @property
    def url(self):
        """ profile url """
        return self.get('url', None)

    @property
    def username(self):
        """ username """
        return self.get('username', None)

    def __setitem__(self, key, value):
        """ Do not allow items to be set. """
        raise NotImplementedError

class LocationData(dict):
    """ Object representing a user's location data """

    @property
    def city_name(self):
        return self.get('city_name', None)

    @property
    def continent_code(self):
        return self.get('continent_code', None)

    @property
    def country_name(self):
        return self.get('country_name', None)

    @property
    def latitude(self):
        return self.get('latitude', None)

    @property
    def longitude(self):
        return self.get('longitude', None)

    @property
    def postal_code(self):
        return self.get('postal_code', None)

    @property
    def region_name(self):
        return self.get('region_name', None)

    @property
    def timezone(self):
        return self.get('timezone', None)

    @property
    def country_code(self):
        return self.get('country_code', None)

    def __setitem__(self, key, value):
        """ Do not allow items to be set. """
        raise NotImplementedError
