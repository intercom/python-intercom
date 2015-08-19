# -*- coding: utf-8 -*-

from intercom import HttpError
from intercom import utils


class Find(object):

    def find(self, **params):
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
