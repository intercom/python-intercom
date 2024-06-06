# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import segment_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.segment import Segment
from ..types.segment_list import SegmentList

__all__ = ["SegmentsResource", "AsyncSegmentsResource"]


class SegmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SegmentsResourceWithRawResponse:
        return SegmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SegmentsResourceWithStreamingResponse:
        return SegmentsResourceWithStreamingResponse(self)

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
    ) -> Segment:
        """
        You can fetch the details of a single segment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/segments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Segment,
        )

    def list(
        self,
        *,
        include_count: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SegmentList:
        """
        You can fetch a list of all segments.

        Args:
          include_count: It includes the count of contacts that belong to each segment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/segments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_count": include_count}, segment_list_params.SegmentListParams),
            ),
            cast_to=SegmentList,
        )


class AsyncSegmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSegmentsResourceWithRawResponse:
        return AsyncSegmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSegmentsResourceWithStreamingResponse:
        return AsyncSegmentsResourceWithStreamingResponse(self)

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
    ) -> Segment:
        """
        You can fetch the details of a single segment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/segments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Segment,
        )

    async def list(
        self,
        *,
        include_count: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SegmentList:
        """
        You can fetch a list of all segments.

        Args:
          include_count: It includes the count of contacts that belong to each segment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/segments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_count": include_count}, segment_list_params.SegmentListParams
                ),
            ),
            cast_to=SegmentList,
        )


class SegmentsResourceWithRawResponse:
    def __init__(self, segments: SegmentsResource) -> None:
        self._segments = segments

        self.retrieve = to_raw_response_wrapper(
            segments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            segments.list,
        )


class AsyncSegmentsResourceWithRawResponse:
    def __init__(self, segments: AsyncSegmentsResource) -> None:
        self._segments = segments

        self.retrieve = async_to_raw_response_wrapper(
            segments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            segments.list,
        )


class SegmentsResourceWithStreamingResponse:
    def __init__(self, segments: SegmentsResource) -> None:
        self._segments = segments

        self.retrieve = to_streamed_response_wrapper(
            segments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            segments.list,
        )


class AsyncSegmentsResourceWithStreamingResponse:
    def __init__(self, segments: AsyncSegmentsResource) -> None:
        self._segments = segments

        self.retrieve = async_to_streamed_response_wrapper(
            segments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            segments.list,
        )
