# -*- coding: utf-8 -*-
"""Operation to delete an instance of a particular resource."""

from intercom import utils


class Delete(object):
    """A mixin that provides `delete` functionality."""

    def delete(self, obj=None, **kwargs):
        """Delete the specified instance of this resource."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        assert obj is not None or kwargs.keys()[0] == "%s_id" % collection
        obj_id = kwargs.values()[0] if obj is None else obj.id
        self.client.delete("/%s/%s" % (collection, obj_id), {})
        return obj
