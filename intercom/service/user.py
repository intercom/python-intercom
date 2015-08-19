# -*- coding: utf-8 -*-

from intercom import user
from intercom.api_operations.all import All
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.delete import Delete
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.service.base_service import BaseService


class User(BaseService, All, Find, FindAll, Delete, Save, Load):

    @property
    def collection_class(self):
        return user.User
