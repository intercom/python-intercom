# -*- coding: utf-8 -*-

from intercom import utils
from intercom.user import User
from intercom.collection_proxy import CollectionProxy


class Users(object):

    @property
    def users(self):
        collection = utils.resource_class_to_collection_name(self.__class__)
        finder_url = "/%s/%s/users" % (collection, self.id)
        return CollectionProxy(User, "users", finder_url)
