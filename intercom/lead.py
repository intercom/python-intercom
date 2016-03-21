# -*- coding: utf-8 -*-

from intercom.traits.api_resource import Resource


class Lead(Resource):

    update_verb = 'put'
    identity_vars = ['email', 'user_id']
    collection_name = 'contacts'

    @property
    def flat_store_attributes(self):
        return ['custom_attributes']
