# -*- coding: utf-8 -*-

import calendar
import datetime
import time

from intercom.lib.flat_store import FlatStore
from intercom.lib.typed_json_deserializer import JsonDeserializer
from pytz import utc


def type_field(attribute):
    return attribute == "type"


def timestamp_field(attribute):
    return attribute.endswith('_at')


def custom_attribute_field(attribute):
    return attribute == 'custom_attributes'


def typed_value(value):
    return hasattr(value, 'keys') and 'type' in value


def datetime_value(value):
    return hasattr(value, "timetuple")


def to_datetime_value(value):
    if value:
        return datetime.datetime.utcfromtimestamp(int(value)).replace(tzinfo=utc)


class Resource(object):
    client = None
    changed_attributes = []

    def __init__(_self, *args, **params):  # noqa
        if args:
            _self.client = args[0]

        # intercom includes a 'self' field in the JSON, to avoid the naming
        # conflict we go with _self here
        _self.from_dict(params)

        if hasattr(_self, 'flat_store_attributes'):
            for attr in _self.flat_store_attributes:
                if not hasattr(_self, attr):
                    setattr(_self, attr, FlatStore())

    def _flat_store_attribute(self, attribute):
        if hasattr(self, 'flat_store_attributes'):
            return attribute in self.flat_store_attributes
        return False

    @classmethod
    def from_api(cls, response):
        obj = cls()
        obj.from_response(response)
        return obj

    def from_response(self, response):
        self.from_dict(response)
        return self

    def from_dict(self, dict):
        for attribute, value in list(dict.items()):
            if type_field(attribute):
                continue
            setattr(self, attribute, value)
        if hasattr(self, 'id'):
            # already exists in Intercom
            self.changed_attributes = []

    def to_dict(self):
        a_dict = {}
        for name in list(self.__dict__.keys()):
            if name == "changed_attributes":
                continue
            a_dict[name] = self.__dict__[name]  # direct access
        return a_dict

    @property
    def attributes(self):
        res = {}
        for name, value in list(self.__dict__.items()):
            if self.submittable_attribute(name, value):
                res[name] = value
        return res

    def submittable_attribute(self, name, value):
        return name in self.changed_attributes or (isinstance(value, FlatStore) and name in self.flat_store_attributes)  # noqa

    def __getattribute__(self, attribute):
        value = super(Resource, self).__getattribute__(attribute)
        if timestamp_field(attribute):
            return to_datetime_value(value)
        else:
            return value

    def __setattr__(self, attribute, value):
        if typed_value(value) and not custom_attribute_field(attribute):
            value_to_set = JsonDeserializer(value).deserialize()
        elif self._flat_store_attribute(attribute):
            value_to_set = FlatStore(value)
        elif timestamp_field(attribute) and datetime_value(value):
            value_to_set = calendar.timegm(value.utctimetuple())
        else:
            value_to_set = value
        if attribute != 'changed_attributes':
            self.changed_attributes.append(attribute)
        super(Resource, self).__setattr__(attribute, value_to_set)
