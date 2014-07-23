from intercom.user import Resource
from intercom.api_operations.count import Count
from intercom.api_operations.find import Find

class Segment(Resource, Find, Count):
    pass
