# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types.news import Newsfeed
from intercom.types.shared import PaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNewsfeeds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        newsfeed = response.parse()
        assert_matches_type(Newsfeed, newsfeed, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.news.newsfeeds.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            newsfeed = response.parse()
            assert_matches_type(Newsfeed, newsfeed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.news.newsfeeds.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        newsfeed = client.news.newsfeeds.list()
        assert_matches_type(PaginatedResponse, newsfeed, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.news.newsfeeds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        newsfeed = response.parse()
        assert_matches_type(PaginatedResponse, newsfeed, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.news.newsfeeds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            newsfeed = response.parse()
            assert_matches_type(PaginatedResponse, newsfeed, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNewsfeeds:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        newsfeed = await async_client.news.newsfeeds.retrieve(
            "string",
        )
        assert_matches_type(Newsfeed, newsfeed, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.news.newsfeeds.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        newsfeed = await response.parse()
        assert_matches_type(Newsfeed, newsfeed, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.news.newsfeeds.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            newsfeed = await response.parse()
            assert_matches_type(Newsfeed, newsfeed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.news.newsfeeds.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        newsfeed = await async_client.news.newsfeeds.list()
        assert_matches_type(PaginatedResponse, newsfeed, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.news.newsfeeds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        newsfeed = await response.parse()
        assert_matches_type(PaginatedResponse, newsfeed, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.news.newsfeeds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            newsfeed = await response.parse()
            assert_matches_type(PaginatedResponse, newsfeed, path=["response"])

        assert cast(Any, response.is_closed) is True
