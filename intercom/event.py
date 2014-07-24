from intercom.user import Resource
from intercom.api_operations.find import Find
from intercom.api_operations.save import Save


class Event(Resource, Save, Find):
    pass
