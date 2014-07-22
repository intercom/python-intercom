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


if __name__ == "__main__":
    print pluralize('company')
    print pluralize('user')

    print entity_key_from_type('company.list')

    print constantize_singular_resource_name('location_data')
    print constantize_singular_resource_name('companies')

    from intercom.user import User
    user = User()
    user.from_dict({
        'username': 'john', 
        'companies': {
            "type": "company.list",
            "companies": [
                {
                    "type": "company",
                    "id": "xyz"
                }
            ]
        }
    })
    print user.username
    print user.companies[0].__class__.__name__
