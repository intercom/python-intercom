# -*- coding: utf-8 -*-

from intercom import company
from intercom.api_operations.all import All
from intercom.api_operations.find import Find
from intercom.api_operations.find_all import FindAll
from intercom.api_operations.save import Save
from intercom.api_operations.load import Load
from intercom.service.base_service import BaseService


class Company(BaseService, All, Find, FindAll, Save, Load):

    @property
    def collection_class(self):
        return company.Company

# require 'intercom/extended_api_operations/users'
# require 'intercom/extended_api_operations/tags'
# require 'intercom/extended_api_operations/segments'

# module Intercom
#   module Service
#     class Company < BaseService
#       include ApiOperations::Find
#       include ApiOperations::FindAll
#       include ApiOperations::Load
#       include ApiOperations::List
#       include ApiOperations::Save
#       include ExtendedApiOperations::Users
#       include ExtendedApiOperations::Tags
#       include ExtendedApiOperations::Segments

#       def collection_class
#         Intercom::Company
#       end
#     end
#   end
# end
