from intercom import Intercom
from intercom import utils


class Load(object):

    def load(self):
        cls = self.__class__
        collection = utils.resource_class_to_collection_name(cls)
        if hasattr(self, 'id'):
            response = Intercom.get("/%s/%s" % (collection, self.id))
        else:
            raise Exception(
                "Cannot load %s as it does not have a valid id." % (cls))
        return cls(**response)
