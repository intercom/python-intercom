# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.shared.note import Note

__all__ = ["NotesResource", "AsyncNotesResource"]


class NotesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotesResourceWithRawResponse:
        return NotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotesResourceWithStreamingResponse:
        return NotesResourceWithStreamingResponse(self)

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
    ) -> Note:
        """
        You can fetch the details of a single note.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/notes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Note,
        )


class AsyncNotesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotesResourceWithRawResponse:
        return AsyncNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotesResourceWithStreamingResponse:
        return AsyncNotesResourceWithStreamingResponse(self)

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
    ) -> Note:
        """
        You can fetch the details of a single note.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/notes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Note,
        )


class NotesResourceWithRawResponse:
    def __init__(self, notes: NotesResource) -> None:
        self._notes = notes

        self.retrieve = to_raw_response_wrapper(
            notes.retrieve,
        )


class AsyncNotesResourceWithRawResponse:
    def __init__(self, notes: AsyncNotesResource) -> None:
        self._notes = notes

        self.retrieve = async_to_raw_response_wrapper(
            notes.retrieve,
        )


class NotesResourceWithStreamingResponse:
    def __init__(self, notes: NotesResource) -> None:
        self._notes = notes

        self.retrieve = to_streamed_response_wrapper(
            notes.retrieve,
        )


class AsyncNotesResourceWithStreamingResponse:
    def __init__(self, notes: AsyncNotesResource) -> None:
        self._notes = notes

        self.retrieve = async_to_streamed_response_wrapper(
            notes.retrieve,
        )
