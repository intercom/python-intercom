# -*- coding: utf-8 -*-

from intercom import segment
from intercom.api_operations.all import All
from intercom.api_operations.find import Find
from intercom.service.base_service import BaseService


class Segment(BaseService, All, Find):

    @property
    def collection_class(self):
        return segment.Segment
