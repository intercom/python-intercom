# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import httpretty, os, re

DIRPATH = os.path.dirname(__file__)
FIXTURES = os.path.join(DIRPATH, 'fixtures')

from intercom import AuthenticationError
from intercom import ResourceNotFound
from intercom import ServerError
from intercom import Intercom
from intercom import User
from intercom import MessageThread
from intercom import Impression
from intercom import Note
from nose.tools import nottest
from sure import expect

Intercom.app_id = 'dummy-app-id'
Intercom.api_key = 'dummy-secret-key'

get = httpretty.GET
post = httpretty.POST
r = re.compile

def fixture(fixture):
    fixture_path = os.path.join(FIXTURES, '%(fixture)s.json' % {'fixture': fixture})
    return open(fixture_path).read()

@httpretty.activate
def test_users():
    httpretty.register_uri(
        httpretty.GET, 
        re.compile(r"/v1/users"),
        body=fixture('v1-users'))
    expect(len(User.all())).should.be.greater_than(0)

@httpretty.activate
def test_user():
    httpretty.register_uri(get, r(r"/v1/users\?email="), body=fixture('v1-user'), match_querystring=True)
    user = User.find(email='somebody@example.com')
    expect(user.name).to.equal('Somebody')

@httpretty.activate
def test_not_found():
    httpretty.register_uri(get, r(r"/v1/users\?email=not-found"), status=404, match_querystring=True)
    User.find.when.called_with(email='not-found@example.com').should.throw(ResourceNotFound)

@httpretty.activate
def test_server_error():
    httpretty.register_uri(get, r(r"/v1/users\?email=server-error"), status=500, match_querystring=True)
    User.find.when.called_with(email='server-error@example.com').should.throw(ServerError)

@httpretty.activate
def test_bad_api_key():
    httpretty.register_uri(get, r(r"/v1/users\?email=authentication-error"), status=401, match_querystring=True)
    Intercom.app_id = 'bad-app-id'
    Intercom.api_key = 'bad-secret-key'
    User.find.when.called_with(email='authentication-error@example.com').should.throw(AuthenticationError)

@httpretty.activate
def test_message_threads():
    httpretty.register_uri(get, r(r"/v1/users/message_threads\?email=somebody"), body=fixture('v1-users-message_threads'), match_querystring=True)
    thread = MessageThread.find_all(email='somebody@example.com')[0]
    for attr in ['thread_id', 'read', 'messages', 'created_at', 'updated_at']:
        expect(getattr(thread, attr)).should.be.ok

@nottest
@httpretty.activate
def test_message_thread():
    httpretty.register_uri(get, r(r"/v1/users/message_threads\?email=somebody"), body=fixture('v1-users-message_threads'), match_querystring=True)
    httpretty.register_uri(get, r(r"/v1/users/message_threads"), body=fixture('v1-users-message_thread'))
    thread = MessageThread.find_all(email='somebody@example.com')[0]
    thread.mark_as_read()

@httpretty.activate
def test_impression():
    httpretty.register_uri(post, r(r"/v1/users/impressions"), body=fixture('v1-users-impressions'))
    impression = Impression.create(email='somebody@example.com')
    expect(impression.unread_messages).should.be.greater_than(0)
    # expect(impression.email).to.equal('somebody@example.com')

@httpretty.activate
def test_note():
    httpretty.register_uri(post, r(r"/v1/users/notes"), body=fixture('v1-users-note'))
    note = Note.create(body="This is a note", email='somebody@example.com')
    expect(note.html).to.equal("<p>This is a note</p>")
    expect(note.user.email).to.equal("somebody@example.com")

@nottest
@httpretty.activate
def test_endpoints():
    # FakeWeb.allow_net_connect = %r(127.0.0.7)
    httpretty.register_uri(get, r(r"/v1/users\?email="), body=fixture('v1-user'), match_querystring=True)
    Intercom.endpoints = ("http://127.0.0.7", "https://api.intercom.io")
    user = User.find(email='somebody@example.com')
    expect(user.name).to.equal('Somebody')

@nottest
@httpretty.activate
def test_unreachable():
    class ServiceUnavailableError(Exception):
        pass
    httpretty.register_uri(get, r(r"example\.com"), body=fixture('v1-user'), status=503)
    Intercom.endpoints = ("http://example.com")
    User.find.when.called_with(email='somebody@example.com').should.throw(ServiceUnavailableError)
    Intercom.endpoints = ("http://example.com", "http://api.example.com")
    User.find.when.called_with(email='not-found@example.com').should.throw(ServiceUnavailableError)

@nottest
@httpretty.activate
def test_bad_gateway():
    class BadGatewayError(Exception):
        pass
    httpretty.register_uri(get, r(r"example\.com"), body=fixture('v1-user'), status=502)
    Intercom.endpoints = ("http://example.com")
    User.find.when.called_with(email='somebody@example.com').should.throw(BadGatewayError)
    Intercom.endpoints = ("http://example.com", "http://api.example.com")
    User.find.when.called_with(email='not-found@example.com').should.throw(BadGatewayError)
