# -*- coding: utf-8 -*-
"""Service module for Conversations."""

from intercom import conversation
from intercom import utils
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.load import Load
from intercom.api_operations.save import Save
from intercom.service.base_service import BaseService


class Conversation(BaseService, Find, FindAll, Save, Load):
    """Service class for Conversations."""

    @property
    def collection(self):
        """Return the name of the collection."""
        return utils.resource_class_to_collection_name(self.collection_class)

    @property
    def collection_class(self):
        """Return the class of the collection."""
        return conversation.Conversation

    def resource_url(self, _id):
        """Return the URL for the specified resource in this collection."""
        return "/%s/%s/reply" % (self.collection, _id)

    def reply(self, **reply_data):
        """Reply to a message."""
        return self.__reply(reply_data)

    def assign(self, **reply_data):
        """Assign a conversation to a user."""
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'assignment'
        return self.__reply(reply_data)

    def open(self, **reply_data):
        """Mark a conversation as open."""
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'open'
        return self.__reply(reply_data)

    def close(self, **reply_data):
        """Mark a conversation as closed."""
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'close'
        return self.__reply(reply_data)

    def mark_read(self, _id):
        """Mark a conversation as read."""
        data = {'read': True}
        response = self.client.put(self.resource_url(_id), data)
        return self.collection_class().from_response(response)

    def __reply(self, reply_data):
        """Send requests to the resource handler."""
        _id = reply_data.pop('id')
        reply_data['conversation_id'] = _id
        response = self.client.post(self.resource_url(_id), reply_data)
        return self.collection_class().from_response(response)
