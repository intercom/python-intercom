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
    @functools.wraps(func_to_decorate)
    def wrapper(instance):
        value = func_to_decorate(instance)
        return datetime.fromtimestamp(value)
    return wrapper

def to_timestamp_property(func_to_decorate):
    @functools.wraps(func_to_decorate)
    def wrapper(instance, value):
        value = time.mktime(value.timetuple())
        func_to_decorate(instance, value)
    return wrapper


from .intercom import Intercom
from .user import User
from .message_thread import MessageThread
from .impression import Impression
