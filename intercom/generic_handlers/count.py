# -*- coding: utf-8 -*-

import re

count_breakdown_matcher = re.compile(r'(\w+)_counts_for_each_(\w+)')

class CountType(type):  # noqa

    def __getattr__(cls, name):  # noqa
        match = count_breakdown_matcher.search(name)
        if match:
            entity_to_count = match.group(1)
            count_context = match.group(2)
            return cls.do_broken_down_count(entity_to_count, count_context)
