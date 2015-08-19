# -*- coding: utf-8 -*-

from intercom import utils
from intercom.collection_proxy import CollectionProxy


class FindAll(object):

    def find_all(self, **params):
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        if 'id' in params and 'type' not in params:
            finder_url = "/%s/%s" % (collection, params['id'])
        else:
            finder_url = "/%s" % (collection)
        finder_params = params
        return CollectionProxy(
            self.client, self.collection_class, collection,
            finder_url, finder_params)
