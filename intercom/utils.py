import inflection

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
    from intercom.user import create_class_instance
    return create_class_instance(class_name)


def resource_class_to_collection_name(cls):
    return cls.__name__.lower() + "s"


def resource_class_to_name(cls):
    return cls.__name__.lower()
