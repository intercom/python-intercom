# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import httpretty
import os
import re

DIRPATH = os.path.dirname(__file__)
FIXTURES = os.path.join(DIRPATH, 'fixtures')

from intercom import AuthenticationError
from intercom import BadGatewayError
from intercom import ResourceNotFound
from intercom import ServerError
from intercom import ServiceUnavailableError
from intercom import Intercom
from intercom import User
from intercom import MessageThread
from intercom import Impression
from intercom import Note
from nose.tools import nottest
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import raises

Intercom.app_id = 'dummy-app-id'
Intercom.api_key = 'dummy-secret-key'

get = httpretty.GET
post = httpretty.POST
put = httpretty.PUT
delete = httpretty.DELETE
r = re.compile


def fixture(fixture):
    fixture_path = os.path.join(
        FIXTURES, '%(fixture)s.json' % {'fixture': fixture})
    return open(fixture_path).read()


@httpretty.activate
def test_users():
    httpretty.register_uri(get, r(r"/v1/users"), body=fixture('v1-users'))
    ok_(len(User.all()) > 0)


@httpretty.activate
def test_user():
    httpretty.register_uri(
        get, r(r"/v1/users\?email="),
        body=fixture('v1-user'), match_querystring=True)
    user = User.find(email='somebody@example.com')
    eq_(user.name, 'Somebody')

    httpretty.register_uri(
        get, r(r"/v1/users\?user_id="),
        body=fixture('v1-user'), match_querystring=True)
    user = User.find_by_user_id('123')
    eq_(user.name, 'Somebody')


@httpretty.activate
@raises(ResourceNotFound)
def test_not_found():
    httpretty.register_uri(
        get, r(r"/v1/users\?email=not-found"),
        status=404, match_querystring=True)
    User.find(email='not-found@example.com')


@httpretty.activate
@raises(ResourceNotFound)
def test_not_found_qs():
    httpretty.register_uri(
        get, r(r"/v1/users\?email=not-found"),
        body=fixture('v1-user_not_found'), status=404, match_querystring=True)
    User.find(email='not-found@example.com')


@httpretty.activate
@raises(ServerError)
def test_server_error():
    httpretty.register_uri(
        get, r(r"/v1/users\?email=server-error"),
        status=500, match_querystring=True)
    User.find(email='server-error@example.com')


@httpretty.activate
@raises(ServerError)
def test_server_error_qs():
    httpretty.register_uri(
        get, r(r"/v1/users\?email=server-error"),
        body=fixture('v1-user_server_error'), status=500,
        match_querystring=True)
    User.find(email='server-error@example.com')


@httpretty.activate
@raises(AuthenticationError)
def test_bad_api_key():
    httpretty.register_uri(
        get, r(r"/v1/users\?email=authentication-error"),
        status=401, match_querystring=True)
    Intercom.app_id = 'bad-app-id'
    Intercom.api_key = 'bad-secret-key'
    User.find(email='authentication-error@example.com')


@httpretty.activate
def test_message_threads():
    httpretty.register_uri(
        get, r(r"/v1/users/message_threads\?email=somebody"),
        body=fixture('v1-users-message_threads'), match_querystring=True)
    thread = MessageThread.find_all(email='somebody@example.com')[0]
    for attr in ['thread_id', 'read', 'messages', 'created_at', 'updated_at']:
        ok_(getattr(thread, attr))


@nottest
@httpretty.activate
def test_message_thread():
    httpretty.register_uri(
        get, r(r"/v1/users/message_threads\?email=somebody"),
        body=fixture('v1-users-message_threads'), match_querystring=True)
    httpretty.register_uri(
        get, r(r"/v1/users/message_threads"),
        body=fixture('v1-users-message_thread'))
    thread = MessageThread.find_all(email='somebody@example.com')[0]
    thread.mark_as_read()


@httpretty.activate
def test_impression():
    httpretty.register_uri(
        post, r(r"/v1/users/impressions"),
        body=fixture('v1-users-impressions'))
    impression = Impression.create(email='somebody@example.com')
    ok_(impression.unread_messages > 0)
    # eq_(impression.email, 'somebody@example.com')


@httpretty.activate
def test_note():
    httpretty.register_uri(
        post, r(r"/v1/users/notes"),
        body=fixture('v1-users-note'))
    note = Note.create(body="This is a note", email='somebody@example.com')
    eq_(note.html, "<p>This is a note</p>")
    eq_(note.user.email, "somebody@example.com")


@nottest
@httpretty.activate
def test_endpoints():
    # FakeWeb.allow_net_connect = %r(127.0.0.7)
    httpretty.register_uri(
        get, r(r"/v1/users\?email="),
        body=fixture('v1-user'), match_querystring=True)
    Intercom.endpoints = ("http://127.0.0.7", "https://api.intercom.io")
    user = User.find(email='somebody@example.com')
    eq_(user.name, 'Somebody')


@nottest
@httpretty.activate
def test_unreachable_endpoints():
    class ServiceUnavailableError(Exception):
        pass
    httpretty.register_uri(
        get, r(r"example\.com"),
        body=fixture('v1-user'), status=503)
    Intercom.endpoints = ("http://example.com")
    User.find.when.called_with(email='somebody@example.com')\
        .should.throw(ServiceUnavailableError)
    Intercom.endpoints = ("http://example.com", "http://api.example.com")
    User.find.when.called_with(email='not-found@example.com')\
        .should.throw(ServiceUnavailableError)


@httpretty.activate
@raises(ServiceUnavailableError)
def test_unreachable():
    httpretty.register_uri(
        get, r(r"/v1/users\?email="),
        status=503, match_querystring=True)
    User.find(email='somebody@example.com')


@nottest
@httpretty.activate
def test_bad_gateway_endpoints():
    class BadGatewayError(Exception):
        pass
    httpretty.register_uri(
        get, r(r"example\.com"),
        body=fixture('v1-user'), status=502)
    Intercom.endpoints = ("http://example.com")
    User.find.when.called_with(email='somebody@example.com')\
        .should.throw(BadGatewayError)
    Intercom.endpoints = ("http://example.com", "http://api.example.com")
    User.find.when.called_with(email='not-found@example.com')\
        .should.throw(BadGatewayError)


@httpretty.activate
@raises(BadGatewayError)
def test_bad_gateway():
    httpretty.register_uri(
        get, r(r"/v1/users\?email="),
        status=502, match_querystring=True)
    User.find(email='somebody@example.com')


@httpretty.activate
def test_doctest():
    import doctest

    def request_callback(method, uri, headers):
        parsed_body = httpretty.last_request().parsed_body
        # handle the user updates
        if 'name' in parsed_body:
            return (200, headers, fixture('v1-user-updated'))
        return (200, headers, fixture('v1-user'))

    httpretty.register_uri(
        get, r(r'/v1/users$'),
        body=fixture('v1-users'), match_querystring=True)
    httpretty.register_uri(
        get, r(r'/v1/users\?page=1'),
        body=fixture('v1-users'), match_querystring=True)
    httpretty.register_uri(
        post, r(r'/v1/users$'),
        body=fixture('v1-user'), match_querystring=True)
    httpretty.register_uri(
        put, r(r'/v1/users$'),
        body=request_callback, match_querystring=True)
    httpretty.register_uri(
        delete, r(r'/v1/users$'),
        body=fixture('v1-user'), match_querystring=True)
    httpretty.register_uri(
        get, r(r"/v1/users\?email=somebody"),
        body=fixture('v1-user'), match_querystring=True)
    httpretty.register_uri(
        get, r(r"/v1/users\?user_id=123"),
        body=fixture('v1-user'), match_querystring=True)
    httpretty.register_uri(
        get, r(r"/v1/users\?email=not-found"),
        status=404, match_querystring=True)
    httpretty.register_uri(
        get, r(r"/v1/users\?email=server-error"),
        status=500, match_querystring=True)
    httpretty.register_uri(
        get, r(r"/v1/users\?email=authentication-error"),
        status=401, match_querystring=True)

    httpretty.register_uri(
        get, r(r"/v1/tags\?name=Free"),
        body=fixture('v1-tag'))
    httpretty.register_uri(
        get, r(r"/v1/tags"),
        body=fixture('v1-tag'))
    httpretty.register_uri(
        post, r(r"/v1/tags"),
        body=fixture('v1-tag'))
    httpretty.register_uri(
        put, r(r"/v1/tags"),
        body=fixture('v1-tag'))

    httpretty.register_uri(
        post, r(r"/v1/users/notes"),
        body=fixture('v1-users-note'))

    httpretty.register_uri(
        get, r(r'/v1/users/message_threads$'),
        body=fixture('v1-users-message_threads'), match_querystring=True)
    httpretty.register_uri(
        post, r(r'/v1/users/message_threads$'),
        body=fixture('v1-users-message_thread'), match_querystring=True)
    httpretty.register_uri(
        put, r(r'/v1/users/message_threads$'),
        body=fixture('v1-users-message_thread'), match_querystring=True)
    httpretty.register_uri(
        get, r(r"/v1/users/message_threads\?thread_id=5591"),
        body=fixture('v1-users-message_thread'), match_querystring=True)
    httpretty.register_uri(
        get, r(r"/v1/users/message_threads\?email=somebody"),
        body=fixture('v1-users-message_threads'), match_querystring=True)

    httpretty.register_uri(
        post, r(r"/v1/users/impressions"),
        body=fixture('v1-users-impressions'))

    (failure_count, test_count) = doctest.testfile(
        "../../intercom/user.py")
    eq_(failure_count, 0)

    (failure_count, test_count) = doctest.testfile(
        "../../intercom/tag.py")
    eq_(failure_count, 0)

    (failure_count, test_count) = doctest.testfile(
        "../../intercom/note.py")
    eq_(failure_count, 0)

    (failure_count, test_count) = doctest.testfile(
        "../../intercom/message_thread.py")
    eq_(failure_count, 0)

    (failure_count, test_count) = doctest.testfile(
        "../../intercom/impression.py")
    eq_(failure_count, 0)

    (failure_count, test_count) = doctest.testfile(
        "../../intercom/intercom.py")
    eq_(failure_count, 0)
