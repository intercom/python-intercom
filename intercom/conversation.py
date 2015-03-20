# -*- coding: utf-8 -*-

from intercom.api_operations.find_all import FindAll
from intercom.api_operations.find import Find
from intercom.api_operations.load import Load
from intercom.api_operations.save import Save
from intercom.extended_api_operations.reply import Reply
from intercom.traits.api_resource import Resource


class Conversation(Resource, FindAll, Find, Load, Save, Reply):
    pass
