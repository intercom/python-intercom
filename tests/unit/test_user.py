# coding=utf-8
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

from datetime import datetime
from intercom.user import CustomData
from intercom.user import LocationData
from intercom.user import SocialProfile
from intercom.user import User
from intercom.user import Company
from nose.tools import eq_
from nose.tools import raises


def test_init_no_arg():
    # no arg __init__
    custom_data = CustomData()
    eq_(0, len(custom_data))


def test_init_dict_arg():
    # dict arg __init__
    custom_data = CustomData({'color': 'red'})
    eq_(1, len(custom_data))


def test_string_key():
    # string keys are allowed
    custom_data = CustomData()
    custom_data['a'] = 'b'


@raises(ValueError)
def test_numeric_key():
    # numeric keys are not allowed
    custom_data = CustomData()
    custom_data[1] = 'a'


@raises(ValueError)
def test_dict_key():
    # dict keys are not allowed
    custom_data = CustomData()
    custom_data[{'a': 'b'}] = 'c'


def test_numeric_values():
    # numeric values are allowed
    custom_data = CustomData()
    custom_data['a'] = 1
    custom_data['b'] = 3.14
    custom_data['c'] = 0177
    custom_data['d'] = 0x7F


@raises(ValueError)
def test_complex_number_values():
    # complex numeber values are allowed
    custom_data = CustomData()
    custom_data['a'] = complex(1.0, 0.2)


@raises(ValueError)
def test_dict_value():
    # dict values are not allowed
    custom_data = CustomData()
    custom_data['a'] = {'b': 'c'}


@raises(ValueError)
def test_list_value():
    # list values are not allowed
    custom_data = CustomData()
    custom_data['a'] = ['b', 'c']


def test_attr():
    sc_dict = {
        'type': 'twitter',
        'url': 'http://twitter.com/myname',
        'username': 'myname',
        'id': '123456789'
    }

    social_profile = SocialProfile(sc_dict)
    eq_('twitter', social_profile.type)
    eq_('http://twitter.com/myname', social_profile.url)
    eq_('myname', social_profile.username)
    eq_('123456789', social_profile.id)


@raises(NotImplementedError)
def test_setitem():
    social_profile = SocialProfile()
    social_profile['type'] = 'facebook'


def test_user_properties():

    created_at = datetime.fromtimestamp(1331764344)
    last_request_at = datetime.fromtimestamp(1331764345)
    last_impression_at = datetime.fromtimestamp(1331764346)
    user = User()
    user.email = 'somebody@example.com'
    user.user_id = 1234
    user.name = 'Somebody'
    user.last_seen_ip = '192.168.1.100'
    user.last_seen_user_agent = 'Mozilla/5.0'
    user.last_request_at = last_request_at
    user.last_impression_at = last_impression_at
    user.created_at = created_at
    user.unsubscribed_from_emails = True
    user.custom_data = {'name': 'Ace'}
    user.companies = [{
        'id': 1,
        'name': 'Intercom',
        'created_at': created_at}]
    try:
        # cannot set the relationship score
        user.relationship_score = 50
        raise AttributeError
    except AttributeError:
        pass

    eq_(user.email, 'somebody@example.com')
    eq_(user.user_id, 1234)
    eq_(user.name, 'Somebody')
    eq_(user.last_seen_ip, '192.168.1.100')
    eq_(user.last_seen_user_agent, 'Mozilla/5.0')
    eq_(user.last_request_at, last_request_at)
    eq_(user.last_impression_at, last_impression_at)
    eq_(user.relationship_score, None)
    eq_(user.created_at, created_at)
    eq_(user.unsubscribed_from_emails, True)
    eq_(user.custom_data['name'], 'Ace')
    eq_(user.session_count, 0)
    raises(AttributeError, lambda: user.companies)


def test_company_properties():
    c_dict = {
        'id': 1,
        'name': 'Intercom',
        'created_at': 1331764344
    }
    company = Company(c_dict)
    eq_(company.id, 1)
    eq_(company.name, 'Intercom')
    eq_(company.created_at, datetime.fromtimestamp(1331764344))

    company.id = 100
    company.name = 'ACME Inc.'
    company.created_at = datetime.fromtimestamp(1331764300)
    eq_(company.id, 100)
    eq_(company.name, 'ACME Inc.')
    eq_(company.created_at, datetime.fromtimestamp(1331764300))


@raises(ValueError)
def test_user_company():
    user = User()
    # use a Company object
    user.company = Company({
        'id': 1,
        'name': 'Intercom',
        'created_at': datetime.fromtimestamp(1331764344)
    })

    # use a dict object
    user.company = {
        'id': 1,
        'name': 'Intercom',
        'created_at': datetime.fromtimestamp(1331764344)
    }
    raises(AttributeError, lambda: user.company)
    user.company = ['foo']


@raises(ValueError)
def test_user_companies():
    user = User()
    user.companies = [{
        'id': 1,
        'name': 'Intercom',
        'created_at': datetime.fromtimestamp(1331764344)}]
    raises(AttributeError, lambda: user.companies)
    user.companies = {'foo': 'bar'}


@raises(AttributeError)
def test_location_setattr():
    location_data = LocationData()
    location_data.city_name = "Dublin"


@raises(NotImplementedError)
def test_location_setitem():
    location_data = LocationData()
    location_data['city_name'] = "Dublin"


def test_location_properties():
    location_data = LocationData({
        "city_name": "Santiago",
        "continent_code": "SA",
        "country_name": "Chile",
        "latitude": -33.44999999999999,
        "longitude": -70.6667,
        "postal_code": "",
        "region_name": "12",
        "timezone": "Chile/Continental",
        "country_code": "CHL"
    })

    eq_(location_data.city_name, 'Santiago')
    eq_(location_data.continent_code, 'SA')
    eq_(location_data.country_name, 'Chile')
    eq_(location_data.latitude, -33.44999999999999)
    eq_(location_data.longitude, -70.6667)
    eq_(location_data.postal_code, '')
    eq_(location_data.region_name, '12')
    eq_(location_data.timezone, 'Chile/Continental')
    eq_(location_data.country_code, 'CHL')
