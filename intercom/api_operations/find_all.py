# -*- coding: utf-8 -*-
"""Operation to find all instances of a particular resource."""

from intercom import utils
from intercom.collection_proxy import CollectionProxy


class FindAll(object):
    """A mixin that provides `find_all` functionality."""

    def find_all(self, **params):
        """Find all instances of the resource based on the supplied parameters."""
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
