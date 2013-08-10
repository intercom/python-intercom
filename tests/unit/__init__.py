# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import json
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


def local_response(**params):
    def _call(*args, **kwargs):
        response = Mock()
        reply = {}
        for name, value in kwargs.items():
            reply[name] = value
        for name, value in params.items():
            reply[name] = value
        response.content = json.dumps(reply)
        response.status_code = 200
        return response
    return _call
