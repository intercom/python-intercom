# -*- coding: utf-8 -*-  # noqa

from intercom import lead
from intercom.api_operations.all import All
from intercom.api_operations.convert import Convert
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.delete import Delete
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.service.base_service import BaseService


class Lead(BaseService, All, Find, FindAll, Delete, Save, Load, Convert):
    """Leads are useful for representing logged-out users of your application.

    Ref: https://developers.intercom.io/reference#leads
    """

    @property
    def collection_class(self):
        """The collection class that represents this resource."""
        return lead.Lead
