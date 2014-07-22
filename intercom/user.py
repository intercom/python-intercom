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


def resource_class_to_collection_name(cls):
    return cls.__name__.lower() + "s"


def resource_class_to_name(cls):
    return cls.__name__.lower()


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


class Find(object):

    @classmethod
    def find(cls, **params):
        collection = resource_class_to_collection_name(cls)
        print "find %s in %s" % (params, collection)
        if 'id' in params:
            response = Intercom.get("/%s/%s" % (collection, params['id']))
        else:
            response = Intercom.get("/%s" % (collection), **params)
        return cls(**response)


class CollectionProxy(object):

    def __init__(self, cls, collection, finder_url, finder_params={}):
        # needed to create class instances of the resource
        self.collection_cls = cls

        # needed to reference the collection in the response
        self.collection = collection

        # the original URL to retrieve the resources
        self.finder_url = finder_url

        # the params to filter the resources
        self.finder_params = finder_params

        # an iterator over the resources found in the response
        self.resources = None

        # a link to the next page of results
        self.next_page = None


    def __iter__(self):
        return self

    def next(self):
        if self.resources is None:
            # get the first page of results
            self.get_first_page()

        # try to get a resource if there are no more in the 
        # current resource iterator (StopIteration is raised)
        # try to get the next page of results first
        try:
            resource = self.resources.next()
        except StopIteration:
            self.get_next_page()
            resource = self.resources.next()

        instance = self.collection_cls(**resource)
        return instance

    def get_first_page(self):
        # get the first page of results
        return self.get_page(self.finder_url, self.finder_params)

    def get_next_page(self):
        # get the next page of results
        return self.get_page(self.next_page)

    def get_page(self, url, params={}):
        # get a page of results

        # if there is no url stop iterating
        if url is None:
            raise StopIteration

        response = Intercom.get(url, **params)
        collection = response[self.collection]
        # if there are no resources in the response stop iterating
        if collection is None:
            raise StopIteration

        # create the resource iterator
        self.resources = iter(collection)
        # grab the next page URL if one exists
        self.next_page = self.extract_next_link(response)

    def paging_info_present(self, response):
        return 'pages' in response and 'type' in response['pages']

    def extract_next_link(self, response):
        if self.paging_info_present(response):
            paging_info = response["pages"]
            return paging_info["next"]


class FindAll(object):

    @classmethod
    def find_all(cls, **params):
        collection = resource_class_to_collection_name(cls)
        print "find_all %s in %s" % (params, collection)
        if 'id' in params and 'type' not in params:
            finder_url = "/%s/%s" % (collection, params['id'])
        else:
            finder_url = "/%s" % (collection)
        finder_params = params
        return CollectionProxy(cls, collection, finder_url, finder_params)


class IncrementableAttributes(object):

    def increment(self, key, value=1):
        existing_value = self.custom_attributes.get(key, 0)
        self.custom_attributes[key] = existing_value + value


class All(object):

    @classmethod
    def all(cls):
        collection = resource_class_to_collection_name(cls)
        print "list %s" % (collection)
        finder_url = "/%s" % (collection)
        return CollectionProxy(cls, collection, finder_url)


class Count(object):

    @classmethod
    def count(cls):
        response = Intercom.get("/counts/")
        return response[resource_class_to_name(cls)]['count']


class Save(object):

    @classmethod
    def create(cls, **params):
        collection = resource_class_to_collection_name(cls)
        response = Intercom.post("/%s/" % (collection), **params)
        return cls(**response)

    def from_dict(self, pdict):
        for key, value in pdict.items():
            setattr(self, key, value)

    @property
    def to_dict(self):
        a_dict = {}
        for name in self.attributes.keys():
            a_dict[name] = self.__dict__[name]  # direct access
        return a_dict


    @classmethod
    def from_api(cls, response):
        obj = cls()
        obj.from_response(response)
        return obj

    def from_response(self, response):
        self.from_dict(response)
        return self

    def save(self):
        collection = resource_class_to_collection_name(self.__class__)
        params = self.__dict__
        if self.id_present:
            # update
            response = Intercom.put('/%s/%s' % (collection, self.id), **params)
        else:
            # create
            response = Intercom.post('/%s' % (collection), **params)
        if response:
            return self.from_response(response)


    @property
    def id_present(self):
        return getattr(self, 'id', None) and self.id != ""

    @property
    def posted_updates(self):
        return getattr(self, 'update_verb', None) != 'post'

    @property
    def identity_hash(self):
        identity_vars = getattr(self, 'identity_vars', None)
        if identity_vars:
            return {}



class Delete(object):

    def delete(self):
        collection = resource_class_to_collection_name(self.__class__)
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
