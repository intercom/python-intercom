from intercom import Intercom
from intercom import utils


class Save(object):

    @classmethod
    def create(cls, **params):
        collection = utils.resource_class_to_collection_name(cls)
        response = Intercom.post("/%s/" % (collection), **params)
        return cls(**response)

    def from_dict(self, pdict):
        for key, value in pdict.items():
            setattr(self, key, value)

    @property
    def to_dict(self):
        a_dict = {}
        for name in self.attributes.keys():
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
        collection = utils.resource_class_to_collection_name(self.__class__)
        params = self.__dict__
        if self.id_present:
            # update
            response = Intercom.put('/%s/%s' % (collection, self.id), **params)
        else:
            # create
            response = Intercom.post('/%s' % (collection), **params)
        if response:
            return self.from_response(response)

    @property
    def id_present(self):
        return getattr(self, 'id', None) and self.id != ""

    @property
    def posted_updates(self):
        return getattr(self, 'update_verb', None) != 'post'

    @property
    def identity_hash(self):
        identity_vars = getattr(self, 'identity_vars', None)
        if identity_vars:
            return {}
