# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.shared.paginated_response import PaginatedResponse

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponse:
        """
        You can fetch a list of all news items that are live on a given newsfeed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/news/newsfeeds/{id}/items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaginatedResponse,
        )


class AsyncItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponse:
        """
        You can fetch a list of all news items that are live on a given newsfeed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/news/newsfeeds/{id}/items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaginatedResponse,
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.list = to_raw_response_wrapper(
            items.list,
        )


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.list = async_to_raw_response_wrapper(
            items.list,
        )


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.list = to_streamed_response_wrapper(
            items.list,
        )


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.list = async_to_streamed_response_wrapper(
            items.list,
        )
