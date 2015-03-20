# -*- coding: utf-8 -*-

from intercom.api_operations.all import All
from intercom.api_operations.find import Find
from intercom.traits.api_resource import Resource


class Admin(Resource, Find, All):
    pass
