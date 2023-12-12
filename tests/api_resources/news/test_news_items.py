# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.news import NewsItem, NewsItemDeleteResponse
from intercom.types.shared import PaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestNewsItems:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        news_item = client.news.news_items.create(
            sender_id=991266564,
            title="Halloween is here!",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        news_item = client.news.news_items.create(
            sender_id=991266564,
            title="Halloween is here!",
            body="<p>New costumes in store for this spooky season</p>",
            deliver_silently=True,
            labels=["Product", "Update", "New"],
            newsfeed_assignments=[
                {
                    "newsfeed_id": 3,
                    "published_at": 1664638214,
                }
            ],
            reactions=["😆", "😅"],
            state="live",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.news.news_items.with_raw_response.create(
            sender_id=991266564,
            title="Halloween is here!",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        news_item = client.news.news_items.retrieve(
            0,
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.news.news_items.with_raw_response.retrieve(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        news_item = client.news.news_items.update(
            0,
            sender_id=991266575,
            title="Christmas is here!",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        news_item = client.news.news_items.update(
            0,
            sender_id=991266575,
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
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.news.news_items.with_raw_response.update(
            0,
            sender_id=991266575,
            title="Christmas is here!",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        news_item = client.news.news_items.list()
        assert_matches_type(PaginatedResponse, news_item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.news.news_items.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(PaginatedResponse, news_item, path=["response"])

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        news_item = client.news.news_items.delete(
            0,
        )
        assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.news.news_items.with_raw_response.delete(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])


class TestAsyncNewsItems:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        news_item = await client.news.news_items.create(
            sender_id=991266564,
            title="Halloween is here!",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        news_item = await client.news.news_items.create(
            sender_id=991266564,
            title="Halloween is here!",
            body="<p>New costumes in store for this spooky season</p>",
            deliver_silently=True,
            labels=["Product", "Update", "New"],
            newsfeed_assignments=[
                {
                    "newsfeed_id": 3,
                    "published_at": 1664638214,
                }
            ],
            reactions=["😆", "😅"],
            state="live",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.news.news_items.with_raw_response.create(
            sender_id=991266564,
            title="Halloween is here!",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        news_item = await client.news.news_items.retrieve(
            0,
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.news.news_items.with_raw_response.retrieve(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIntercom) -> None:
        news_item = await client.news.news_items.update(
            0,
            sender_id=991266575,
            title="Christmas is here!",
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIntercom) -> None:
        news_item = await client.news.news_items.update(
            0,
            sender_id=991266575,
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
        )
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncIntercom) -> None:
        response = await client.news.news_items.with_raw_response.update(
            0,
            sender_id=991266575,
            title="Christmas is here!",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItem, news_item, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        news_item = await client.news.news_items.list()
        assert_matches_type(PaginatedResponse, news_item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.news.news_items.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(PaginatedResponse, news_item, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncIntercom) -> None:
        news_item = await client.news.news_items.delete(
            0,
        )
        assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncIntercom) -> None:
        response = await client.news.news_items.with_raw_response.delete(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news_item = response.parse()
        assert_matches_type(NewsItemDeleteResponse, news_item, path=["response"])
