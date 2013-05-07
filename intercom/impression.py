# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#
""" Impression module.

>>> from intercom import Intercom
>>> Intercom.app_id = 'dummy-app-id'
>>> Intercom.api_key = 'dummy-api-key'
>>> from intercom import Impression

"""

from . import Intercom
from .user import UserId


class Impression(UserId):
    """ An Impression represents an interaction between a User and your
    application. """

    @classmethod
    def create(cls, user_id=None, email=None, user_ip=None, user_agent=None,
               location=None):
        """ Create an Impression.

        >>> Impression.create(email="somebody@example.com",
        ...        location="/pricing/upgrade",
        ...        user_ip="1.2.3.4",
        ...        user_agent="my-service-iphone-app-1.2")
        {u'unread_messages': 1}

        """
        resp = Intercom.create_impression(
            user_id=user_id, email=email, user_ip=user_ip,
            user_agent=user_agent, location=location)
        return cls(resp)

    def save(self):
        """ Create an Impression from this objects properties:

        >>> impression = Impression()
        >>> impression.email = "somebody@example.com"
        >>> impression.location = "/pricing/upgrade"
        >>> impression.user_ip = "1.2.3.4"
        >>> impression.user_agent = "my-service-iphone-app-1.2"
        >>> impression.save()
        >>> impression.unread_messages
        1

        """
        resp = Intercom.create_impression(**self)
        self.update(resp)

    @property
    def user_ip(self):
        """ The IP address where this Impression originated. """
        return dict.get(self, 'user_ip', None)

    @user_ip.setter
    def user_ip(self, user_ip):
        """ Set the user IP address. """
        self['user_ip'] = user_ip

    @property
    def location(self):
        """ The location where this Impression originated e.g.
        /pricing/upgrade or 'DesktopApp: Pricing' or 'iOS'. """
        return dict.get(self, 'location', None)

    @location.setter
    def location(self, location):
        """ Set the location. """
        self['location'] = location

    @property
    def user_agent(self):
        """ The User Agent that created this Impression e.g. the browser
        User Agent, or the name and version of an application. """
        return dict.get(self, 'user_agent', None)

    @user_agent.setter
    def user_agent(self, user_agent):
        """ Set the User Agent. """
        self['user_agent'] = user_agent

    @property
    def unread_messages(self):
        """ The number of unread messages for the User who made the
        Impression for the current location. """
        return dict.get(self, 'unread_messages', None)
