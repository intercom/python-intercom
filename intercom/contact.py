# -*- coding: utf-8 -*-

from intercom.traits.api_resource import Resource
from intercom.traits.incrementable_attributes import IncrementableAttributes


class Contact(Resource, IncrementableAttributes):

    collection_name = 'contacts'
    update_verb = 'put'
    identity_vars = ['id', 'email', 'workspace_id', 'external_id']

    @property
    def flat_store_attributes(self):
        return ['custom_attributes']
