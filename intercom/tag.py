from intercom.user import Resource
from intercom.api_operations.count import Count
from intercom.api_operations.find import Find


class Tag(Resource, Find, Count):
    pass
