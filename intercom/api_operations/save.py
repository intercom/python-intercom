# -*- coding: utf-8 -*-

from intercom import utils


class Save(object):

    @classmethod
    def create(cls, **params):
        from intercom import Intercom
        collection = utils.resource_class_to_collection_name(cls)
        response = Intercom.post("/%s/" % (collection), **params)
        if response:  # may be empty if we received a 202
            return cls(**response)

    def from_dict(self, pdict):
        for key, value in list(pdict.items()):
            setattr(self, key, value)

    @property
    def to_dict(self):
        a_dict = {}
        for name in list(self.__dict__.keys()):
            if name == "changed_attributes":
                continue
            a_dict[name] = self.__dict__[name]  # direct access
        return a_dict

    @classmethod
    def from_api(cls, response):
        obj = cls()
        obj.from_response(response)
        return obj

    def from_response(self, response):
        self.from_dict(response)
        return self

    def save(self):
        from intercom import Intercom
        collection = utils.resource_class_to_collection_name(self.__class__)
        params = self.attributes
        if self.id_present and not self.posted_updates:
            # update
            response = Intercom.put('/%s/%s' % (collection, self.id), **params)
        else:
            # create
            params.update(self.identity_hash)
            response = Intercom.post('/%s' % (collection), **params)
        if response:
            return self.from_response(response)

    @property
    def id_present(self):
        return getattr(self, 'id', None) and self.id != ""

    @property
    def posted_updates(self):
        return getattr(self, 'update_verb', None) == 'post'

    @property
    def identity_hash(self):
        identity_vars = getattr(self, 'identity_vars', [])
        parts = {}
        for var in identity_vars:
            id_var = getattr(self, var, None)
            if id_var:  # only present id var if it is not blank or None
                parts[var] = id_var
        return parts
