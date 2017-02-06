# -*- coding: utf-8 -*-

from intercom import event
from intercom.api_operations.bulk import Submit
from intercom.api_operations.save import Save
from intercom.api_operations.find_all import FindAll
from intercom.service.base_service import BaseService
from intercom.collection_proxy import CollectionProxy


class EventCollectionProxy(CollectionProxy):

    def paging_info_present(self, response):
        return 'pages' in response and 'next' in response['pages']


class Event(BaseService, Save, Submit, FindAll):

    proxy_class = EventCollectionProxy

    @property
    def collection_class(self):
        return event.Event
