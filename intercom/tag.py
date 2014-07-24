from intercom.user import Resource
from intercom.api_operations.count import Count
from intercom.api_operations.find import Find
from intercom.api_operations.save import Save


class Tag(Resource, Find, Count, Save):
    pass
