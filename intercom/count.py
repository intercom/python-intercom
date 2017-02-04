# -*- coding: utf-8 -*-

from intercom.traits.api_resource import Resource


class Count(Resource):
    pass

    # @classmethod
    # def fetch_for_app(cls):
    #     return Count.find()

    # @classmethod
    # def do_broken_down_count(cls, entity_to_count, count_context):
    #     result = cls.fetch_broken_down_count(entity_to_count, count_context)
    #     return getattr(result, entity_to_count)[count_context]

    # @classmethod
    # def fetch_broken_down_count(cls, entity_to_count, count_context):
    #     return Count.find(type=entity_to_count, count=count_context)
