# -*- coding: utf-8 -*-
from deprecated import deprecated

from intercom import user
from intercom.api_operations.all import All
from intercom.api_operations.bulk import Submit
from intercom.api_operations.delete import Delete
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.load import Load
from intercom.api_operations.save import Save
from intercom.api_operations.scroll import Scroll
from intercom.extended_api_operations.tags import Tags
from intercom.service.base_service import BaseService


@deprecated(
    """Users is no longer available as a resource. 
    In order to see information and take action on users, 
    you should use the Contacts API."""
)
class User(BaseService, All, Find, FindAll, Delete, Save, Load, Submit, Tags, Scroll):

    @property
    def collection_class(self):
        return user.User
