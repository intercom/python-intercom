# -*- coding: utf-8 -*-

import re


class FindAllHandler():
    def __init__(self, entity, context):
        self.entity = entity
        self.context = context

    def __call__(self, *args, **kwargs):
        return self.entity._find_all_for(
            self.context, *args, **kwargs)


class TagFindAll():

    find_matcher = re.compile(r'find_all_for_(\w+)')

    @classmethod
    def handles_attr(cls, name):
        return cls.find_matcher.search(name) is not None

    @classmethod
    def _get(cls, entity, name):
        match = cls.find_matcher.search(name)
        context = match.group(1)
        return FindAllHandler(entity, context)

    @classmethod
    def _find_all_for(cls, taggable_type, **kwargs):
        params = {
            'taggable_type': taggable_type
        }
        res_id = kwargs.pop('id', None)
        if res_id:
            params['taggable_id'] = res_id
        params.update(kwargs)

        return cls.find_all(**params)
