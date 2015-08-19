# -*- coding: utf-8 -*-

from intercom.traits.api_resource import Resource


class Company(Resource):
    update_verb = 'post'
    identity_vars = ['id', 'company_id']

    @property
    def flat_store_attributes(self):
        return ['custom_attributes']
