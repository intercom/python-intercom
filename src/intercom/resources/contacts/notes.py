# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.shared import Note
from ...types.contacts import NoteList, note_create_params

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Notes", "AsyncNotes"]


class Notes(SyncAPIResource):
    with_raw_response: NotesWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = NotesWithRawResponse(self)

    def create(
        self,
        id: int,
        *,
        body: str,
        admin_id: str | NotGiven = NOT_GIVEN,
        contact_id: str | NotGiven = NOT_GIVEN,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/contacts/{id}/notes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteList,
        )


class AsyncNotes(AsyncAPIResource):
    with_raw_response: AsyncNotesWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncNotesWithRawResponse(self)

    async def create(
        self,
        id: int,
        *,
        body: str,
        admin_id: str | NotGiven = NOT_GIVEN,
        contact_id: str | NotGiven = NOT_GIVEN,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
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

    async def list(
        self,
        id: int,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/contacts/{id}/notes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteList,
        )


class NotesWithRawResponse:
    def __init__(self, notes: Notes) -> None:
        self.create = to_raw_response_wrapper(
            notes.create,
        )
        self.list = to_raw_response_wrapper(
            notes.list,
        )


class AsyncNotesWithRawResponse:
    def __init__(self, notes: AsyncNotes) -> None:
        self.create = async_to_raw_response_wrapper(
            notes.create,
        )
        self.list = async_to_raw_response_wrapper(
            notes.list,
        )
