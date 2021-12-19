# -*- coding: utf-8 -*-

from intercom.traits.api_resource import Resource
from intercom.traits.incrementable_attributes import IncrementableAttributes


class Contact(Resource, IncrementableAttributes):

    update_verb = 'post'
    identity_vars = ['id', 'email', 'external_id']

    @property
    def flat_store_attributes(self):
        return ['custom_attributes']
