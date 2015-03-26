# -*- coding: utf-8 -*-

import unittest

from datetime import datetime
from intercom.traits.api_resource import Resource
from nose.tools import assert_raises
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import istest


class IntercomTraitsApiResource(unittest.TestCase):

    def setUp(self):  # noqa
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

    @istest
    def it_does_not_set_type_on_parsing_json(self):
        ok_(not hasattr(self.api_resource, 'type'))

    @istest
    def it_coerces_time_on_parsing_json(self):
        eq_(datetime.fromtimestamp(1374056196), self.api_resource.created_at)

    @istest
    def it_dynamically_defines_accessors_for_non_existent_properties(self):
        ok_(not hasattr(self.api_resource, 'spiders'))
        self.api_resource.spiders = 4
        ok_(hasattr(self.api_resource, 'spiders'))

    @istest
    def it_calls_dynamically_defined_getter_when_asked(self):
        self.api_resource.foo = 4
        eq_(4, self.api_resource.foo)

    @istest
    def it_accepts_unix_timestamps_into_dynamically_defined_date_setters(self):
        self.api_resource.foo_at = 1401200468
        eq_(1401200468, self.api_resource_obj.__getattribute__('foo_at'))

    @istest
    def it_exposes_dates_correctly_for_dynamically_defined_getters(self):
        self.api_resource.foo_at = 1401200468
        eq_(datetime.fromtimestamp(1401200468), self.api_resource.foo_at)

    # @istest
    # def it_throws_regular_error_when_non_existant_getter_is_called_that_is_backed_by_an_instance_variable(self):  # noqa
    #     super(Resource, self.api_resource).__setattr__('bar', 'you cant see me')  # noqa
    #     print (self.api_resource.bar)

    @istest
    def it_throws_attribute_error_when_non_existent_attribute_is_called(self):
        with assert_raises(AttributeError):
            self.api_resource.flubber

    @istest
    def it_throws_attribute_error_when_non_existent_method_is_called(self):
        with assert_raises(AttributeError):
            self.api_resource.flubber()

    @istest
    def it_throws_attribute_error_when_non_existent_setter_is_called(self):
        with assert_raises(AttributeError):
            self.api_resource.flubber('a', 'b')

    @istest
    def it_create_an_initialized_resource_equal_to_a_from_response_resource(self):  # noqa
        initialized_api_resource = Resource(**self.object_json)
        for key in list(self.object_json.keys()):
            if key == "type":
                continue
            eq_(getattr(initialized_api_resource, key), getattr(self.api_resource, key))  # noqa
