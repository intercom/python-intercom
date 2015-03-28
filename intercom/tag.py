# -*- coding: utf-8 -*-

import six

from intercom.api_operations.all import All
from intercom.api_operations.count import Count
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.generic_handlers.base_handler import BaseHandler
from intercom.generic_handlers.tag import TagUntag
from intercom.generic_handlers.tag_find_all import TagFindAll
from intercom.traits.api_resource import Resource


@six.add_metaclass(BaseHandler)
class Tag(Resource, All, Count, Find, FindAll, Save, TagUntag, TagFindAll):
    pass
