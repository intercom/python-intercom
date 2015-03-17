import httpretty
import json
import re
from describe import expect
import intercom
from intercom.company import Company

get = httpretty.GET
r = re.compile


class DescribeIntercomCompany2:

    @httpretty.activate
    def it_raises_error_if_no_response_on_find(self):
        httpretty.register_uri(
            get, r(r'/companies$'), body=None, status=200)
        with expect.to_raise_error(intercom.HttpError):
            Company.find(company_id='4')

    @httpretty.activate
    def it_raises_error_if_no_response_on_find_all(self):
        httpretty.register_uri(
            get, r(r'/companies$'), body=None, status=200)
        with expect.to_raise_error(intercom.HttpError):
            [x for x in Company.all()]

    @httpretty.activate
    def it_raises_error_on_load(self):
        data = {
            'type': 'user',
            'id': 'aaaaaaaaaaaaaaaaaaaaaaaa',
            'company_id': '4',
            'name': 'MyCo'
        }
        httpretty.register_uri(
            get, r(r'/companies$'), body=json.dumps(data), status=200)
        company = Company.find(company_id='4')
        httpretty.register_uri(
            get, r(r'/companies/aaaaaaaaaaaaaaaaaaaaaaaa$'), body=None, status=200)  # noqa
        with expect.to_raise_error(intercom.HttpError):
            company.load()
