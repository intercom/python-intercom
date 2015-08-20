# -*- coding: utf-8 -*-

from intercom import conversation
from intercom import utils
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.service.base_service import BaseService


class Conversation(BaseService, Find, FindAll, Save, Load):

    @property
    def collection_class(self):
        return conversation.Conversation

    def reply(self, **reply_data):
        return self.__reply(reply_data)

    def assign(self, **reply_data):
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'assignment'
        return self.__reply(reply_data)

    def open(self, **reply_data):
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'open'
        return self.__reply(reply_data)

    def close(self, **reply_data):
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'close'
        return self.__reply(reply_data)

    def __reply(self, reply_data):
        _id = reply_data.pop('id')
        collection = utils.resource_class_to_collection_name(self.collection_class)  # noqa
        url = "/%s/%s/reply" % (collection, _id)
        reply_data['conversation_id'] = _id
        response = self.client.post(url, reply_data)
        return self.collection_class().from_response(response)


#       def mark_read(id)
#         @client.put("/conversations/#{id}", read: true)
#       end
