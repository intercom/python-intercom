# -*- coding: utf-8 -*-

from intercom.api_operations.all import All
from intercom.api_operations.count import Count
from intercom.api_operations.find import Find
from intercom.api_operations.save import Save
from intercom.traits.api_resource import Resource


class Segment(Resource, Find, Count, Save, All):
    pass
