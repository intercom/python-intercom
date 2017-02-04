# -*- coding: utf-8 -*-
"""Operation to retrieve count for a particular resource."""

from intercom import utils


class Count(object):
    """A mixin that provides `count` functionality."""

    @classmethod
    def count(cls):
        """Return the count for the resource."""
        from intercom import Intercom
        response = Intercom.get("/counts/")
        return response[utils.resource_class_to_name(cls)]['count']
