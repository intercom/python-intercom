# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

import httpretty
import json
import mock
import re
import time

from datetime import datetime
from intercom.user import CollectionProxy
from intercom.user import User
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import raises

get = httpretty.GET
post = httpretty.POST
delete = httpretty.DELETE

r = re.compile


def test_to_dict():
    created_at = datetime.utcnow()
    user = User(email="jim@example.com", user_id="12345", created_at=created_at, name="Jim Bob")
    as_dict = user.to_dict
    eq_(as_dict["email"], "jim@example.com")
    eq_(as_dict["user_id"], "12345")
    eq_(as_dict["created_at"], time.mktime(created_at.timetuple()))
    eq_(as_dict["name"], "Jim Bob")


def test_dates():
    now = datetime.utcnow()
    now_ts = time.mktime(now.timetuple())
    user = User.from_api({'created_at': now_ts, 'last_impression_at': now_ts})
    ok_(isinstance(user.created_at, datetime))
    eq_(now.strftime('%c'), user.created_at.strftime('%c'))
    ok_(isinstance(user.last_impression_at, datetime))
    eq_(now.strftime('%c'), user.last_impression_at.strftime('%c'))


@raises(AttributeError)
def test_attribute_not_set():
    user = User()
    user.foo_property


def test_complete_user():
    from . import test_user_obj
    user = User.from_api(test_user_obj)
    eq_('id-from-customers-app', user.user_id)
    eq_('bob@example.com', user.email)
    eq_('Joe Schmoe', user.name)
    eq_('the-app-id', user.app_id)
    eq_(123, user.session_count)
    eq_(1401970114, time.mktime(user.created_at.timetuple()))
    eq_(1393613864, time.mktime(user.remote_created_at.timetuple()))
    eq_(1401970114, time.mktime(user.updated_at.timetuple()))

    eq_('Avatar', user.avatar.__class__.__name__)
    eq_('https://graph.facebook.com/1/picture?width=24&height=24', user.avatar.image_url)

    eq_('list', user.companies.__class__.__name__)
    eq_(1, len(user.companies))
    eq_('Company', user.companies[0].__class__.__name__)
    eq_('123', user.companies[0].company_id)
    eq_('bbbbbbbbbbbbbbbbbbbbbbbb', user.companies[0].id)
    eq_('the-app-id', user.companies[0].app_id)
    eq_('Company 1', user.companies[0].name)
    eq_(1390936440, time.mktime(user.companies[0].remote_created_at.timetuple()))
    eq_(1401970114, time.mktime(user.companies[0].created_at.timetuple()))
    eq_(1401970114, time.mktime(user.companies[0].updated_at.timetuple()))
    eq_(1401970113, time.mktime(user.companies[0].last_request_at.timetuple()))
    eq_(0, user.companies[0].monthly_spend)
    eq_(0, user.companies[0].session_count)
    eq_(1, user.companies[0].user_count)
    eq_([], user.companies[0].tag_ids)

    eq_('FlatStore', user.custom_attributes.__class__.__name__)
    eq_('b', user.custom_attributes["a"])
    eq_(2, user.custom_attributes["b"])

    eq_(4, len(user.social_profiles))
    twitter_account = user.social_profiles[0]
    eq_('SocialProfile', twitter_account.__class__.__name__)
    eq_('twitter', twitter_account.name)
    eq_('abc', twitter_account.username)
    eq_('http://twitter.com/abc', twitter_account.url)

    eq_('LocationData', user.location_data.__class__.__name__)
    eq_('Dublin', user.location_data.city_name)
    eq_('EU', user.location_data.continent_code)
    eq_('Ireland', user.location_data.country_name)
    eq_('90', user.location_data.latitude)
    eq_('10', user.location_data.longitude)
    eq_('IRL', user.location_data.country_code)

    ok_(user.unsubscribed_from_emails)
    eq_("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", user.user_agent_data)


def test_custom_data():
    now = datetime.utcnow()
    now_ts = time.mktime(now.timetuple())

    user = User()
    user.custom_attributes["mad"] = 123
    user.custom_attributes["other"] = now_ts
    user.custom_attributes["thing"] = "yay"
    eq_(user.to_dict["custom_attributes"], {"mad": 123, "other": now_ts, "thing": "yay"})


def test_multiple_companies():
    user = User()
    companies = [
        {"name": "Intercom", "company_id": "6"},
        {"name": "Test", "company_id": "9"},
    ]
    user.companies = companies
    eq_(user.to_dict["companies"], companies)


def test_nested_custom_attributes():
    user = User()
    try:
        user.custom_attributes["thing"] = [1]
        assert False, "list not allowed as custom attribute"
    except ValueError:
        pass

    try:
        user.custom_attributes["thing"] = { 1: 2 }
        assert False, "dict not allowed as custom attribute"
    except ValueError:
        pass

    try:
        user.custom_attributes = { 1: { 2: 3}}
        print "ABC", user.custom_attributes
        assert False, "nested dict not allowed as custom attribute"
    except ValueError:
        pass

    from . import test_user_obj
    user = User.from_api(test_user_obj)
    try:
        user.custom_attributes["thing"] = [1]
        assert False, "list not allowed as custom attribute"
    except ValueError:
        pass


@httpretty.activate
def test_fetch_user():
    from . import test_user_obj
    body = json.dumps(test_user_obj)

    httpretty.register_uri(
        get, r(r"https://api.intercom.io/users\?email="),
        body=body, match_querystring=True)
    user = User.find(email='somebody@example.com')
    eq_(user.email, 'bob@example.com')
    eq_(user.name, 'Joe Schmoe')


@httpretty.activate
def test_save_user_attributes():
    user = User(email="jo@example.com", user_id="i-1224242")
 
    body = json.dumps({
        'email': 'jo@example.com',
        'user_id': 'i-1224242',
        'custom_attributes': {}
    })
    httpretty.register_uri(
        post, r(r"/users"), body=body)
    user.save()
    eq_(user.email, 'jo@example.com')
    eq_(user.custom_attributes, {})


@httpretty.activate
def test_save_user_with_companies():
    user = User(
        email="jo@example.com", user_id="i-1224242",
        companies=[{'company_id': 6, 'name': 'Intercom'},{'company_id': 8, 'name': 'Intercom2'}])
 
    body = json.dumps({
        'email': 'jo@example.com',
        'user_id': 'i-1224242',
        'companies': [{
            'company_id': 6,
            'name': 'Intercom2'
        }]
    })
    httpretty.register_uri(
        post, r(r"/users"), body=body)
    user.save()
    eq_(user.email, 'jo@example.com')
    eq_(len(user.companies), 1)
    # eq_('Company', user.companies[0].__class__.__name__)


@httpretty.activate
def test_delete_user():
    user = User(id="1")
    httpretty.register_uri(
        delete, r(r"https://api.intercom.io/users/1"), body='{}')
    user = user.delete()
    eq_(user.id, "1")

@httpretty.activate
def test_create_user():
    payload = {
        'email': 'jo@example.com',
        'user_id': 'i-1224242',
        'custom_attributes': {}
    }
    httpretty.register_uri(post, r(r"/users"), body=json.dumps(payload))
    user = User.create(email="jo@example.com", user_id="i-1224242")
    eq_(payload, user.to_dict)


@httpretty.activate
def test_create_user_server_attributes():
    payload = {
        'email': 'jo@example.com',
        'user_id': 'i-1224242',
        'custom_attributes': {},
        'session_count': 4
    }
    httpretty.register_uri(post, r(r"/users"), body=json.dumps(payload))

    user = User.create(email="jo@example.com", user_id="i-1224242")
    eq_(payload, user.to_dict)


@httpretty.activate
def test_null_dates():
    payload = {
        'email': 'jo@example.com',
        'custom_attributes': {},
        'remote_created_at': None
    }
    httpretty.register_uri(post, r("/users"), body=json.dumps(payload))
    user = User.create(email="jo@example.com", remote_created_at=None)
    eq_(user.remote_created_at, None)


@httpretty.activate
def test_getset_rw_keys():
    created_at = datetime.utcnow()
    payload = {
        'email': 'me@example.com',
        'user_id': 'abc123',
        'name': 'Bob Smith',
        'last_seen_ip': '1.2.3.4',
        'last_seen_user_agent': 'ie6',
        'created_at': time.mktime(created_at.timetuple())
    }
    httpretty.register_uri(post, r("/users"), body=json.dumps(payload))
    user = User(**payload)
    expected_keys = ['custom_attributes']
    expected_keys.extend(payload.keys())
    eq_(sorted(expected_keys), sorted(user.to_dict.keys()))
    for key in payload.keys():
        eq_(payload[key], user.to_dict[key])


@httpretty.activate
def test_extra_response_attributes():
    user = User.from_api({'new_param': 'some value'})
    eq_('some value', user.new_param)


def test_all_collectionproxy():
    with mock.patch('intercom.Intercom.send_request_to_path', new_callable=mock.NonCallableMock):
        res = User.all()
        ok_(type(res), CollectionProxy)


def test_count():

    with mock.patch.object(User, 'count') as mock_count:
        mock_count.return_value = 100
        eq_(100, User.count())


def test_incremental_attributes():
    created_at = datetime.utcnow()
    params = {
        'email': 'jo@example.com',
        'user_id': 'i-1224242',
        'custom_attributes': {
            'mad': 123,
            'another': 432,
            'other': time.mktime(created_at.timetuple()),
            'thing': 'yay'
        }
    }
    user = User(**params)
    user.increment('mad')
    eq_(user.to_dict['custom_attributes']['mad'], 124)

    user = User(**params)
    user.increment('mad', 4)
    eq_(user.to_dict['custom_attributes']['mad'], 127)

    user = User(**params)
    user.increment('mad', -1)
    eq_(user.to_dict['custom_attributes']['mad'], 122)

    user = User(**params)
    user.increment('new_field', 3)
    eq_(user.to_dict['custom_attributes']['new_field'], 3)

    user = User(**params)
    user.increment('mad')
    user.increment('mad')
    eq_(user.to_dict['custom_attributes']['mad'], 125)

