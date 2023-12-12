# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .newsfeeds import (
    Newsfeeds,
    AsyncNewsfeeds,
    NewsfeedsWithRawResponse,
    AsyncNewsfeedsWithRawResponse,
)
from .news_items import (
    NewsItems,
    AsyncNewsItems,
    NewsItemsWithRawResponse,
    AsyncNewsItemsWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["News", "AsyncNews"]


class News(SyncAPIResource):
    news_items: NewsItems
    newsfeeds: Newsfeeds
    with_raw_response: NewsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.news_items = NewsItems(client)
        self.newsfeeds = Newsfeeds(client)
        self.with_raw_response = NewsWithRawResponse(self)


class AsyncNews(AsyncAPIResource):
    news_items: AsyncNewsItems
    newsfeeds: AsyncNewsfeeds
    with_raw_response: AsyncNewsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.news_items = AsyncNewsItems(client)
        self.newsfeeds = AsyncNewsfeeds(client)
        self.with_raw_response = AsyncNewsWithRawResponse(self)


class NewsWithRawResponse:
    def __init__(self, news: News) -> None:
        self.news_items = NewsItemsWithRawResponse(news.news_items)
        self.newsfeeds = NewsfeedsWithRawResponse(news.newsfeeds)


class AsyncNewsWithRawResponse:
    def __init__(self, news: AsyncNews) -> None:
        self.news_items = AsyncNewsItemsWithRawResponse(news.news_items)
        self.newsfeeds = AsyncNewsfeedsWithRawResponse(news.newsfeeds)
