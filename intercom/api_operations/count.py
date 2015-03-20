# -*- coding: utf-8 -*-

from intercom import utils


class Count(object):

    @classmethod
    def count(cls):
        from intercom import Intercom
        response = Intercom.get("/counts/")
        return response[utils.resource_class_to_name(cls)]['count']
