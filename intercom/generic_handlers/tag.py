# -*- coding: utf-8 -*-

from intercom import utils


class TagHandler():
    def __init__(self, entity, name, context):
        self.entity = entity
        self.untag = name == "untag"
        self.context = context

    def __call__(self, *args, **kwargs):
        return self.entity._tag_collection(
            self.context, *args, untag=self.untag, **kwargs)


class TagUntag():

    @classmethod
    def handles_attr(cls, name):
        name, context = name.split('_', 1)
        if name in ["tag", "untag"]:
            return True

    @classmethod
    def _get(cls, entity, name):
        name, context = name.split('_', 1)
        return TagHandler(entity, name, context)

    @classmethod
    def _tag_collection(
            cls, collection_name, name, objects, untag=False):
        from intercom import Intercom
        collection = utils.resource_class_to_collection_name(cls)
        object_ids = []
        for obj in objects:
            if not hasattr(obj, 'keys'):
                obj = {'id': obj}
            if untag:
                obj['untag'] = True
            object_ids.append(obj)

        params = {
            'name': name,
            collection_name: object_ids,
        }
        response = Intercom.post("/%s" % (collection), **params)
        return cls(**response)
