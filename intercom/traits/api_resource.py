import datetime
import time

from intercom.lib.flat_store import FlatStore
from intercom.lib.typed_json_deserializer import JsonDeserializer


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
        return datetime.datetime.fromtimestamp(int(value))


class Resource(object):

    def __init__(self, **params):
        self.from_dict(params)

        if hasattr(self, 'flat_store_attributes'):
            for attr in self.flat_store_attributes:
                if not hasattr(self, attr):
                    setattr(self, attr, FlatStore())

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
        for attribute, value in dict.items():
            if type_field(attribute):
                continue
            setattr(self, attribute, value)

    @property
    def attributes(self):
        return self.__dict__

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
            value_to_set = time.mktime(value.timetuple())
        else:
            value_to_set = value
        super(Resource, self).__setattr__(attribute, value_to_set)
