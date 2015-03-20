# -*- coding: utf-8 -*-

from intercom import utils


class Reply(object):

    @property
    def reply(self, reply_data):
        from intercom import Intercom
        collection = utils.resource_class_to_collection_name(self.__class__)
        url = "/%s/%s/reply" % (collection, self.id)
        reply_data['conversation_id'] = self.id
        response = Intercom.post(url, reply_data)
        return self.from_response(response)
