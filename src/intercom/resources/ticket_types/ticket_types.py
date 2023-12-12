# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    TicketType,
    TicketTypeList,
    ticket_type_create_params,
    ticket_type_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .attributes import (
    Attributes,
    AsyncAttributes,
    AttributesWithRawResponse,
    AsyncAttributesWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["TicketTypes", "AsyncTicketTypes"]


class TicketTypes(SyncAPIResource):
    attributes: Attributes
    with_raw_response: TicketTypesWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.attributes = Attributes(client)
        self.with_raw_response = TicketTypesWithRawResponse(self)

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


class AsyncTicketTypes(AsyncAPIResource):
    attributes: AsyncAttributes
    with_raw_response: AsyncTicketTypesWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.attributes = AsyncAttributes(client)
        self.with_raw_response = AsyncTicketTypesWithRawResponse(self)

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
        return await self._put(
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


class TicketTypesWithRawResponse:
    def __init__(self, ticket_types: TicketTypes) -> None:
        self.attributes = AttributesWithRawResponse(ticket_types.attributes)

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


class AsyncTicketTypesWithRawResponse:
    def __init__(self, ticket_types: AsyncTicketTypes) -> None:
        self.attributes = AsyncAttributesWithRawResponse(ticket_types.attributes)

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
