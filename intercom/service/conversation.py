# -*- coding: utf-8 -*-

from intercom import conversation
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.service.base_service import BaseService


class Conversation(BaseService, Find, FindAll, Save, Load):

    @property
    def collection_class(self):
        return conversation.Conversation


#       def mark_read(id)
#         @client.put("/conversations/#{id}", read: true)
#       end

#       def reply(reply_data)
#         id = reply_data.delete(:id)
#         collection_name = Utils.resource_class_to_collection_name(collection_class)  # noqa
#         response = @client.post("/#{collection_name}/#{id}/reply", reply_data.merge(:conversation_id => id))  # noqa
#         collection_class.new.from_response(response)
#       end

#       def open(reply_data)
#         reply reply_data.merge(message_type: 'open', type: 'admin')
#       end

#       def close(reply_data)
#         reply reply_data.merge(message_type: 'close', type: 'admin')
#       end

#       def assign(reply_data)
#         assignee_id = reply_data.fetch(:assignee_id) { fail 'assignee_id is required' }  # noqa
#         reply reply_data.merge(message_type: 'assignment', assignee_id: assignee_id, type: 'admin')  # noqa
#       end
#     end
#   end
# end
