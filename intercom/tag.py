from intercom import Intercom
from intercom import utils
from intercom.user import Resource
from intercom.api_operations.all import All
from intercom.api_operations.count import Count
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save


class Tag(Resource, All, Count, Find, FindAll, Save):

    @classmethod
    def _tag_collection(cls, name, collection_name, objects, untag=False):
        collection = utils.resource_class_to_collection_name(cls)

        object_ids = []
        for obj in objects:
            if not hasattr(obj, 'keys'):
                obj = {'id': obj}
            if untag:
                obj['untag'] = True
            object_ids.append(obj)

        params = {
            'name': name,
            collection_name: object_ids,
        }
        response = Intercom.post("/%s" % (collection), **params)
        return cls(**response)

    @classmethod
    def tag_users(cls, name, users):
        return cls._tag_collection(name, 'users', users)

    @classmethod
    def untag_users(cls, name, users):
        return cls._tag_collection(name, 'users', users, untag=True)

    @classmethod
    def tag_companies(cls, name, companies):
        return cls._tag_collection(name, 'companies', companies)

    @classmethod
    def untag_companies(cls, name, companies):
        return cls._tag_collection(name, 'companies', companies, untag=True)
