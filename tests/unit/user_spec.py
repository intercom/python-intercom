# -*- coding: utf-8 -*-

import httpretty
import json
import mock
import re
import time

from datetime import datetime
from describe import expect
from intercom.collection_proxy import CollectionProxy
from intercom.lib.flat_store import FlatStore
from intercom import User
from intercom.utils import create_class_instance
from tests.unit import test_user


get = httpretty.GET
post = httpretty.POST
delete = httpretty.DELETE

r = re.compile


class DescribeIntercomUser:

    def it_to_dict_itself(self):
        created_at = datetime.utcnow()
        user = User(
            email="jim@example.com", user_id="12345",
            created_at=created_at, name="Jim Bob")
        as_dict = user.to_dict
        expect(as_dict["email"]) == "jim@example.com"
        expect(as_dict["user_id"]) == "12345"
        expect(as_dict["created_at"]) == time.mktime(created_at.timetuple())
        expect(as_dict["name"]) == "Jim Bob"

    def it_presents_created_at_and_last_impression_at_as_datetime(self):
        now = datetime.utcnow()
        now_ts = time.mktime(now.timetuple())
        user = User.from_api(
            {'created_at': now_ts, 'last_impression_at': now_ts})
        expect(user.created_at).to.be_instance_of(datetime)
        expect(now.strftime('%c')) == user.created_at.strftime('%c')
        expect(user.last_impression_at).to.be_instance_of(datetime)
        expect(now.strftime('%c')) == user.last_impression_at.strftime('%c')

    def it_throws_an_attribute_error_on_trying_to_access_an_attribute_that_has_not_been_set(self):  # noqa
        with expect.to_raise_error(AttributeError):
            user = User()
            user.foo_property

    def it_presents_a_complete_user_record_correctly(self):
        user = User.from_api(test_user())
        expect('id-from-customers-app') == user.user_id
        expect('bob@example.com') == user.email
        expect('Joe Schmoe') == user.name
        expect('the-app-id') == user.app_id
        expect(123) == user.session_count
        expect(1401970114) == time.mktime(user.created_at.timetuple())
        expect(1393613864) == time.mktime(user.remote_created_at.timetuple())
        expect(1401970114) == time.mktime(user.updated_at.timetuple())

        Avatar = create_class_instance('Avatar')  # noqa
        Company = create_class_instance('Company')  # noqa
        SocialProfile = create_class_instance('SocialProfile')  # noqa
        LocationData = create_class_instance('LocationData')  # noqa
        expect(user.avatar).to.be_instance_of(Avatar.__class__)
        img_url = 'https://graph.facebook.com/1/picture?width=24&height=24'
        expect(img_url) == user.avatar.image_url

        expect(user.companies).to.be_instance_of(list)
        expect(1) == len(user.companies)
        expect(user.companies[0]).to.be_instance_of(Company.__class__)
        expect('123') == user.companies[0].company_id
        expect('bbbbbbbbbbbbbbbbbbbbbbbb') == user.companies[0].id
        expect('the-app-id') == user.companies[0].app_id
        expect('Company 1') == user.companies[0].name
        expect(1390936440) == time.mktime(
            user.companies[0].remote_created_at.timetuple())
        expect(1401970114) == time.mktime(
            user.companies[0].created_at.timetuple())
        expect(1401970114) == time.mktime(
            user.companies[0].updated_at.timetuple())
        expect(1401970113) == time.mktime(
            user.companies[0].last_request_at.timetuple())
        expect(0) == user.companies[0].monthly_spend
        expect(0) == user.companies[0].session_count
        expect(1) == user.companies[0].user_count
        expect([]) == user.companies[0].tag_ids

        expect(user.custom_attributes).to.be_instance_of(FlatStore)
        expect('b') == user.custom_attributes["a"]
        expect(2) == user.custom_attributes["b"]

        expect(4) == len(user.social_profiles)
        twitter_account = user.social_profiles[0]
        expect(twitter_account).to.be_instance_of(SocialProfile.__class__)
        expect('twitter') == twitter_account.name
        expect('abc') == twitter_account.username
        expect('http://twitter.com/abc') == twitter_account.url

        expect(user.location_data).to.be_instance_of(LocationData.__class__)
        expect('Dublin') == user.location_data.city_name
        expect('EU') == user.location_data.continent_code
        expect('Ireland') == user.location_data.country_name
        expect('90') == user.location_data.latitude
        expect('10') == user.location_data.longitude
        expect('IRL') == user.location_data.country_code

        expect(user.unsubscribed_from_emails)
        expect("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11") == user.user_agent_data  # noqa

    def it_allows_update_last_request_at(self):
        payload = {
            'user_id': '1224242',
            'update_last_request_at': True,
            'custom_attributes': {}
        }
        httpretty.register_uri(post, r("/users"), body=json.dumps(payload))
        User(user_id='1224242', update_last_request_at=True)

    def it_allows_easy_setting_of_custom_data(self):
        now = datetime.utcnow()
        now_ts = time.mktime(now.timetuple())

        user = User()
        user.custom_attributes["mad"] = 123
        user.custom_attributes["other"] = now_ts
        user.custom_attributes["thing"] = "yay"
        attrs = {"mad": 123, "other": now_ts, "thing": "yay"}
        expect(user.to_dict["custom_attributes"]) == attrs

    def it_allows_easy_setting_of_multiple_companies(self):
        user = User()
        companies = [
            {"name": "Intercom", "company_id": "6"},
            {"name": "Test", "company_id": "9"},
        ]
        user.companies = companies
        expect(user.to_dict["companies"]) == companies

    def it_rejects_nested_data_structures_in_custom_attributes(self):
        user = User()
        with expect.to_raise_error(ValueError):
            user.custom_attributes["thing"] = [1]

        with expect.to_raise_error(ValueError):
            user.custom_attributes["thing"] = {1: 2}

        with expect.to_raise_error(ValueError):
            user.custom_attributes = {1: {2: 3}}

        user = User.from_api(test_user())
        with expect.to_raise_error(ValueError):
            user.custom_attributes["thing"] = [1]

    @httpretty.activate
    def it_fetches_a_user(self):
        body = json.dumps(test_user())

        httpretty.register_uri(
            get, r(r"https://api.intercom.io/users\?email="),
            body=body, match_querystring=True)
        user = User.find(email='somebody@example.com')
        expect(user.email) == 'bob@example.com'
        expect(user.name) == 'Joe Schmoe'

    @httpretty.activate
    def it_saves_a_user_always_sends_custom_attributes(self):
        user = User(email="jo@example.com", user_id="i-1224242")

        body = json.dumps({
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'custom_attributes': {}
        })
        httpretty.register_uri(
            post, r(r"/users"), body=body)
        user.save()
        expect(user.email) == 'jo@example.com'
        expect(user.custom_attributes) == {}

    @httpretty.activate
    def it_saves_a_user_with_a_company(self):
        user = User(
            email="jo@example.com", user_id="i-1224242",
            company={'company_id': 6, 'name': 'Intercom'})

        body = json.dumps({
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        })
        httpretty.register_uri(
            post, r(r"/users"), body=body)
        user.save()
        expect(user.email) == 'jo@example.com'
        expect(len(user.companies)) == 1

    @httpretty.activate
    def it_saves_a_user_with_companies(self):
        user = User(
            email="jo@example.com", user_id="i-1224242",
            companies=[{'company_id': 6, 'name': 'Intercom'}])
        body = json.dumps({
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        })
        httpretty.register_uri(
            post, r(r"/users"), body=body)
        user.save()
        expect(user.email) == 'jo@example.com'
        expect(len(user.companies)) == 1

    @httpretty.activate
    def it_can_save_a_user_with_a_none_email(self):
        user = User(
            email=None, user_id="i-1224242",
            companies=[{'company_id': 6, 'name': 'Intercom'}])
        body = json.dumps({
            'custom_attributes': {},
            'email': None,
            'user_id': 'i-1224242',
            'companies': [{
                'company_id': 6,
                'name': 'Intercom'
            }]
        })
        httpretty.register_uri(
            post, r(r"/users"), body=body)
        user.save()
        expect(user.email) is None
        expect(user.user_id) is 'i-1224242'

    @httpretty.activate
    def it_deletes_a_user(self):
        user = User(id="1")
        httpretty.register_uri(
            delete, r(r"https://api.intercom.io/users/1"), body='{}')
        user = user.delete()
        expect(user.id) == "1"

    @httpretty.activate
    def it_can_use_user_create_for_convenience(self):
        payload = {
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'custom_attributes': {}
        }
        httpretty.register_uri(post, r(r"/users"), body=json.dumps(payload))
        user = User.create(email="jo@example.com", user_id="i-1224242")
        expect(payload) == user.to_dict

    @httpretty.activate
    def it_updates_the_user_with_attributes_set_by_the_server(self):
        payload = {
            'email': 'jo@example.com',
            'user_id': 'i-1224242',
            'custom_attributes': {},
            'session_count': 4
        }
        httpretty.register_uri(post, r(r"/users"), body=json.dumps(payload))

        user = User.create(email="jo@example.com", user_id="i-1224242")
        expect(payload) == user.to_dict

    @httpretty.activate
    def it_allows_setting_dates_to_none_without_converting_them_to_0(self):
        payload = {
            'email': 'jo@example.com',
            'custom_attributes': {},
            'remote_created_at': None
        }
        httpretty.register_uri(post, r("/users"), body=json.dumps(payload))
        user = User.create(email="jo@example.com", remote_created_at=None)
        expect(user.remote_created_at) is None

    @httpretty.activate
    def it_gets_sets_rw_keys(self):
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
        expect(sorted(expected_keys)) == sorted(user.to_dict.keys())
        for key in payload.keys():
            expect(payload[key]) == user.to_dict[key]

    @httpretty.activate
    def it_will_allow_extra_attributes_in_response_from_api(self):
        user = User.from_api({'new_param': 'some value'})
        expect('some value') == user.new_param

    def it_returns_a_collectionproxy_for_all_without_making_any_requests(self):
        with mock.patch('intercom.Request.send_request_to_path', new_callable=mock.NonCallableMock):  # noqa
            res = User.all()
            expect(res).to.be_instance_of(CollectionProxy)

    def it_returns_the_total_number_of_users(self):
        with mock.patch.object(User, 'count') as mock_count:
            mock_count.return_value = 100
            expect(100) == User.count()

    class DescribeIncrementingCustomAttributeFields:

        def before_each(self, context):
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
            self.user = User(**params)

        def it_increments_up_by_1_with_no_args(self):
            self.user.increment('mad')
            expect(self.user.to_dict['custom_attributes']['mad']) == 124

        def it_increments_up_by_given_value(self):
            self.user.increment('mad', 4)
            expect(self.user.to_dict['custom_attributes']['mad']) == 127

        def it_increments_down_by_given_value(self):
            self.user.increment('mad', -1)
            expect(self.user.to_dict['custom_attributes']['mad']) == 122

        def it_can_increment_new_custom_data_fields(self):
            self.user.increment('new_field', 3)
            expect(self.user.to_dict['custom_attributes']['new_field']) == 3

        def it_can_call_increment_on_the_same_key_twice_and_increment_by_2(self):  # noqa
            self.user.increment('mad')
            self.user.increment('mad')
            expect(self.user.to_dict['custom_attributes']['mad']) == 125
