from intercom.user import Resource
from intercom.api_operations.count import Count
from intercom.api_operations.find import Find
from intercom.api_operations.load import Load


class Company(Resource, Count, Find, Load):
    update_verb = 'post'
    identity_vars = ['id', 'company_id']
