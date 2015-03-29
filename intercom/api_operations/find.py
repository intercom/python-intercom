# -*- coding: utf-8 -*-

from intercom import HttpError
from intercom import utils


class Find(object):

    @classmethod
    def find(cls, **params):
        from intercom import Intercom
        collection = utils.resource_class_to_collection_name(cls)
        if 'id' in params:
            response = Intercom.get("/%s/%s" % (collection, params['id']))
        else:
            response = Intercom.get("/%s" % (collection), **params)

        if response is None:
            raise HttpError('Http Error - No response entity returned')

        return cls(**response)
