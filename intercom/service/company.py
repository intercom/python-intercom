# -*- coding: utf-8 -*-

from intercom import company
from intercom.api_operations.all import All
from intercom.api_operations.delete import Delete
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.extended_api_operations.users import Users
from intercom.extended_api_operations.tags import Tags
from intercom.service.base_service import BaseService


class Company(BaseService, All, Delete, Find, FindAll, Save, Load, Users, Tags):

    @property
    def collection_class(self):
        return company.Company

# require 'intercom/extended_api_operations/segments'
