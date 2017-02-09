# -*- coding: utf-8 -*-

from intercom import count
from intercom.api_operations.find import Find
from intercom.service.base_service import BaseService


class Count(BaseService, Find):

    @property
    def collection_class(self):
        return count.Count

    def for_app(self):
        return self.find()

    def for_type(self, type, count=None):
        return self.find(type=type, count=count)
