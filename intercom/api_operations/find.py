from intercom import Intercom
from intercom import utils


class Find(object):

    @classmethod
    def find(cls, **params):
        collection = utils.resource_class_to_collection_name(cls)
        if 'id' in params:
            response = Intercom.get("/%s/%s" % (collection, params['id']))
        else:
            response = Intercom.get("/%s" % (collection), **params)
        return cls(**response)
