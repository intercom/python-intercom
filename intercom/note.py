from intercom.user import Resource
from intercom.api_operations.find import Find
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load


class Note(Resource, Find, Load, Save):
    pass
