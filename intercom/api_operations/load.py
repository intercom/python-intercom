# -*- coding: utf-8 -*-
"""Operation to load an instance of a particular resource."""

from intercom import HttpError
from intercom import utils


class Load(object):
    """A mixin that provides `load` functionality."""

    def load(self, resource):
        """Load the resource from the latest data in Intercom."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        if hasattr(resource, 'id'):
            response = self.client.get("/%s/%s" % (collection, resource.id), {})  # noqa
        else:
            raise Exception(
                "Cannot load %s as it does not have a valid id." % (
                    self.collection_class))

        if response is None:
            raise HttpError('Http Error - No response entity returned')

        return resource.from_response(response)
