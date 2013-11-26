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
from nose.tools import raises
from sure import expect


def test_init_no_arg():
    # no arg __init__
    custom_data = CustomData()
    expect(len(custom_data)).to.equal(0)


def test_init_dict_arg():
    # dict arg __init__
    custom_data = CustomData({'color': 'red'})
    expect(len(custom_data)).to.equal(1)


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
    expect(social_profile.type).to.equal('twitter')
    expect(social_profile.url).to.equal('http://twitter.com/myname')
    expect(social_profile.username).to.equal('myname')
    expect(social_profile.id).to.equal('123456789')


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

    expect(user.email).to.equal('somebody@example.com')
    expect(user.user_id).to.equal(1234)
    expect(user.name).to.equal('Somebody')
    expect(user.last_seen_ip).to.equal('192.168.1.100')
    expect(user.last_seen_user_agent).to.equal('Mozilla/5.0')
    expect(user.last_request_at).to.equal(last_request_at)
    expect(user.last_impression_at).to.equal(last_impression_at)
    expect(user.relationship_score).to.equal(None)
    expect(user.created_at).to.equal(created_at)
    expect(user.unsubscribed_from_emails).to.equal(True)
    expect(user.custom_data['name']).to.equal('Ace')
    expect(user.session_count).to.equal(0)
    raises(AttributeError, lambda: user.companies)


def test_company_properties():
    c_dict = {
        'id': 1,
        'name': 'Intercom',
        'created_at': 1331764344
    }
    company = Company(c_dict)
    expect(company.id).to.equal(1)
    expect(company.name).to.equal('Intercom')
    expect(company.created_at).to.equal(datetime.fromtimestamp(1331764344))

    company.id = 100
    company.name = 'ACME Inc.'
    company.created_at = datetime.fromtimestamp(1331764300)
    expect(company.id).to.equal(100)
    expect(company.name).to.equal('ACME Inc.')
    expect(company.created_at).to.equal(datetime.fromtimestamp(1331764300))


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

    expect(location_data.city_name).to.equal('Santiago')
    expect(location_data.continent_code).to.equal('SA')
    expect(location_data.country_name).to.equal('Chile')
    expect(location_data.latitude).to.equal(-33.44999999999999)
    expect(location_data.longitude).to.equal(-70.6667)
    expect(location_data.postal_code).to.equal('')
    expect(location_data.region_name).to.equal('12')
    expect(location_data.timezone).to.equal('Chile/Continental')
    expect(location_data.country_code).to.equal('CHL')
