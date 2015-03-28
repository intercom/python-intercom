# -*- coding: utf-8 -*-

import six

from intercom.api_operations.find import Find
from intercom.generic_handlers.count import Counter
from intercom.generic_handlers.base_handler import BaseHandler
from intercom.api_operations.count import Count as CountOperation
from intercom.traits.api_resource import Resource


@six.add_metaclass(BaseHandler)
class Count(Resource, Find, CountOperation, Counter):

    @classmethod
    def fetch_for_app(cls):
        return Count.find()

    @classmethod
    def do_broken_down_count(cls, entity_to_count, count_context):
        result = cls.fetch_broken_down_count(entity_to_count, count_context)
        return getattr(result, entity_to_count)[count_context]

    @classmethod
    def fetch_broken_down_count(cls, entity_to_count, count_context):
        return Count.find(type=entity_to_count, count=count_context)
