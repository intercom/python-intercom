# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .newsfeeds import (
    NewsfeedsResource,
    AsyncNewsfeedsResource,
    NewsfeedsResourceWithRawResponse,
    AsyncNewsfeedsResourceWithRawResponse,
    NewsfeedsResourceWithStreamingResponse,
    AsyncNewsfeedsResourceWithStreamingResponse,
)
from .news_items import (
    NewsItemsResource,
    AsyncNewsItemsResource,
    NewsItemsResourceWithRawResponse,
    AsyncNewsItemsResourceWithRawResponse,
    NewsItemsResourceWithStreamingResponse,
    AsyncNewsItemsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .newsfeeds.newsfeeds import NewsfeedsResource, AsyncNewsfeedsResource

__all__ = ["NewsResource", "AsyncNewsResource"]


class NewsResource(SyncAPIResource):
    @cached_property
    def news_items(self) -> NewsItemsResource:
        return NewsItemsResource(self._client)

    @cached_property
    def newsfeeds(self) -> NewsfeedsResource:
        return NewsfeedsResource(self._client)

    @cached_property
    def with_raw_response(self) -> NewsResourceWithRawResponse:
        return NewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsResourceWithStreamingResponse:
        return NewsResourceWithStreamingResponse(self)


class AsyncNewsResource(AsyncAPIResource):
    @cached_property
    def news_items(self) -> AsyncNewsItemsResource:
        return AsyncNewsItemsResource(self._client)

    @cached_property
    def newsfeeds(self) -> AsyncNewsfeedsResource:
        return AsyncNewsfeedsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNewsResourceWithRawResponse:
        return AsyncNewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsResourceWithStreamingResponse:
        return AsyncNewsResourceWithStreamingResponse(self)


class NewsResourceWithRawResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

    @cached_property
    def news_items(self) -> NewsItemsResourceWithRawResponse:
        return NewsItemsResourceWithRawResponse(self._news.news_items)

    @cached_property
    def newsfeeds(self) -> NewsfeedsResourceWithRawResponse:
        return NewsfeedsResourceWithRawResponse(self._news.newsfeeds)


class AsyncNewsResourceWithRawResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

    @cached_property
    def news_items(self) -> AsyncNewsItemsResourceWithRawResponse:
        return AsyncNewsItemsResourceWithRawResponse(self._news.news_items)

    @cached_property
    def newsfeeds(self) -> AsyncNewsfeedsResourceWithRawResponse:
        return AsyncNewsfeedsResourceWithRawResponse(self._news.newsfeeds)


class NewsResourceWithStreamingResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

    @cached_property
    def news_items(self) -> NewsItemsResourceWithStreamingResponse:
        return NewsItemsResourceWithStreamingResponse(self._news.news_items)

    @cached_property
    def newsfeeds(self) -> NewsfeedsResourceWithStreamingResponse:
        return NewsfeedsResourceWithStreamingResponse(self._news.newsfeeds)


class AsyncNewsResourceWithStreamingResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

    @cached_property
    def news_items(self) -> AsyncNewsItemsResourceWithStreamingResponse:
        return AsyncNewsItemsResourceWithStreamingResponse(self._news.news_items)

    @cached_property
    def newsfeeds(self) -> AsyncNewsfeedsResourceWithStreamingResponse:
        return AsyncNewsfeedsResourceWithStreamingResponse(self._news.newsfeeds)
