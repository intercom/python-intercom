# -*- coding: utf-8 -*-
"""Operation to scroll through users."""

from intercom import utils
from intercom.scroll_collection_proxy import ScrollCollectionProxy


class Scroll(object):
    """A mixin that provides `scroll` functionality."""

    def scroll(self, **params):
        """Find all instances of the resource based on the supplied parameters."""
        collection_name = utils.resource_class_to_collection_name(
            self.collection_class)
        finder_url = "/{}/scroll".format(collection_name)
        return ScrollCollectionProxy(
            self.client, self.collection_class, collection_name, finder_url)
