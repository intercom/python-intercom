# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types.shared import PaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        item = client.news.newsfeeds.items.list(
            "string",
        )
        assert_matches_type(PaginatedResponse, item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        item = client.news.newsfeeds.items.list(
            "string",
            intercom_version="2.11",
        )
        assert_matches_type(PaginatedResponse, item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.news.newsfeeds.items.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(PaginatedResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.news.newsfeeds.items.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(PaginatedResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.news.newsfeeds.items.with_raw_response.list(
                "",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        item = await async_client.news.newsfeeds.items.list(
            "string",
        )
        assert_matches_type(PaginatedResponse, item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        item = await async_client.news.newsfeeds.items.list(
            "string",
            intercom_version="2.11",
        )
        assert_matches_type(PaginatedResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.news.newsfeeds.items.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(PaginatedResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.news.newsfeeds.items.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(PaginatedResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.news.newsfeeds.items.with_raw_response.list(
                "",
            )
