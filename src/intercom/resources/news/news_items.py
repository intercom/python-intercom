# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.news import news_item_create_params, news_item_update_params
from ..._base_client import (
    make_request_options,
)
from ...types.news.news_item import NewsItem
from ...types.shared.paginated_response import PaginatedResponse
from ...types.news.news_item_delete_response import NewsItemDeleteResponse

__all__ = ["NewsItemsResource", "AsyncNewsItemsResource"]


class NewsItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NewsItemsResourceWithRawResponse:
        return NewsItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsItemsResourceWithStreamingResponse:
        return NewsItemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        sender_id: int,
        title: str,
        body: str | NotGiven = NOT_GIVEN,
        deliver_silently: bool | NotGiven = NOT_GIVEN,
        labels: List[str] | NotGiven = NOT_GIVEN,
        newsfeed_assignments: Iterable[news_item_create_params.NewsfeedAssignment] | NotGiven = NOT_GIVEN,
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
        newsfeed_assignments: Iterable[news_item_update_params.NewsfeedAssignment] | NotGiven = NOT_GIVEN,
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


class AsyncNewsItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNewsItemsResourceWithRawResponse:
        return AsyncNewsItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsItemsResourceWithStreamingResponse:
        return AsyncNewsItemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        sender_id: int,
        title: str,
        body: str | NotGiven = NOT_GIVEN,
        deliver_silently: bool | NotGiven = NOT_GIVEN,
        labels: List[str] | NotGiven = NOT_GIVEN,
        newsfeed_assignments: Iterable[news_item_create_params.NewsfeedAssignment] | NotGiven = NOT_GIVEN,
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
            body=await async_maybe_transform(
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
        newsfeed_assignments: Iterable[news_item_update_params.NewsfeedAssignment] | NotGiven = NOT_GIVEN,
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
            body=await async_maybe_transform(
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


class NewsItemsResourceWithRawResponse:
    def __init__(self, news_items: NewsItemsResource) -> None:
        self._news_items = news_items

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


class AsyncNewsItemsResourceWithRawResponse:
    def __init__(self, news_items: AsyncNewsItemsResource) -> None:
        self._news_items = news_items

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


class NewsItemsResourceWithStreamingResponse:
    def __init__(self, news_items: NewsItemsResource) -> None:
        self._news_items = news_items

        self.create = to_streamed_response_wrapper(
            news_items.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            news_items.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            news_items.update,
        )
        self.list = to_streamed_response_wrapper(
            news_items.list,
        )
        self.delete = to_streamed_response_wrapper(
            news_items.delete,
        )


class AsyncNewsItemsResourceWithStreamingResponse:
    def __init__(self, news_items: AsyncNewsItemsResource) -> None:
        self._news_items = news_items

        self.create = async_to_streamed_response_wrapper(
            news_items.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            news_items.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            news_items.update,
        )
        self.list = async_to_streamed_response_wrapper(
            news_items.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            news_items.delete,
        )
