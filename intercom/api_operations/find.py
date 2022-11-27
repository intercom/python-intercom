# -*- coding: utf-8 -*-
"""Operation to find an instance of a particular resource."""

from intercom import HttpError
from intercom import utils


class Find(object):
    """A mixin that provides `find` functionality."""

    def find(self, force_only_one=True, **params):
        """Find the instance of the resource based on the supplied parameters."""
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        if 'id' in params:
            object_data = self.client.get(
                "/%s/%s" % (collection, params['id']), {})
        else:
            response = self.client.post("/%s/search" % collection, params)
            data_list = response["data"]
            if force_only_one:
                if len(data_list) > 1:
                    raise Exception("There is more than 1 result (%s)" % len(data_list))
                object_data = data_list[0]
            else:
                object_data = response

        if object_data is None:
            raise HttpError('Http Error - No response entity returned')

        return self.collection_class(**object_data)
