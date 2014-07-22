from intercom import Intercom
from intercom import utils


class Delete(object):

    def delete(self):
        collection = utils.resource_class_to_collection_name(self.__class__)
        Intercom.delete("/%s/%s/" % (collection, self.id))
        return self
