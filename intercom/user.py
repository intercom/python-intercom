# coding=utf-8
#
# Copyright 2014 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from intercom import Intercom
from intercom import FlatStore
import datetime
import time
import types
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.collection_proxy import CollectionProxy


class ArgumentError(ValueError):
    pass

from intercom import utils

class JsonDeserializer(object):

    def __init__(self, json):
        self._json = json
        self._object_type = None

    @property
    def _get_object_type(self):
        if self._object_type is None:
            self._object_type = self._json.get('type', None)
            # print "OBJECT TYPE IS ", self._object_type
            if self._object_type is None:
                raise Exception('No type field found to faciliate deserialization')
        return self._object_type

    @property
    def _is_list_type(self):
        # print "IS LIST TYPE", self._get_object_type
        return self._get_object_type.endswith('.list')

    @property
    def _object_entity_key(self):
        return utils.entity_key_from_type(self._get_object_type)

    def deserialize(self):
        if self._is_list_type:
            # print "SELF %s" % (self._json)
            # print "ENTITY KEY %s" % (self._object_entity_key)
            # print "  JSON %s" % (self._json[self._object_entity_key])
            return self.deserialize_collection(self._json[self._object_entity_key])
        else:
            return self.deserialize_object(self._json)

    def deserialize_collection(self, collection_json):
        return [JsonDeserializer(object_json).deserialize() for object_json in collection_json]

    def deserialize_object(self, object_json):
        entity_class = utils.constantize_singular_resource_name(self._object_entity_key)
        return entity_class.from_api(object_json)
    #     return entity_class
    # print "deserialize %s:%s:%s" % (name, value, type(value))

    # if name[-3:] == "_at":
    #     if hasattr(value, "timetuple"):
    #         value = time.mktime(value.timetuple())
    #     elif hasattr(value, 'keys'):
    #         print "HAS KEYS [%s:%s]" % (name, value.get('type'))
    #         if 'type' in value:
    #             if value['type'][-5:] == '.list':
    #                 res = []
    #                 for item in value[name]:
    #                     obj = Intercom.create_class_instance(name)
    #                     obj.update(item)
    #                     res.append(obj)
    #                 value = res
    #             else:
    #                 obj = Intercom.create_class_instance(name)
    #                 obj.update(value)
    #                 value = obj
    #         else:
    #             print "ELSE NAME %s [%s] [%s]" % (name, self.__class__, value)
    #             if hasattr(self, 'flat_store_attributes') and name in self.flat_store_attributes:
    #                 value = FlatStore(value)
    #             else:
    #                 obj = Intercom.create_class_instance(name)
    #                 obj.update(value)
    #                 value = obj
    #                 print "CREATED %s" % (type(value))
    #     elif type(value) == types.ListType:
    #         print "LIST ATTR"


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

    # class __metaclass__(type):
    #     def __new__(mcs, name, bases, attributes):
    #         if '__intercom_collection__' not in attributes:
    #             attributes.update(__intercom_collection__=name.lower() + "s")
    #         if '__intercom_name__' not in attributes:
    #             attributes.update(__intercom_name__=name.lower())
    #         cls = type.__new__(mcs, name, bases, attributes)
    #         return cls

    def __init__(self, **params):
        # self.__class__.__intercom_collection__ = self.__class__.__name__.lower() + "s"
        # self.__class__.__intercom_name__ = self.__class__.__name__.lower()
        # if '__intercom_collection__' not in attributes:
        #     attributes.update(__intercom_collection__=name.lower() + "s")
        # if '__intercom_name__' not in attributes:
        #     attributes.update(__intercom_name__=name.lower())
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
        # setattr(self, attribute, value_to_set)

    # def __setattr__(self, name, value):
    #     print "SET ATTR %s:%s:%s" % (name, value, type(value))
    #     # print "setattr", name, value
    #     if name[-3:] == "_at":
    #         if hasattr(value, "timetuple"):
    #             value = time.mktime(value.timetuple())
    #     elif hasattr(value, 'keys'):
    #         print "NAME %s [%s] [%s]" % (name, self.__class__, value)
    #         if hasattr(self, 'flat_store_attributes') and name in self.flat_store_attributes:
    #             value = FlatStore(value)
    #         else:
    #             obj = create_class_instance(name)
    #             obj.update(value)
    #             value = obj
    #             print "CREATED %s" % (type(value))
    #     elif type(value) == types.ListType:
    #         print "LIST ATTR"

    #     super(Resource, self).__setattr__(name, value)


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


class All(object):

    @classmethod
    def all(cls):
        collection = utils.resource_class_to_collection_name(cls)
        print "list %s" % (collection)
        finder_url = "/%s" % (collection)
        return CollectionProxy(cls, collection, finder_url)


class Count(object):

    @classmethod
    def count(cls):
        response = Intercom.get("/counts/")
        return response[utils.resource_class_to_name(cls)]['count']


class Delete(object):

    def delete(self):
        collection = utils.resource_class_to_collection_name(self.__class__)
        Intercom.delete("/%s/%s/" % (collection, self.id))
        return self


class User(Resource, Find, FindAll, All, Count, Save, Delete, IncrementableAttributes):
    @property
    def flat_store_attributes(self):
        return ['custom_attributes']

    # __slots__ = [
    #     'type', 'id', 'created_at', 'remote_created_at',
    #     'updated_at', 'user_id', 'email', 'name', 'custom_attributes',
    #     'last_request_at', 'session_count', 'avatar',
    #     'unsubscribed_from_emails', 'location_data', 'user_agent_data',
    #     'last_seen_ip', 'companies', 'social_profiles', 'segments',
    #     'tags'
    # ]


class Company(Resource, Find, Count):
    pass


class Admin(Resource, Find):
    pass


class Tag(Resource, Find, Count):
    pass


class Segment(Resource, Find, Count):
    pass


class Note(Resource, Find):
    pass


class Event(Resource, Find):
    pass


# class Count(Resource):
#     pass


class Conversation(Resource, Find):
    pass
