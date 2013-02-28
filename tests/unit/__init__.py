# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import os

from mock import Mock

DIRPATH = os.path.dirname(__file__)
FIXTURES = os.path.join(DIRPATH, 'fixtures')

def create_response(status, fixture=None):
    def request(*args, **kwargs):
        response = Mock()
        response.status_code = status
        if fixture:
            fixture_path = os.path.join(FIXTURES, fixture)
            response.content = open(fixture_path).read()
        return response
    return request
