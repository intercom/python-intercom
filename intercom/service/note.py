# -*- coding: utf-8 -*-

from intercom import note
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.service.base_service import BaseService


class Note(BaseService, Find, FindAll, Save, Load):

    @property
    def collection_class(self):
        return note.Note
