from intercom import Intercom
from intercom import utils


class Count(object):

    @classmethod
    def count(cls):
        response = Intercom.get("/counts/")
        return response[utils.resource_class_to_name(cls)]['count']
