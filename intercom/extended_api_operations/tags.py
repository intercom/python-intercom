# -*- coding: utf-8 -*-
"""Operation to return resources with a particular tag."""

from intercom import utils
from intercom.collection_proxy import CollectionProxy


class Tags(object):
    """A mixin that provides `by_tag` functionality a resource."""

    def by_tag(self, _id):
        """Return a CollectionProxy to all the tagged resources."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        finder_url = "/%s?tag_id=%s" % (collection, _id)
        return CollectionProxy(
            self.client, self.collection_class, collection, finder_url)
