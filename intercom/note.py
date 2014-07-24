from intercom.user import Resource
from intercom.api_operations.find import Find
from intercom.api_operations.save import Save


class Note(Resource, Find, Save):
    pass
