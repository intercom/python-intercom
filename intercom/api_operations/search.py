# -*- coding: utf-8 -*-
"""Operation to search through contacts."""

from intercom import utils


class Search(object):
    """A mixin that provides `search` functionality."""

    def search(self, query, **params):
        """Find all instances of the resource based on the supplied parameters."""
        collection_name = utils.resource_class_to_collection_name(
            self.collection_class)
        finder_url = "/{}/scroll".format(collection_name)

        response = self.client.post("/{}/search".format(collection_name), query)
        
        collection_data = response['data']
            
        return map(lambda item: self.collection_class(**item), collection_data)