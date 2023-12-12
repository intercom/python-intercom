# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import Tag, TagList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestTags:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        tag = client.tags.retrieve(
            "string",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        tag = client.tags.list()
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        tag = client.tags.delete(
            "string",
        )
        assert tag is None

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @parametrize
    def test_method_create_or_update_overload_1(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_create_or_update_with_all_params_overload_1(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            name="Independent",
            id="656452352",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create_or_update_overload_1(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.create_or_update(
            name="Independent",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_create_or_update_overload_2(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create_or_update_overload_2(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_create_or_update_overload_3(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create_or_update_overload_3(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_create_or_update_overload_4(self, client: Intercom) -> None:
        tag = client.tags.create_or_update(
            name="Independent",
            users=[{}, {}, {}],
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create_or_update_overload_4(self, client: Intercom) -> None:
        response = client.tags.with_raw_response.create_or_update(
            name="Independent",
            users=[{}, {}, {}],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])


class TestAsyncTags:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        tag = await client.tags.retrieve(
            "string",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.tags.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        tag = await client.tags.list()
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.tags.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncIntercom) -> None:
        tag = await client.tags.delete(
            "string",
        )
        assert tag is None

    @parametrize
    async def test_raw_response_delete(self, client: AsyncIntercom) -> None:
        response = await client.tags.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @parametrize
    async def test_method_create_or_update_overload_1(self, client: AsyncIntercom) -> None:
        tag = await client.tags.create_or_update(
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_create_or_update_with_all_params_overload_1(self, client: AsyncIntercom) -> None:
        tag = await client.tags.create_or_update(
            name="Independent",
            id="656452352",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update_overload_1(self, client: AsyncIntercom) -> None:
        response = await client.tags.with_raw_response.create_or_update(
            name="Independent",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_create_or_update_overload_2(self, client: AsyncIntercom) -> None:
        tag = await client.tags.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update_overload_2(self, client: AsyncIntercom) -> None:
        response = await client.tags.with_raw_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_create_or_update_overload_3(self, client: AsyncIntercom) -> None:
        tag = await client.tags.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update_overload_3(self, client: AsyncIntercom) -> None:
        response = await client.tags.with_raw_response.create_or_update(
            companies=[{}, {}, {}],
            name="Independent",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_create_or_update_overload_4(self, client: AsyncIntercom) -> None:
        tag = await client.tags.create_or_update(
            name="Independent",
            users=[{}, {}, {}],
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update_overload_4(self, client: AsyncIntercom) -> None:
        response = await client.tags.with_raw_response.create_or_update(
            name="Independent",
            users=[{}, {}, {}],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])
