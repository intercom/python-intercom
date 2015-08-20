# -*- coding: utf-8 -*-

from intercom import utils


class Delete(object):

    def delete(self, obj):
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        self.client.delete("/%s/%s/" % (collection, obj.id), {})
        return obj
