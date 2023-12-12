# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...types.news import (
    NewsItem,
    NewsItemDeleteResponse,
    news_item_create_params,
    news_item_update_params,
)
from ..._base_client import make_request_options
from ...types.shared import PaginatedResponse

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["NewsItems", "AsyncNewsItems"]


class NewsItems(SyncAPIResource):
    with_raw_response: NewsItemsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = NewsItemsWithRawResponse(self)

    def create(
        self,
        *,
        sender_id: int,
        title: str,
        body: str | NotGiven = NOT_GIVEN,
        deliver_silently: bool | NotGiven = NOT_GIVEN,
        labels: List[str] | NotGiven = NOT_GIVEN,
        newsfeed_assignments: List[news_item_create_params.NewsfeedAssignment] | NotGiven = NOT_GIVEN,
        reactions: List[Optional[str]] | NotGiven = NOT_GIVEN,
        state: Literal["draft", "live"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewsItem:
        """
        You can create a news item

        Args:
          sender_id: The id of the sender of the news item. Must be a teammate on the workspace.

          title: The title of the news item.

          body: The news item body, which may contain HTML.

          deliver_silently: When set to `true`, the news item will appear in the messenger newsfeed without
              showing a notification badge.

          labels: Label names displayed to users to categorize the news item.

          newsfeed_assignments: A list of newsfeed_assignments to assign to the specified newsfeed.

          reactions: Ordered list of emoji reactions to the news item. When empty, reactions are
              disabled.

          state: News items will not be visible to your users in the assigned newsfeeds until
              they are set live.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/news/news_items",
            body=maybe_transform(
                {
                    "sender_id": sender_id,
                    "title": title,
                    "body": body,
                    "deliver_silently": deliver_silently,
                    "labels": labels,
                    "newsfeed_assignments": newsfeed_assignments,
                    "reactions": reactions,
                    "state": state,
                },
                news_item_create_params.NewsItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsItem,
        )

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewsItem:
        """
        You can fetch the details of a single news item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/news/news_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsItem,
        )

    def update(
        self,
        id: int,
        *,
        sender_id: int,
        title: str,
        body: str | NotGiven = NOT_GIVEN,
        deliver_silently: bool | NotGiven = NOT_GIVEN,
        labels: List[str] | NotGiven = NOT_GIVEN,
        newsfeed_assignments: List[news_item_update_params.NewsfeedAssignment] | NotGiven = NOT_GIVEN,
        reactions: List[Optional[str]] | NotGiven = NOT_GIVEN,
        state: Literal["draft", "live"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewsItem:
        """Update a news item

        Args:
          sender_id: The id of the sender of the news item.

        Must be a teammate on the workspace.

          title: The title of the news item.

          body: The news item body, which may contain HTML.

          deliver_silently: When set to `true`, the news item will appear in the messenger newsfeed without
              showing a notification badge.

          labels: Label names displayed to users to categorize the news item.

          newsfeed_assignments: A list of newsfeed_assignments to assign to the specified newsfeed.

          reactions: Ordered list of emoji reactions to the news item. When empty, reactions are
              disabled.

          state: News items will not be visible to your users in the assigned newsfeeds until
              they are set live.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/news/news_items/{id}",
            body=maybe_transform(
                {
                    "sender_id": sender_id,
                    "title": title,
                    "body": body,
                    "deliver_silently": deliver_silently,
                    "labels": labels,
                    "newsfeed_assignments": newsfeed_assignments,
                    "reactions": reactions,
                    "state": state,
                },
                news_item_update_params.NewsItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsItem,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponse:
        """You can fetch a list of all news items"""
        return self._get(
            "/news/news_items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaginatedResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewsItemDeleteResponse:
        """
        You can delete a single news item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/news/news_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsItemDeleteResponse,
        )


class AsyncNewsItems(AsyncAPIResource):
    with_raw_response: AsyncNewsItemsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncNewsItemsWithRawResponse(self)

    async def create(
        self,
        *,
        sender_id: int,
        title: str,
        body: str | NotGiven = NOT_GIVEN,
        deliver_silently: bool | NotGiven = NOT_GIVEN,
        labels: List[str] | NotGiven = NOT_GIVEN,
        newsfeed_assignments: List[news_item_create_params.NewsfeedAssignment] | NotGiven = NOT_GIVEN,
        reactions: List[Optional[str]] | NotGiven = NOT_GIVEN,
        state: Literal["draft", "live"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewsItem:
        """
        You can create a news item

        Args:
          sender_id: The id of the sender of the news item. Must be a teammate on the workspace.

          title: The title of the news item.

          body: The news item body, which may contain HTML.

          deliver_silently: When set to `true`, the news item will appear in the messenger newsfeed without
              showing a notification badge.

          labels: Label names displayed to users to categorize the news item.

          newsfeed_assignments: A list of newsfeed_assignments to assign to the specified newsfeed.

          reactions: Ordered list of emoji reactions to the news item. When empty, reactions are
              disabled.

          state: News items will not be visible to your users in the assigned newsfeeds until
              they are set live.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/news/news_items",
            body=maybe_transform(
                {
                    "sender_id": sender_id,
                    "title": title,
                    "body": body,
                    "deliver_silently": deliver_silently,
                    "labels": labels,
                    "newsfeed_assignments": newsfeed_assignments,
                    "reactions": reactions,
                    "state": state,
                },
                news_item_create_params.NewsItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsItem,
        )

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewsItem:
        """
        You can fetch the details of a single news item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/news/news_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsItem,
        )

    async def update(
        self,
        id: int,
        *,
        sender_id: int,
        title: str,
        body: str | NotGiven = NOT_GIVEN,
        deliver_silently: bool | NotGiven = NOT_GIVEN,
        labels: List[str] | NotGiven = NOT_GIVEN,
        newsfeed_assignments: List[news_item_update_params.NewsfeedAssignment] | NotGiven = NOT_GIVEN,
        reactions: List[Optional[str]] | NotGiven = NOT_GIVEN,
        state: Literal["draft", "live"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewsItem:
        """Update a news item

        Args:
          sender_id: The id of the sender of the news item.

        Must be a teammate on the workspace.

          title: The title of the news item.

          body: The news item body, which may contain HTML.

          deliver_silently: When set to `true`, the news item will appear in the messenger newsfeed without
              showing a notification badge.

          labels: Label names displayed to users to categorize the news item.

          newsfeed_assignments: A list of newsfeed_assignments to assign to the specified newsfeed.

          reactions: Ordered list of emoji reactions to the news item. When empty, reactions are
              disabled.

          state: News items will not be visible to your users in the assigned newsfeeds until
              they are set live.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/news/news_items/{id}",
            body=maybe_transform(
                {
                    "sender_id": sender_id,
                    "title": title,
                    "body": body,
                    "deliver_silently": deliver_silently,
                    "labels": labels,
                    "newsfeed_assignments": newsfeed_assignments,
                    "reactions": reactions,
                    "state": state,
                },
                news_item_update_params.NewsItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsItem,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponse:
        """You can fetch a list of all news items"""
        return await self._get(
            "/news/news_items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaginatedResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewsItemDeleteResponse:
        """
        You can delete a single news item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/news/news_items/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsItemDeleteResponse,
        )


class NewsItemsWithRawResponse:
    def __init__(self, news_items: NewsItems) -> None:
        self.create = to_raw_response_wrapper(
            news_items.create,
        )
        self.retrieve = to_raw_response_wrapper(
            news_items.retrieve,
        )
        self.update = to_raw_response_wrapper(
            news_items.update,
        )
        self.list = to_raw_response_wrapper(
            news_items.list,
        )
        self.delete = to_raw_response_wrapper(
            news_items.delete,
        )


class AsyncNewsItemsWithRawResponse:
    def __init__(self, news_items: AsyncNewsItems) -> None:
        self.create = async_to_raw_response_wrapper(
            news_items.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            news_items.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            news_items.update,
        )
        self.list = async_to_raw_response_wrapper(
            news_items.list,
        )
        self.delete = async_to_raw_response_wrapper(
            news_items.delete,
        )
