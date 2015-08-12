# -*- coding: utf-8 -*-

from intercom import utils


class Reply(object):

    def reply(self, **reply_data):
        return self.__reply(reply_data)

    def close_conversation(self, **reply_data):
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'close'
        return self.__reply(reply_data)

    def open_conversation(self, **reply_data):
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'open'
        return self.__reply(reply_data)

    def assign(self, **reply_data):
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'assignment'
        return self.__reply(reply_data)

    def __reply(self, reply_data):
        from intercom import Intercom
        collection = utils.resource_class_to_collection_name(self.__class__)
        url = "/%s/%s/reply" % (collection, self.id)
        reply_data['conversation_id'] = self.id
        response = Intercom.post(url, **reply_data)
        return self.from_response(response)
