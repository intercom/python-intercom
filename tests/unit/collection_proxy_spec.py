import httpretty
import json
import re
from describe import expect
from intercom.user import User
from tests.unit import page_of_users

get = httpretty.GET
r = re.compile


class DescribeIntercomCollectionProxy:

    @httpretty.activate
    def it_stops_iterating_if_no_next_link(self):
        body = json.dumps(page_of_users(include_next_link=False))
        httpretty.register_uri(get, r(r"/users"), body=body)
        emails = [user.email for user in User.all()]
        expect(emails) == ['user1@example.com', 'user2@example.com', 'user3@example.com']

    @httpretty.activate
    def it_keeps_iterating_if_next_link(self):
        page1 = json.dumps(page_of_users(include_next_link=True))
        page2 = json.dumps(page_of_users(include_next_link=False))
        httpretty.register_uri(get, r(r"/users$"), body=page1)
        httpretty.register_uri(
            get, r(r'https://api.intercom.io/users\?per_page=50&page=2'), body=page2,
            match_querystring=True)
        emails = [user.email for user in User.all()]
        expect(emails) == ['user1@example.com', 'user2@example.com', 'user3@example.com'] * 2

    @httpretty.activate
    def it_supports_indexed_array_access(self):
        body = json.dumps(page_of_users(include_next_link=False))
        httpretty.register_uri(get, r(r"/users"), body=body)
        expect(User.all()[0].email) == 'user1@example.com'

    @httpretty.activate
    def it_supports_querying(self):
        body = json.dumps(page_of_users(include_next_link=False))
        httpretty.register_uri(get, r(r"/users"), body=body)
        emails = [user.email for user in User.find_all(tag_name='Taggart J')]
        expect(emails) == ['user1@example.com', 'user2@example.com', 'user3@example.com']
