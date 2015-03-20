# -*- coding: utf-8 -*-

from intercom import utils
from intercom.collection_proxy import CollectionProxy


class FindAll(object):

    @classmethod
    def find_all(cls, **params):
        collection = utils.resource_class_to_collection_name(cls)
        if 'id' in params and 'type' not in params:
            finder_url = "/%s/%s" % (collection, params['id'])
        else:
            finder_url = "/%s" % (collection)
        finder_params = params
        return CollectionProxy(cls, collection, finder_url, finder_params)
