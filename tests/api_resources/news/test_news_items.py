# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types.news import (
    NewsItem,
    NewsItemListResponse,
    NewsItemDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNewsItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        news_item = client.news.news_items.create(
            sender_id=991268690,
            title="Halloween is here!",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        news_item = client.news.news_items.create(
            sender_id=991268690,
            title="Halloween is here!",
            body="<p>New costumes in store for this spooky season</p>",
            deliver_silently=True,
            labels=["Product", "Update", "New"],
            newsfeed_assignments=[
                {
                    "newsfeed_id": 103,
                    "published_at": 1664638214,
                }
            ],
            reactions=["😆", "😅"],
            state="live",
            intercom_version="2.11",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.news.news_items.with_raw_response.create(
            sender_id=991268690,
            title="Halloween is here!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.news.news_items.with_streaming_response.create(
            sender_id=991268690,
            title="Halloween is here!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_item = response.parse()
            assert_matches_type(NewsItem, news_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        news_item = client.news.news_items.retrieve(
            id=123,
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        news_item = client.news.news_items.retrieve(
            id=123,
            intercom_version="2.11",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.news.news_items.with_raw_response.retrieve(
            id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.news.news_items.with_streaming_response.retrieve(
            id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_item = response.parse()
            assert_matches_type(NewsItem, news_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        news_item = client.news.news_items.update(
            id=123,
            sender_id=991268701,
            title="Christmas is here!",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        news_item = client.news.news_items.update(
            id=123,
            sender_id=991268701,
            title="Christmas is here!",
            body="<p>New gifts in store for the jolly season</p>",
            deliver_silently=True,
            labels=["Product", "Update", "New"],
            newsfeed_assignments=[
                {
                    "newsfeed_id": 198313,
                    "published_at": 1674917488,
                },
                {
                    "newsfeed_id": 198313,
                    "published_at": 1674917488,
                },
                {
                    "newsfeed_id": 198313,
                    "published_at": 1674917488,
                },
            ],
            reactions=["😝", "😂"],
            state="live",
            intercom_version="2.11",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.news.news_items.with_raw_response.update(
            id=123,
            sender_id=991268701,
            title="Christmas is here!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Intercom) -> None:
        with client.news.news_items.with_streaming_response.update(
            id=123,
            sender_id=991268701,
            title="Christmas is here!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_item = response.parse()
            assert_matches_type(NewsItem, news_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        news_item = client.news.news_items.list()
        assert_matches_type(NewsItemListResponse, news_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        news_item = client.news.news_items.list(
            intercom_version="2.11",
        )
        assert_matches_type(NewsItemListResponse, news_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.news.news_items.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItemListResponse, news_item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.news.news_items.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_item = response.parse()
            assert_matches_type(NewsItemListResponse, news_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        news_item = client.news.news_items.delete(
            id=123,
        )
        assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Intercom) -> None:
        news_item = client.news.news_items.delete(
            id=123,
            intercom_version="2.11",
        )
        assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.news.news_items.with_raw_response.delete(
            id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Intercom) -> None:
        with client.news.news_items.with_streaming_response.delete(
            id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_item = response.parse()
            assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNewsItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        news_item = await async_client.news.news_items.create(
            sender_id=991268690,
            title="Halloween is here!",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        news_item = await async_client.news.news_items.create(
            sender_id=991268690,
            title="Halloween is here!",
            body="<p>New costumes in store for this spooky season</p>",
            deliver_silently=True,
            labels=["Product", "Update", "New"],
            newsfeed_assignments=[
                {
                    "newsfeed_id": 103,
                    "published_at": 1664638214,
                }
            ],
            reactions=["😆", "😅"],
            state="live",
            intercom_version="2.11",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.news.news_items.with_raw_response.create(
            sender_id=991268690,
            title="Halloween is here!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = await response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.news.news_items.with_streaming_response.create(
            sender_id=991268690,
            title="Halloween is here!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_item = await response.parse()
            assert_matches_type(NewsItem, news_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        news_item = await async_client.news.news_items.retrieve(
            id=123,
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        news_item = await async_client.news.news_items.retrieve(
            id=123,
            intercom_version="2.11",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.news.news_items.with_raw_response.retrieve(
            id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = await response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.news.news_items.with_streaming_response.retrieve(
            id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_item = await response.parse()
            assert_matches_type(NewsItem, news_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncIntercom) -> None:
        news_item = await async_client.news.news_items.update(
            id=123,
            sender_id=991268701,
            title="Christmas is here!",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIntercom) -> None:
        news_item = await async_client.news.news_items.update(
            id=123,
            sender_id=991268701,
            title="Christmas is here!",
            body="<p>New gifts in store for the jolly season</p>",
            deliver_silently=True,
            labels=["Product", "Update", "New"],
            newsfeed_assignments=[
                {
                    "newsfeed_id": 198313,
                    "published_at": 1674917488,
                },
                {
                    "newsfeed_id": 198313,
                    "published_at": 1674917488,
                },
                {
                    "newsfeed_id": 198313,
                    "published_at": 1674917488,
                },
            ],
            reactions=["😝", "😂"],
            state="live",
            intercom_version="2.11",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIntercom) -> None:
        response = await async_client.news.news_items.with_raw_response.update(
            id=123,
            sender_id=991268701,
            title="Christmas is here!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = await response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIntercom) -> None:
        async with async_client.news.news_items.with_streaming_response.update(
            id=123,
            sender_id=991268701,
            title="Christmas is here!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_item = await response.parse()
            assert_matches_type(NewsItem, news_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        news_item = await async_client.news.news_items.list()
        assert_matches_type(NewsItemListResponse, news_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        news_item = await async_client.news.news_items.list(
            intercom_version="2.11",
        )
        assert_matches_type(NewsItemListResponse, news_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.news.news_items.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = await response.parse()
        assert_matches_type(NewsItemListResponse, news_item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.news.news_items.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_item = await response.parse()
            assert_matches_type(NewsItemListResponse, news_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncIntercom) -> None:
        news_item = await async_client.news.news_items.delete(
            id=123,
        )
        assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncIntercom) -> None:
        news_item = await async_client.news.news_items.delete(
            id=123,
            intercom_version="2.11",
        )
        assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncIntercom) -> None:
        response = await async_client.news.news_items.with_raw_response.delete(
            id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = await response.parse()
        assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncIntercom) -> None:
        async with async_client.news.news_items.with_streaming_response.delete(
            id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news_item = await response.parse()
            assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])

        assert cast(Any, response.is_closed) is True
