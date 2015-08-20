# -*- coding: utf-8 -*-

from intercom import utils
from intercom.collection_proxy import CollectionProxy


class Users(object):

    def users(self, id):
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        finder_url = "/%s/%s/users" % (collection, id)
        return CollectionProxy(
            self.client, self.collection_class, "users", finder_url)
