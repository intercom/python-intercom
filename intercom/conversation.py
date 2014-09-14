from intercom.user import Resource
from intercom.api_operations.find import Find
from intercom.api_operations.load import Load


class Conversation(Resource, Find, Load):
    pass
