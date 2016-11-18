# -*- coding: utf-8 -*-
"""Operations to manage conversations."""

from intercom import utils


class Reply(object):
    """A mixin that provides methods to manage a conversation.

    This includes opening and closing them, assigning them to users, and
    replying them.
    """

    def reply(self, **reply_data):
        """Add a reply, created from the supplied paramters, to the conversation."""
        return self.__reply(reply_data)

    def close_conversation(self, **reply_data):
        """Close the conversation."""
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'close'
        return self.__reply(reply_data)

    def open_conversation(self, **reply_data):
        """Open the conversation."""
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'open'
        return self.__reply(reply_data)

    def assign(self, **reply_data):
        """Assign the conversation to an admin user."""
        reply_data['type'] = 'admin'
        reply_data['message_type'] = 'assignment'
        return self.__reply(reply_data)

    def __reply(self, reply_data):
        """Send the Conversation requests to Intercom and handl the responses."""
        from intercom import Intercom
        collection = utils.resource_class_to_collection_name(self.__class__)
        url = "/%s/%s/reply" % (collection, self.id)
        reply_data['conversation_id'] = self.id
        response = Intercom.post(url, **reply_data)
        return self.from_response(response)
