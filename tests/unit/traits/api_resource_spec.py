# -*- coding: utf-8 -*-

from datetime import datetime
from describe import expect
from intercom.traits.api_resource import Resource


class DescribeIntercomTraitsApiResource:

    def before_each(self, context):
        self.object_json = {
            "type": "company",
            "id": "aaaaaaaaaaaaaaaaaaaaaaaa",
            "app_id": "some-app-id",
            "name": "SuperSuite",
            "plan_id": 1,
            "remote_company_id": "8",
            "remote_created_at": 103201,
            "created_at": 1374056196,
            "user_count": 1,
            "custom_attributes": {}
        }
        self.api_resource = Resource().from_response(self.object_json)
        self.api_resource_obj = super(Resource, self.api_resource)

    def it_does_not_set_type_on_parsing_json(self):
        expect(self.api_resource).to_not.have_attr('type')

    def it_coerces_time_on_parsing_json(self):
        expect(datetime.fromtimestamp(1374056196)) == self.api_resource.created_at

    def it_dynamically_defines_accessors_for_non_existent_properties(self):
        expect(self.api_resource).to_not.have_attr('spiders')
        self.api_resource.spiders = 4
        expect(self.api_resource).to.have_attr('spiders')

    def it_calls_dynamically_defined_getter_when_asked(self):
        self.api_resource.foo = 4
        expect(4) == self.api_resource.foo

    def it_accepts_unix_timestamps_into_dynamically_defined_date_setters(self):
        self.api_resource.foo_at = 1401200468
        expect(1401200468) == self.api_resource_obj.__getattribute__('foo_at')

    def it_exposes_dates_correctly_for_dynamically_defined_getters(self):
        self.api_resource.foo_at = 1401200468
        expect(datetime.fromtimestamp(1401200468)) == self.api_resource.foo_at

    # def it_throws_regular_error_when_non_existant_getter_is_called_that_is_backed_by_an_instance_variable(self):
    #     super(Resource, self.api_resource).__setattr__('bar', 'you cant see me')
    #     print self.api_resource.bar

    def it_throws_attribute_error_when_non_existent_attribute_is_called(self):
        with expect.to_raise_error(AttributeError):
            self.api_resource.flubber

    def it_throws_attribute_error_when_non_existent_method_is_called(self):
        with expect.to_raise_error(AttributeError):
            self.api_resource.flubber()

    def it_throws_attribute_error_when_non_existent_setter_is_called(self):
        with expect.to_raise_error(AttributeError):
            self.api_resource.flubber('a', 'b')

    def it_create_an_initialized_resource_equal_to_a_from_response_resource(self):
        initialized_api_resource = Resource(**self.object_json)
        for key in self.object_json.keys():
            if key == "type":
                continue
            expect(getattr(initialized_api_resource, key)) == getattr(self.api_resource, key)
