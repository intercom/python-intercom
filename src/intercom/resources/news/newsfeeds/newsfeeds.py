# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
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
from ....types.news.newsfeed import Newsfeed
from ....types.shared.paginated_response import PaginatedResponse

__all__ = ["NewsfeedsResource", "AsyncNewsfeedsResource"]


class NewsfeedsResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> NewsfeedsResourceWithRawResponse:
        return NewsfeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsfeedsResourceWithStreamingResponse:
        return NewsfeedsResourceWithStreamingResponse(self)

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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


class AsyncNewsfeedsResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNewsfeedsResourceWithRawResponse:
        return AsyncNewsfeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsfeedsResourceWithStreamingResponse:
        return AsyncNewsfeedsResourceWithStreamingResponse(self)

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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


class NewsfeedsResourceWithRawResponse:
    def __init__(self, newsfeeds: NewsfeedsResource) -> None:
        self._newsfeeds = newsfeeds

        self.retrieve = to_raw_response_wrapper(
            newsfeeds.retrieve,
        )
        self.list = to_raw_response_wrapper(
            newsfeeds.list,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._newsfeeds.items)


class AsyncNewsfeedsResourceWithRawResponse:
    def __init__(self, newsfeeds: AsyncNewsfeedsResource) -> None:
        self._newsfeeds = newsfeeds

        self.retrieve = async_to_raw_response_wrapper(
            newsfeeds.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            newsfeeds.list,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._newsfeeds.items)


class NewsfeedsResourceWithStreamingResponse:
    def __init__(self, newsfeeds: NewsfeedsResource) -> None:
        self._newsfeeds = newsfeeds

        self.retrieve = to_streamed_response_wrapper(
            newsfeeds.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            newsfeeds.list,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._newsfeeds.items)


class AsyncNewsfeedsResourceWithStreamingResponse:
    def __init__(self, newsfeeds: AsyncNewsfeedsResource) -> None:
        self._newsfeeds = newsfeeds

        self.retrieve = async_to_streamed_response_wrapper(
            newsfeeds.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            newsfeeds.list,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._newsfeeds.items)
