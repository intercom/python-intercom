# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import is_given, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.contacts.contact_segments import ContactSegments

__all__ = ["SegmentsResource", "AsyncSegmentsResource"]


class SegmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SegmentsResourceWithRawResponse:
        return SegmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SegmentsResourceWithStreamingResponse:
        return SegmentsResourceWithStreamingResponse(self)

    def list(
        self,
        contact_id: str,
        *,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactSegments:
        """
        You can fetch a list of segments that are associated to a contact.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._get(
            f"/contacts/{contact_id}/segments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactSegments,
        )


class AsyncSegmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSegmentsResourceWithRawResponse:
        return AsyncSegmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSegmentsResourceWithStreamingResponse:
        return AsyncSegmentsResourceWithStreamingResponse(self)

    async def list(
        self,
        contact_id: str,
        *,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContactSegments:
        """
        You can fetch a list of segments that are associated to a contact.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/contacts/{contact_id}/segments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactSegments,
        )


class SegmentsResourceWithRawResponse:
    def __init__(self, segments: SegmentsResource) -> None:
        self._segments = segments

        self.list = to_raw_response_wrapper(
            segments.list,
        )


class AsyncSegmentsResourceWithRawResponse:
    def __init__(self, segments: AsyncSegmentsResource) -> None:
        self._segments = segments

        self.list = async_to_raw_response_wrapper(
            segments.list,
        )


class SegmentsResourceWithStreamingResponse:
    def __init__(self, segments: SegmentsResource) -> None:
        self._segments = segments

        self.list = to_streamed_response_wrapper(
            segments.list,
        )


class AsyncSegmentsResourceWithStreamingResponse:
    def __init__(self, segments: AsyncSegmentsResource) -> None:
        self._segments = segments

        self.list = async_to_streamed_response_wrapper(
            segments.list,
        )
