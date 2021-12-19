# -*- coding: utf-8 -*-
"""Operation to return all users for a particular Company."""

from intercom import utils, contact
from intercom.collection_proxy import CollectionProxy


class Contacts(object):
    """A mixin that provides `users` functionality to Company."""

    def contacts(self, id):
        """Return a CollectionProxy to all the users for the specified Company."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        finder_url = "/%s/%s/contacts" % (collection, id)
        return CollectionProxy(
            self.client, contact.Contact, "contacts", finder_url)
