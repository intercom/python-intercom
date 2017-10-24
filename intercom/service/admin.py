# -*- coding: utf-8 -*-

from intercom import admin
from intercom.api_operations.all import All
from intercom.service.base_service import BaseService


class Admin(BaseService, All):

    @property
    def collection_class(self):
        return admin.Admin
