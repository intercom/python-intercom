from intercom.api_operations.all import All
from intercom.api_operations.count import Count
from intercom.api_operations.delete import Delete
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.load import Load
from intercom.api_operations.save import Save
from intercom.traits.api_resource import Resource
from intercom.traits.incrementable_attributes import IncrementableAttributes


class User(Resource, Find, FindAll, All, Count, Load, Save, Delete,
           IncrementableAttributes):

    @property
    def flat_store_attributes(self):
        return ['custom_attributes']
