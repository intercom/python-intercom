# -*- coding: utf-8 -*-
"""Operation to return all users for a particular Company."""

from deprecated import deprecated

from intercom import user, utils
from intercom.collection_proxy import CollectionProxy


@deprecated(
    """Users is no longer available as a resource. 
    In order to see information and take action on users, 
    you should use the Contacts API."""
)
class Users(object):
    """A mixin that provides `users` functionality to Company."""

    def users(self, id):
        """Return a CollectionProxy to all the users for the specified Company."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class
        )
        finder_url = f"/{collection}/{id}/users"
        return CollectionProxy(
            self.client, user.User, "users", finder_url
        )
