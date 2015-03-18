import httpretty
import json
import re
import mock
import time

from describe import expect
from datetime import datetime
from intercom.collection_proxy import CollectionProxy
from intercom.lib.flat_store import FlatStore
from intercom.user import User
from intercom.utils import create_class_instance
from tests.unit import test_user


get = httpretty.GET
post = httpretty.POST
delete = httpretty.DELETE

r = re.compile


class DescribeIntercomUser:

    @httpretty.activate
    def it_raises_multiplematchingusers_error_when_receiving_a_conflict(self):
        multiple_matching_error = {
            'type': 'error.list',
            'errors': [
                {
                    'code': 'conflict',
                    'message': 'Multiple existing users match this email address - must be more specific using user_id'
                }
            ]
        }
        httpretty.register_uri(
            get, r("/users"),
            body=json.dumps(multiple_matching_error),
            status=400)
        print User.find(email='jo@example.com')
