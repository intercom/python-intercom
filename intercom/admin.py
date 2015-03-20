from intercom.traits.api_resource import Resource
from intercom.api_operations.all import All
from intercom.api_operations.find import Find


class Admin(Resource, Find, All):
    pass
