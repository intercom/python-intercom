# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import ticket_type_create_params, ticket_type_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .attributes import (
    AttributesResource,
    AsyncAttributesResource,
    AttributesResourceWithRawResponse,
    AsyncAttributesResourceWithRawResponse,
    AttributesResourceWithStreamingResponse,
    AsyncAttributesResourceWithStreamingResponse,
)
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
from ...types.ticket_type import TicketType
from ...types.ticket_type_list import TicketTypeList

__all__ = ["TicketTypesResource", "AsyncTicketTypesResource"]


class TicketTypesResource(SyncAPIResource):
    @cached_property
    def attributes(self) -> AttributesResource:
        return AttributesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TicketTypesResourceWithRawResponse:
        return TicketTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TicketTypesResourceWithStreamingResponse:
        return TicketTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        category: Literal["Customer", "Back-office", "Tracker"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        icon: str | NotGiven = NOT_GIVEN,
        is_internal: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TicketType]:
        """
        You can create a new ticket type.

        > 📘 Creating ticket types.
        >
        > Every ticket type will be created with two default attributes: _default_title_
        > and _default_description_. For the `icon` propery, use an emoji from
        > [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/)

        Args:
          name: The name of the ticket type.

          category: Category of the Ticket Type.

          description: The description of the ticket type.

          icon: The icon of the ticket type.

          is_internal: Whether the tickets associated with this ticket type are intended for internal
              use only or will be shared with customers. This is currently a limited
              attribute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ticket_types",
            body=maybe_transform(
                {
                    "name": name,
                    "category": category,
                    "description": description,
                    "icon": icon,
                    "is_internal": is_internal,
                },
                ticket_type_create_params.TicketTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketType,
        )

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
    ) -> Optional[TicketType]:
        """
        You can fetch the details of a single ticket type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/ticket_types/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketType,
        )

    def update(
        self,
        id: str,
        *,
        archived: bool | NotGiven = NOT_GIVEN,
        category: Literal["Customer", "Back-office", "Tracker"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        icon: str | NotGiven = NOT_GIVEN,
        is_internal: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TicketType]:
        """
        You can update a ticket type.

        > 📘 Updating a ticket type.
        >
        > For the `icon` propery, use an emoji from
        > [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/)

        Args:
          archived: The archived status of the ticket type.

          category: Category of the Ticket Type.

          description: The description of the ticket type.

          icon: The icon of the ticket type.

          is_internal: Whether the tickets associated with this ticket type are intended for internal
              use only or will be shared with customers. This is currently a limited
              attribute.

          name: The name of the ticket type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/ticket_types/{id}",
            body=maybe_transform(
                {
                    "archived": archived,
                    "category": category,
                    "description": description,
                    "icon": icon,
                    "is_internal": is_internal,
                    "name": name,
                },
                ticket_type_update_params.TicketTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketType,
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
    ) -> TicketTypeList:
        """You can get a list of all ticket types for a workspace."""
        return self._get(
            "/ticket_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketTypeList,
        )


class AsyncTicketTypesResource(AsyncAPIResource):
    @cached_property
    def attributes(self) -> AsyncAttributesResource:
        return AsyncAttributesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTicketTypesResourceWithRawResponse:
        return AsyncTicketTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTicketTypesResourceWithStreamingResponse:
        return AsyncTicketTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        category: Literal["Customer", "Back-office", "Tracker"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        icon: str | NotGiven = NOT_GIVEN,
        is_internal: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TicketType]:
        """
        You can create a new ticket type.

        > 📘 Creating ticket types.
        >
        > Every ticket type will be created with two default attributes: _default_title_
        > and _default_description_. For the `icon` propery, use an emoji from
        > [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/)

        Args:
          name: The name of the ticket type.

          category: Category of the Ticket Type.

          description: The description of the ticket type.

          icon: The icon of the ticket type.

          is_internal: Whether the tickets associated with this ticket type are intended for internal
              use only or will be shared with customers. This is currently a limited
              attribute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ticket_types",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "category": category,
                    "description": description,
                    "icon": icon,
                    "is_internal": is_internal,
                },
                ticket_type_create_params.TicketTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketType,
        )

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
    ) -> Optional[TicketType]:
        """
        You can fetch the details of a single ticket type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/ticket_types/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketType,
        )

    async def update(
        self,
        id: str,
        *,
        archived: bool | NotGiven = NOT_GIVEN,
        category: Literal["Customer", "Back-office", "Tracker"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        icon: str | NotGiven = NOT_GIVEN,
        is_internal: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TicketType]:
        """
        You can update a ticket type.

        > 📘 Updating a ticket type.
        >
        > For the `icon` propery, use an emoji from
        > [Twemoji Cheatsheet](https://twemoji-cheatsheet.vercel.app/)

        Args:
          archived: The archived status of the ticket type.

          category: Category of the Ticket Type.

          description: The description of the ticket type.

          icon: The icon of the ticket type.

          is_internal: Whether the tickets associated with this ticket type are intended for internal
              use only or will be shared with customers. This is currently a limited
              attribute.

          name: The name of the ticket type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/ticket_types/{id}",
            body=await async_maybe_transform(
                {
                    "archived": archived,
                    "category": category,
                    "description": description,
                    "icon": icon,
                    "is_internal": is_internal,
                    "name": name,
                },
                ticket_type_update_params.TicketTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketType,
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
    ) -> TicketTypeList:
        """You can get a list of all ticket types for a workspace."""
        return await self._get(
            "/ticket_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketTypeList,
        )


class TicketTypesResourceWithRawResponse:
    def __init__(self, ticket_types: TicketTypesResource) -> None:
        self._ticket_types = ticket_types

        self.create = to_raw_response_wrapper(
            ticket_types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ticket_types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ticket_types.update,
        )
        self.list = to_raw_response_wrapper(
            ticket_types.list,
        )

    @cached_property
    def attributes(self) -> AttributesResourceWithRawResponse:
        return AttributesResourceWithRawResponse(self._ticket_types.attributes)


class AsyncTicketTypesResourceWithRawResponse:
    def __init__(self, ticket_types: AsyncTicketTypesResource) -> None:
        self._ticket_types = ticket_types

        self.create = async_to_raw_response_wrapper(
            ticket_types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ticket_types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ticket_types.update,
        )
        self.list = async_to_raw_response_wrapper(
            ticket_types.list,
        )

    @cached_property
    def attributes(self) -> AsyncAttributesResourceWithRawResponse:
        return AsyncAttributesResourceWithRawResponse(self._ticket_types.attributes)


class TicketTypesResourceWithStreamingResponse:
    def __init__(self, ticket_types: TicketTypesResource) -> None:
        self._ticket_types = ticket_types

        self.create = to_streamed_response_wrapper(
            ticket_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ticket_types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ticket_types.update,
        )
        self.list = to_streamed_response_wrapper(
            ticket_types.list,
        )

    @cached_property
    def attributes(self) -> AttributesResourceWithStreamingResponse:
        return AttributesResourceWithStreamingResponse(self._ticket_types.attributes)


class AsyncTicketTypesResourceWithStreamingResponse:
    def __init__(self, ticket_types: AsyncTicketTypesResource) -> None:
        self._ticket_types = ticket_types

        self.create = async_to_streamed_response_wrapper(
            ticket_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ticket_types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ticket_types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ticket_types.list,
        )

    @cached_property
    def attributes(self) -> AsyncAttributesResourceWithStreamingResponse:
        return AsyncAttributesResourceWithStreamingResponse(self._ticket_types.attributes)
