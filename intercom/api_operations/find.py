# -*- coding: utf-8 -*-
"""Operation to find an instance of a particular resource."""

from intercom import HttpError
from intercom import utils


class Find(object):
    """A mixin that provides `find` functionality."""

    def find(self, **params):
        """Find the instance of the resource based on the supplied parameters."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        if 'id' in params:
            response = self.client.get(
                "/%s/%s" % (collection, params['id']), {})
        else:
            response = self.client.get("/%s" % (collection), params)

        if response is None:
            raise HttpError('Http Error - No response entity returned')

        return self.collection_class(**response)
