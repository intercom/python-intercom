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

    # @classmethod
    # def do_broken_down_count(cls, entity_to_count, count_context):
    #     result = cls.fetch_broken_down_count(entity_to_count, count_context)
    #     return getattr(result, entity_to_count)[count_context]

    # @classmethod
    # def fetch_broken_down_count(cls, entity_to_count, count_context):
    #     return Count.find(type=entity_to_count, count=count_context)
