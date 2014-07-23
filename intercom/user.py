# coding=utf-8
#
# Copyright 2014 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import datetime
import time
from intercom import FlatStore
from intercom.api_operations.all import All
from intercom.api_operations.count import Count
from intercom.api_operations.delete import Delete
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.lib.typed_json_deserializer import JsonDeserializer


class ArgumentError(ValueError):
    pass


def timestamp_field(attribute):
    return attribute.endswith('_at')


def type_field(attribute):
    return attribute == "type"


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


CLASS_REGISTRY = {}

def create_class_instance(class_name):

    if class_name in CLASS_REGISTRY:
        return CLASS_REGISTRY[class_name]

    class Meta(type):
        def __new__(mcs, name, bases, attributes):
            return super(Meta, mcs).__new__(mcs, str(class_name), bases, attributes)

    class DynamicClass(Resource):
        __metaclass__ = Meta

    dyncls = DynamicClass()
    CLASS_REGISTRY[class_name] = dyncls
    return dyncls



class IncrementableAttributes(object):

    def increment(self, key, value=1):
        existing_value = self.custom_attributes.get(key, 0)
        self.custom_attributes[key] = existing_value + value


class User(Resource, Find, FindAll, All, Count, Save, Delete, IncrementableAttributes):

    @property
    def flat_store_attributes(self):
        return ['custom_attributes']


class Company(Resource, Find, Count):
    pass


class Admin(Resource, Find):
    pass


class Tag(Resource, Find, Count):
    pass



class Note(Resource, Find):
    pass


class Event(Resource, Find):
    pass


# class Count(Resource):
#     pass


class Conversation(Resource, Find):
    pass
