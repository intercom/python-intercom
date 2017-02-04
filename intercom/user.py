# -*- coding: utf-8 -*-

from intercom.traits.api_resource import Resource
from intercom.traits.incrementable_attributes import IncrementableAttributes


class User(Resource, IncrementableAttributes):

    update_verb = 'post'
    identity_vars = ['id', 'email', 'user_id']

    @property
    def flat_store_attributes(self):
        return ['custom_attributes']
