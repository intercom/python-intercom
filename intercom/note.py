# -*- coding: utf-8 -*-

from intercom.api_operations.find_all import FindAll
from intercom.api_operations.find import Find
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.traits.api_resource import Resource


class Note(Resource, Find, FindAll, Load, Save):
    pass
