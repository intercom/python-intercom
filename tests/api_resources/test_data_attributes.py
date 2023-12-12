# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import DataAttribute, DataAttributeList
from intercom._client import Intercom, AsyncIntercom

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestDataAttributes:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        data_attribute = client.data_attributes.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        data_attribute = client.data_attributes.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
            description="My Data Attribute Description",
            options=["option1", "option2"],
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.data_attributes.with_raw_response.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = response.parse()
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        data_attribute = client.data_attributes.update(
            0,
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        data_attribute = client.data_attributes.update(
            0,
            archived=False,
            description="Just a plain old ring",
            options=["string", "string"],
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.data_attributes.with_raw_response.update(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = response.parse()
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        data_attribute = client.data_attributes.list()
        assert_matches_type(DataAttributeList, data_attribute, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        data_attribute = client.data_attributes.list(
            include_archived=True,
            model="contact",
        )
        assert_matches_type(DataAttributeList, data_attribute, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.data_attributes.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = response.parse()
        assert_matches_type(DataAttributeList, data_attribute, path=["response"])


class TestAsyncDataAttributes:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        data_attribute = await client.data_attributes.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        data_attribute = await client.data_attributes.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
            description="My Data Attribute Description",
            options=["option1", "option2"],
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.data_attributes.with_raw_response.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = response.parse()
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIntercom) -> None:
        data_attribute = await client.data_attributes.update(
            0,
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIntercom) -> None:
        data_attribute = await client.data_attributes.update(
            0,
            archived=False,
            description="Just a plain old ring",
            options=["string", "string"],
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncIntercom) -> None:
        response = await client.data_attributes.with_raw_response.update(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = response.parse()
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        data_attribute = await client.data_attributes.list()
        assert_matches_type(DataAttributeList, data_attribute, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIntercom) -> None:
        data_attribute = await client.data_attributes.list(
            include_archived=True,
            model="contact",
        )
        assert_matches_type(DataAttributeList, data_attribute, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.data_attributes.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = response.parse()
        assert_matches_type(DataAttributeList, data_attribute, path=["response"])
