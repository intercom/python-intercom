# -*- coding: utf-8 -*-

from intercom.api_operations.find import Find
from intercom.api_operations.delete import Delete
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.traits.api_resource import Resource


class Subscription(Resource, Find, FindAll, Save, Delete):
    pass
