# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#
""" Intercom API wrapper. """

import functools
import time

from datetime import datetime


def from_timestamp_property(func_to_decorate):
    """ A decorator for properties to convert the property value from a
    timestamp to a datetime. """
    @functools.wraps(func_to_decorate)
    def wrapper(instance):
        """ Closure that converts from timestamp to datetime. """
        value = func_to_decorate(instance)
        if value:
            return datetime.fromtimestamp(value)
    return wrapper


def to_timestamp_property(func_to_decorate):
    """ A decorator for properties to convert the property value from a
    datetime to a timestamp. """
    @functools.wraps(func_to_decorate)
    def wrapper(instance, value):
        """ Closure that converts from datetime to timestamp. """
        if value:
            value = time.mktime(value.timetuple())
        func_to_decorate(instance, value)
    return wrapper

from .intercom import AuthenticationError
from .intercom import BadGatewayError
from .intercom import Intercom
from .intercom import ResourceNotFound
from .intercom import ServerError
from .intercom import ServiceUnavailableError

from .impression import Impression
from .message_thread import MessageThread
from .note import Note
from .user import User
from .tag import Tag
from .events import Event

__all__ = (
    AuthenticationError, BadGatewayError, Intercom, ResourceNotFound,
    ServerError, ServiceUnavailableError, Impression, MessageThread,
    Note, User, Tag, Event
)
