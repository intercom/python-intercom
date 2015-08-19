# -*- coding: utf-8 -*-

from intercom import utils
from intercom.collection_proxy import CollectionProxy


class All(object):

    def all(self):
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        finder_url = "/%s" % (collection)
        return CollectionProxy(
            self.client, self.collection_class, collection, finder_url)
