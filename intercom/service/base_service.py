# -*- coding: utf-8 -*-


class BaseService(object):

    def __init__(self, client):
        self.client = client

    @property
    def collection_class(self):
        raise NotImplementedError

    def from_api(self, api_response):
        obj = self.collection_class()
        obj.from_response(api_response)
        return obj
