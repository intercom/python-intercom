# -*- coding: utf-8 -*-
"""Operation to delete an instance of a particular resource."""

from intercom import utils


class Delete(object):
    """A mixin that provides `delete` functionality."""

    def delete(self, obj):
        """Delete the specified instance of this resource."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        self.client.delete("/%s/%s" % (collection, obj.id), {})
        return obj
