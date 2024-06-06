# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import (
    DataAttribute,
    DataAttributeList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataAttributes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            messenger_writable=False,
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = response.parse()
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.data_attributes.with_streaming_response.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_attribute = response.parse()
            assert_matches_type(DataAttribute, data_attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            messenger_writable=False,
            options=["string", "string"],
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.data_attributes.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = response.parse()
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Intercom) -> None:
        with client.data_attributes.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_attribute = response.parse()
            assert_matches_type(DataAttribute, data_attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = response.parse()
        assert_matches_type(DataAttributeList, data_attribute, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.data_attributes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_attribute = response.parse()
            assert_matches_type(DataAttributeList, data_attribute, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataAttributes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        data_attribute = await async_client.data_attributes.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        data_attribute = await async_client.data_attributes.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
            description="My Data Attribute Description",
            messenger_writable=False,
            options=["option1", "option2"],
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.data_attributes.with_raw_response.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = await response.parse()
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.data_attributes.with_streaming_response.create(
            data_type="string",
            model="company",
            name="Mithril Shirt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_attribute = await response.parse()
            assert_matches_type(DataAttribute, data_attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncIntercom) -> None:
        data_attribute = await async_client.data_attributes.update(
            0,
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIntercom) -> None:
        data_attribute = await async_client.data_attributes.update(
            0,
            archived=False,
            description="Just a plain old ring",
            messenger_writable=False,
            options=["string", "string"],
        )
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIntercom) -> None:
        response = await async_client.data_attributes.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = await response.parse()
        assert_matches_type(DataAttribute, data_attribute, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIntercom) -> None:
        async with async_client.data_attributes.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_attribute = await response.parse()
            assert_matches_type(DataAttribute, data_attribute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        data_attribute = await async_client.data_attributes.list()
        assert_matches_type(DataAttributeList, data_attribute, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        data_attribute = await async_client.data_attributes.list(
            include_archived=True,
            model="contact",
        )
        assert_matches_type(DataAttributeList, data_attribute, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.data_attributes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_attribute = await response.parse()
        assert_matches_type(DataAttributeList, data_attribute, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.data_attributes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_attribute = await response.parse()
            assert_matches_type(DataAttributeList, data_attribute, path=["response"])

        assert cast(Any, response.is_closed) is True
