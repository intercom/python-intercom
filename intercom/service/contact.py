# -*- coding: utf-8 -*-

from intercom import contact
from intercom.api_operations.all import All
from intercom.api_operations.bulk import Submit
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.search import Search
from intercom.api_operations.delete import Delete
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.extended_api_operations.tags import Tags
from intercom.service.base_service import BaseService


class Contact(BaseService, All, Find, FindAll, Delete, Save, Load, Submit, Tags, Search):

    @property
    def collection_class(self):
        return contact.Contact
