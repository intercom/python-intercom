# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.news import Newsfeed
from intercom.types.shared import PaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestNewsfeeds:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        newsfeed = client.news.newsfeeds.retrieve(
            "string",
        )
        assert_matches_type(Newsfeed, newsfeed, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.news.newsfeeds.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        newsfeed = response.parse()
        assert_matches_type(Newsfeed, newsfeed, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        newsfeed = client.news.newsfeeds.list()
        assert_matches_type(PaginatedResponse, newsfeed, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.news.newsfeeds.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        newsfeed = response.parse()
        assert_matches_type(PaginatedResponse, newsfeed, path=["response"])


class TestAsyncNewsfeeds:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        newsfeed = await client.news.newsfeeds.retrieve(
            "string",
        )
        assert_matches_type(Newsfeed, newsfeed, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.news.newsfeeds.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        newsfeed = response.parse()
        assert_matches_type(Newsfeed, newsfeed, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        newsfeed = await client.news.newsfeeds.list()
        assert_matches_type(PaginatedResponse, newsfeed, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.news.newsfeeds.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        newsfeed = response.parse()
        assert_matches_type(PaginatedResponse, newsfeed, path=["response"])
