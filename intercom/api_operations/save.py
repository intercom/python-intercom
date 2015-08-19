# -*- coding: utf-8 -*-

from intercom import utils


class Save(object):

    def create(self, **params):
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        response = self.client.post("/%s/" % (collection), params)
        if response:  # may be empty if we received a 202
            return self.collection_class(**response)

    # def from_dict(self, pdict):
    #     for key, value in list(pdict.items()):
    #         setattr(self, key, value)

    # @property
    # def to_dict(self):
    #     a_dict = {}
    #     for name in list(self.__dict__.keys()):
    #         if name == "changed_attributes":
    #             continue
    #         a_dict[name] = self.__dict__[name]  # direct access
    #     return a_dict

    # @classmethod
    # def from_api(cls, response):
    #     obj = cls()
    #     obj.from_response(response)
    #     return obj

    # def from_response(self, response):
    #     self.from_dict(response)
    #     return self

    def save(self, obj):
        collection = utils.resource_class_to_collection_name(
            self.collection_class)
        params = obj.attributes
        if hasattr(obj, 'id_present') and not hasattr(obj, 'posted_updates'):
            # update
            response = self.client.put('/%s/%s' % (collection, obj.id), params)
        else:
            # create
            params.update(self.identity_hash(obj))
            response = self.client.post('/%s' % (collection), params)
        if response:
            return obj.from_response(response)

    @property
    def id_present(self):
        return getattr(self, 'id', None) and self.id != ""

    @property
    def posted_updates(self):
        return getattr(self, 'update_verb', None) == 'post'

    def identity_hash(self, obj):
        identity_vars = getattr(obj, 'identity_vars', [])
        parts = {}
        for var in identity_vars:
            id_var = getattr(obj, var, None)
            if id_var:  # only present id var if it is not blank or None
                parts[var] = id_var
        return parts
