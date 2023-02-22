# -*- coding: utf-8 -*-
from deprecated import deprecated

from intercom.traits.api_resource import Resource
from intercom.traits.incrementable_attributes import IncrementableAttributes


@deprecated(
    """Users is no longer available as a resource. 
    In order to see information and take action on users, 
    you should use the Contacts API."""
)
class User(Resource, IncrementableAttributes):

    update_verb = 'post'
    identity_vars = ['id', 'email', 'user_id']

    @property
    def flat_store_attributes(self):
        return ['custom_attributes']
