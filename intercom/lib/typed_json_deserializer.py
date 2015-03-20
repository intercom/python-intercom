# -*- coding: utf-8 -*-

from intercom import utils


class JsonDeserializer(object):

    def __init__(self, json):
        self._json = json
        self._object_type = None

    @property
    def _get_object_type(self):
        if self._object_type is None:
            self._object_type = self._json.get('type', None)
            if self._object_type is None:
                raise Exception(
                    'No type field found to faciliate deserialization')
        return self._object_type

    @property
    def _is_list_type(self):
        return self._get_object_type.endswith('.list')

    @property
    def _object_entity_key(self):
        return utils.entity_key_from_type(self._get_object_type)

    def deserialize(self):
        if self._is_list_type:
            return self.deserialize_collection(
                self._json[self._object_entity_key])
        else:
            return self.deserialize_object(self._json)

    def deserialize_collection(self, collection_json):
        if collection_json is None:
            return []
        return [JsonDeserializer(object_json).deserialize()
                for object_json in collection_json]

    def deserialize_object(self, object_json):
        entity_class = utils.constantize_singular_resource_name(
            self._object_entity_key)
        return entity_class.from_api(object_json)
