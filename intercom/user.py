# coding=utf-8
#
# Copyright 2014 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from intercom.api_operations.all import All
from intercom.api_operations.count import Count
from intercom.api_operations.delete import Delete
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.traits.api_resource import Resource
from intercom.traits.incrementable_attributes import IncrementableAttributes


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


class User(Resource, Find, FindAll, All, Count, Save, Delete, IncrementableAttributes):

    @property
    def flat_store_attributes(self):
        return ['custom_attributes']

