# -*- coding: utf-8 -*-

import inflection
import six


def pluralize(str):
    return inflection.pluralize(str)


def entity_key_from_type(type):
    if '.' in type:
        is_list = type.split('.')[1] == 'list'
        entity_name = type.split('.')[0]
        if is_list:
            return pluralize(entity_name)
    else:
        entity_name = type
    return entity_name


def constantize_singular_resource_name(resource_name):
    class_name = inflection.camelize(resource_name)
    return create_class_instance(class_name)


def resource_class_to_collection_name(cls):
    return pluralize(cls.__name__.lower())


def resource_class_to_name(cls):
    return cls.__name__.lower()


CLASS_REGISTRY = {}


def create_class_instance(class_name):
    from intercom.api_operations.load import Load
    from intercom.traits.api_resource import Resource

    if class_name in CLASS_REGISTRY:
        return CLASS_REGISTRY[class_name]

    class Meta(type):
        def __new__(cls, name, bases, attributes):
            return super(Meta, cls).__new__(
                cls, str(class_name), bases, attributes)

    @six.add_metaclass(Meta)
    class DynamicClass(Resource, Load):
        pass

    dyncls = DynamicClass()
    CLASS_REGISTRY[class_name] = dyncls
    return dyncls
