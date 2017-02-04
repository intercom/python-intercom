# -*- coding: utf-8 -*-

from intercom import message
from intercom.api_operations.save import Save
from intercom.service.base_service import BaseService


class Message(BaseService, Save):

    @property
    def collection_class(self):
        return message.Message
