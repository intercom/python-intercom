# coding=utf-8
#
# Copyright 2014 martin@mekkaoui.fr
#
# License: MIT
#
""" Intercom API wrapper. """

from . import Intercom

class Event(dict):

    @classmethod
    def create(cls, event_name=None, user_id=None, email=None, metadata=None):
        resp = Intercom.create_event(event_name=event_name, user_id=user_id, email=email, metadata=metadata)
        return Event(resp)