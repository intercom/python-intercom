# -*- coding: utf-8 -*-

from intercom import admin
from intercom.api_operations.all import All
from intercom.api_operations.find import Find
from intercom.service.base_service import BaseService


class Admin(BaseService, All, Find):

    @property
    def collection_class(self):
        return admin.Admin
