# -*- coding: utf-8 -*-

from intercom import subscription
from intercom.api_operations.all import All
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.api_operations.delete import Delete
from intercom.service.base_service import BaseService


class Subscription(BaseService, All, Find, FindAll, Save, Delete):

    @property
    def collection_class(self):
        return subscription.Subscription
