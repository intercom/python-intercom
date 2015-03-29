# -*- coding: utf-8 -*-

from intercom import utils
from intercom.collection_proxy import CollectionProxy


class All(object):

    @classmethod
    def all(cls):
        collection = utils.resource_class_to_collection_name(cls)
        finder_url = "/%s" % (collection)
        return CollectionProxy(cls, collection, finder_url)
