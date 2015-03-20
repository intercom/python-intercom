# -*- coding: utf-8 -*-

from intercom.api_operations.find import Find
from intercom.api_operations.save import Save
from intercom.traits.api_resource import Resource


class Event(Resource, Save, Find):
    pass
