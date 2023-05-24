# -*- coding: utf-8 -*-

from intercom import user
from intercom.api_operations.all import All
from intercom.api_operations.bulk import Submit
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.delete import Delete
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.api_operations.scroll import Scroll
from intercom.extended_api_operations.tags import Tags
from intercom.service.base_service import BaseService


class User(BaseService, All, Find, FindAll, Delete, Save, Load, Submit, Tags, Scroll):

    @property
    def collection_class(self):
        return user.User

    def archive(self, obj):
        """Archive a user. This used to be called 'delete', but now is called 'archive'."""
        return self.delete(obj)

    def permanent_delete(self, intercom_user_id):
        """Request permanent deletion of a user."""
        response = self.client.post('/user_delete_requests', {'intercom_user_id': intercom_user_id})
        return response['id']
