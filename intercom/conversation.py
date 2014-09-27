from intercom.user import Resource
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.find import Find
from intercom.api_operations.load import Load
from intercom.api_operations.save import Save


class Conversation(Resource, FindAll, Find, Load, Save):
    pass
