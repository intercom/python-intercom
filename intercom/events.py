# coding=utf-8
#
# Copyright 2014 martin@mekkaoui.fr
#
# License: MIT
#
""" Intercom API wrapper. """

from . import Intercom
from .user import UserId


class Event(UserId):

    @classmethod
    def create(cls, event_name=None, user_id=None, email=None, metadata=None):
        resp = Intercom.create_event(event_name=event_name, user_id=user_id, email=email, metadata=metadata)
        return Event(resp)

    def save(self):
        """ Create an Event from this objects properties:

        >>> event = Event()
        >>> event.event_name = "shared-item"
        >>> event.email = "joe@example.com"
        >>> event.save()

        """
        resp = Intercom.create_event(**self)
        self.update(resp)

    @property
    def event_name(self):
        """ The name of the Event. """
        return dict.get(self, 'event_name', None)

    @event_name.setter
    def event_name(self, event_name):
        """ Set the event name. """
        self['event_name'] = event_name
