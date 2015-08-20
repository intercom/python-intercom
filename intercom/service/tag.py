# -*- coding: utf-8 -*-

from intercom import tag
from intercom.api_operations.all import All
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.service.base_service import BaseService


class Tag(BaseService, All, Find, FindAll, Save):

    @property
    def collection_class(self):
        return tag.Tag

    def tag(self, **params):
        params['tag_or_untag'] = 'tag'
        return self.create(**params)

    def untag(self, **params):
        params['tag_or_untag'] = 'untag'
        for user_or_company in self._users_or_companies(params):
            user_or_company['untag'] = True
        return self.create(**params)

    def _users_or_companies(self, params):
        if 'users' in params:
            return params['users']
        if 'companies' in params:
            return params['companies']
        return []
