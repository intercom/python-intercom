# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from .items import Items, AsyncItems, ItemsWithRawResponse, AsyncItemsWithRawResponse
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ....types.news import Newsfeed
from ...._base_client import make_request_options
from ....types.shared import PaginatedResponse

if TYPE_CHECKING:
    from ...._client import Intercom, AsyncIntercom

__all__ = ["Newsfeeds", "AsyncNewsfeeds"]


class Newsfeeds(SyncAPIResource):
    items: Items
    with_raw_response: NewsfeedsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.items = Items(client)
        self.with_raw_response = NewsfeedsWithRawResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Newsfeed:
        """
        You can fetch the details of a single newsfeed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/news/newsfeeds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Newsfeed,
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
        """You can fetch a list of all newsfeeds"""
        return self._get(
            "/news/newsfeeds",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaginatedResponse,
        )


class AsyncNewsfeeds(AsyncAPIResource):
    items: AsyncItems
    with_raw_response: AsyncNewsfeedsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.items = AsyncItems(client)
        self.with_raw_response = AsyncNewsfeedsWithRawResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Newsfeed:
        """
        You can fetch the details of a single newsfeed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/news/newsfeeds/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Newsfeed,
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
        """You can fetch a list of all newsfeeds"""
        return await self._get(
            "/news/newsfeeds",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaginatedResponse,
        )


class NewsfeedsWithRawResponse:
    def __init__(self, newsfeeds: Newsfeeds) -> None:
        self.items = ItemsWithRawResponse(newsfeeds.items)

        self.retrieve = to_raw_response_wrapper(
            newsfeeds.retrieve,
        )
        self.list = to_raw_response_wrapper(
            newsfeeds.list,
        )


class AsyncNewsfeedsWithRawResponse:
    def __init__(self, newsfeeds: AsyncNewsfeeds) -> None:
        self.items = AsyncItemsWithRawResponse(newsfeeds.items)

        self.retrieve = async_to_raw_response_wrapper(
            newsfeeds.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            newsfeeds.list,
        )
