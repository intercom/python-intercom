# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.shared import Tag
from ...types.tickets import tag_create_params, tag_remove_params

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Tags", "AsyncTags"]


class Tags(SyncAPIResource):
    with_raw_response: TagsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = TagsWithRawResponse(self)

    def create(
        self,
        ticket_id: str,
        *,
        id: str,
        admin_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tag:
        """You can tag a specific ticket.

        This will return a tag object for the tag that
        was added to the ticket.

        Args:
          id: The unique identifier for the tag which is given by Intercom

          admin_id: The unique identifier for the admin which is given by Intercom.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/tickets/{ticket_id}/tags",
            body=maybe_transform(
                {
                    "id": id,
                    "admin_id": admin_id,
                },
                tag_create_params.TagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    def remove(
        self,
        id: str,
        *,
        ticket_id: str,
        admin_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tag:
        """You can remove tag from a specific ticket.

        This will return a tag object for the
        tag that was removed from the ticket.

        Args:
          admin_id: The unique identifier for the admin which is given by Intercom.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/tickets/{ticket_id}/tags/{id}",
            body=maybe_transform({"admin_id": admin_id}, tag_remove_params.TagRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )


class AsyncTags(AsyncAPIResource):
    with_raw_response: AsyncTagsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncTagsWithRawResponse(self)

    async def create(
        self,
        ticket_id: str,
        *,
        id: str,
        admin_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tag:
        """You can tag a specific ticket.

        This will return a tag object for the tag that
        was added to the ticket.

        Args:
          id: The unique identifier for the tag which is given by Intercom

          admin_id: The unique identifier for the admin which is given by Intercom.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/tickets/{ticket_id}/tags",
            body=maybe_transform(
                {
                    "id": id,
                    "admin_id": admin_id,
                },
                tag_create_params.TagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )

    async def remove(
        self,
        id: str,
        *,
        ticket_id: str,
        admin_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tag:
        """You can remove tag from a specific ticket.

        This will return a tag object for the
        tag that was removed from the ticket.

        Args:
          admin_id: The unique identifier for the admin which is given by Intercom.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/tickets/{ticket_id}/tags/{id}",
            body=maybe_transform({"admin_id": admin_id}, tag_remove_params.TagRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tag,
        )


class TagsWithRawResponse:
    def __init__(self, tags: Tags) -> None:
        self.create = to_raw_response_wrapper(
            tags.create,
        )
        self.remove = to_raw_response_wrapper(
            tags.remove,
        )


class AsyncTagsWithRawResponse:
    def __init__(self, tags: AsyncTags) -> None:
        self.create = async_to_raw_response_wrapper(
            tags.create,
        )
        self.remove = async_to_raw_response_wrapper(
            tags.remove,
        )
