# -*- coding: utf-8 -*-

from intercom.api_operations.save import Save
from intercom.traits.api_resource import Resource


class Message(Resource, Save):
    pass
