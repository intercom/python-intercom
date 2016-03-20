# -*- coding: utf-8 -*-

from intercom import job
from intercom.api_operations.all import All
from intercom.api_operations.bulk import LoadErrorFeed
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.service.base_service import BaseService


class Job(BaseService, All, Find, FindAll, Save, Load, LoadErrorFeed):

    @property
    def collection_class(self):
        return job.Job
