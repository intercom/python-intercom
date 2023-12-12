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
    def test_method_create(self, client: Intercom) -> None:
        tag = client.contacts.tags.create(
            "string",
            id="string",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.contacts.tags.with_raw_response.create(
            "string",
            id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        tag = client.contacts.tags.list(
            "string",
        )
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.contacts.tags.with_raw_response.list(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagList, tag, path=["response"])


class TestAsyncTags:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        tag = await client.contacts.tags.create(
            "string",
            id="string",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.contacts.tags.with_raw_response.create(
            "string",
            id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        tag = await client.contacts.tags.list(
            "string",
        )
        assert_matches_type(TagList, tag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.contacts.tags.with_raw_response.list(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagList, tag, path=["response"])
