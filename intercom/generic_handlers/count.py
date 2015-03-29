# -*- coding: utf-8 -*-

import re


class Counter():

    count_breakdown_matcher = re.compile(r'(\w+)_counts_for_each_(\w+)')

    @classmethod
    def handles_attr(cls, name):
        return cls.count_breakdown_matcher.search(name) is not None

    @classmethod
    def _get(cls, entity, name):
        match = cls.count_breakdown_matcher.search(name)
        entity_to_count = match.group(1)
        count_context = match.group(2)
        return entity.do_broken_down_count(entity_to_count, count_context)
