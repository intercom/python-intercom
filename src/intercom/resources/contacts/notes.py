# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
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
from ..._base_client import (
    make_request_options,
)
from ...types.contacts import note_create_params
from ...types.shared.note import Note
from ...types.contacts.note_list import NoteList

__all__ = ["NotesResource", "AsyncNotesResource"]


class NotesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotesResourceWithRawResponse:
        return NotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotesResourceWithStreamingResponse:
        return NotesResourceWithStreamingResponse(self)

    def create(
        self,
        id: int,
        *,
        body: str,
        admin_id: str | NotGiven = NOT_GIVEN,
        contact_id: str | NotGiven = NOT_GIVEN,
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
    ) -> Note:
        """
        You can add a note to a single contact.

        Args:
          body: The text of the note.

          admin_id: The unique identifier of a given admin.

          contact_id: The unique identifier of a given contact.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._post(
            f"/contacts/{id}/notes",
            body=maybe_transform(
                {
                    "body": body,
                    "admin_id": admin_id,
                    "contact_id": contact_id,
                },
                note_create_params.NoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Note,
        )

    def list(
        self,
        id: int,
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
    ) -> NoteList:
        """
        You can fetch a list of notes that are associated to a contact.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._get(
            f"/contacts/{id}/notes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteList,
        )


class AsyncNotesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotesResourceWithRawResponse:
        return AsyncNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotesResourceWithStreamingResponse:
        return AsyncNotesResourceWithStreamingResponse(self)

    async def create(
        self,
        id: int,
        *,
        body: str,
        admin_id: str | NotGiven = NOT_GIVEN,
        contact_id: str | NotGiven = NOT_GIVEN,
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
    ) -> Note:
        """
        You can add a note to a single contact.

        Args:
          body: The text of the note.

          admin_id: The unique identifier of a given admin.

          contact_id: The unique identifier of a given contact.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._post(
            f"/contacts/{id}/notes",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "admin_id": admin_id,
                    "contact_id": contact_id,
                },
                note_create_params.NoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Note,
        )

    async def list(
        self,
        id: int,
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
    ) -> NoteList:
        """
        You can fetch a list of notes that are associated to a contact.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._get(
            f"/contacts/{id}/notes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteList,
        )


class NotesResourceWithRawResponse:
    def __init__(self, notes: NotesResource) -> None:
        self._notes = notes

        self.create = to_raw_response_wrapper(
            notes.create,
        )
        self.list = to_raw_response_wrapper(
            notes.list,
        )


class AsyncNotesResourceWithRawResponse:
    def __init__(self, notes: AsyncNotesResource) -> None:
        self._notes = notes

        self.create = async_to_raw_response_wrapper(
            notes.create,
        )
        self.list = async_to_raw_response_wrapper(
            notes.list,
        )


class NotesResourceWithStreamingResponse:
    def __init__(self, notes: NotesResource) -> None:
        self._notes = notes

        self.create = to_streamed_response_wrapper(
            notes.create,
        )
        self.list = to_streamed_response_wrapper(
            notes.list,
        )


class AsyncNotesResourceWithStreamingResponse:
    def __init__(self, notes: AsyncNotesResource) -> None:
        self._notes = notes

        self.create = async_to_streamed_response_wrapper(
            notes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            notes.list,
        )
