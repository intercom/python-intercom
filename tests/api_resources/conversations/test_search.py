# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.conversations import ConversationList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestSearch:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        search = client.conversations.search.create(
            query={},
        )
        assert_matches_type(ConversationList, search, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        search = client.conversations.search.create(
            query={
                "field": "custom_attributes.social_network",
                "operator": "=",
                "value": "string",
            },
            pagination={
                "page": 2,
                "starting_after": "1HaSB+xrOyyMXAkS/c1RteCL7BzOzTvYjmjakgTergIH31eoe2v4/sbLsJWP\nIncfQLD3ouPkZlCwJ86F\n",
            },
        )
        assert_matches_type(ConversationList, search, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.conversations.search.with_raw_response.create(
            query={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(ConversationList, search, path=["response"])


class TestAsyncSearch:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        search = await client.conversations.search.create(
            query={},
        )
        assert_matches_type(ConversationList, search, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        search = await client.conversations.search.create(
            query={
                "field": "custom_attributes.social_network",
                "operator": "=",
                "value": "string",
            },
            pagination={
                "page": 2,
                "starting_after": "1HaSB+xrOyyMXAkS/c1RteCL7BzOzTvYjmjakgTergIH31eoe2v4/sbLsJWP\nIncfQLD3ouPkZlCwJ86F\n",
            },
        )
        assert_matches_type(ConversationList, search, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.conversations.search.with_raw_response.create(
            query={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(ConversationList, search, path=["response"])
