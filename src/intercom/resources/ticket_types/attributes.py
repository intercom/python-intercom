# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
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
from ...types.ticket_types import attribute_create_params, attribute_update_params
from ...types.shared.ticket_type_attribute import TicketTypeAttribute

__all__ = ["AttributesResource", "AsyncAttributesResource"]


class AttributesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttributesResourceWithRawResponse:
        return AttributesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttributesResourceWithStreamingResponse:
        return AttributesResourceWithStreamingResponse(self)

    def create(
        self,
        ticket_type_id: str,
        *,
        data_type: Literal["string", "list", "integer", "decimal", "boolean", "datetime", "files"],
        description: str,
        name: str,
        allow_multiple_values: bool | NotGiven = NOT_GIVEN,
        list_items: str | NotGiven = NOT_GIVEN,
        multiline: bool | NotGiven = NOT_GIVEN,
        required_to_create: bool | NotGiven = NOT_GIVEN,
        required_to_create_for_contacts: bool | NotGiven = NOT_GIVEN,
        visible_on_create: bool | NotGiven = NOT_GIVEN,
        visible_to_contacts: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TicketTypeAttribute]:
        """
        You can create a new attribute for a ticket type.

        Args:
          data_type: The data type of the attribute

          description: The description of the attribute presented to the teammate or contact

          name: The name of the ticket type attribute

          allow_multiple_values: Whether the attribute allows multiple files to be attached to it (only
              applicable to file attributes)

          list_items: A comma delimited list of items for the attribute value (only applicable to list
              attributes)

          multiline: Whether the attribute allows multiple lines of text (only applicable to string
              attributes)

          required_to_create: Whether the attribute is required to be filled in when teammates are creating
              the ticket in Inbox.

          required_to_create_for_contacts: Whether the attribute is required to be filled in when contacts are creating the
              ticket in Messenger.

          visible_on_create: Whether the attribute is visible to teammates when creating a ticket in Inbox.

          visible_to_contacts: Whether the attribute is visible to contacts when creating a ticket in
              Messenger.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticket_type_id:
            raise ValueError(f"Expected a non-empty value for `ticket_type_id` but received {ticket_type_id!r}")
        return self._post(
            f"/ticket_types/{ticket_type_id}/attributes",
            body=maybe_transform(
                {
                    "data_type": data_type,
                    "description": description,
                    "name": name,
                    "allow_multiple_values": allow_multiple_values,
                    "list_items": list_items,
                    "multiline": multiline,
                    "required_to_create": required_to_create,
                    "required_to_create_for_contacts": required_to_create_for_contacts,
                    "visible_on_create": visible_on_create,
                    "visible_to_contacts": visible_to_contacts,
                },
                attribute_create_params.AttributeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketTypeAttribute,
        )

    def update(
        self,
        id: str,
        *,
        ticket_type_id: str,
        allow_multiple_values: bool | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        list_items: str | NotGiven = NOT_GIVEN,
        multiline: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        required_to_create: bool | NotGiven = NOT_GIVEN,
        required_to_create_for_contacts: bool | NotGiven = NOT_GIVEN,
        visible_on_create: bool | NotGiven = NOT_GIVEN,
        visible_to_contacts: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TicketTypeAttribute]:
        """
        You can update an existing attribute for a ticket type.

        Args:
          allow_multiple_values: Whether the attribute allows multiple files to be attached to it (only
              applicable to file attributes)

          archived: Whether the attribute should be archived and not shown during creation of the
              ticket (it will still be present on previously created tickets)

          description: The description of the attribute presented to the teammate or contact

          list_items: A comma delimited list of items for the attribute value (only applicable to list
              attributes)

          multiline: Whether the attribute allows multiple lines of text (only applicable to string
              attributes)

          name: The name of the ticket type attribute

          required_to_create: Whether the attribute is required to be filled in when teammates are creating
              the ticket in Inbox.

          required_to_create_for_contacts: Whether the attribute is required to be filled in when contacts are creating the
              ticket in Messenger.

          visible_on_create: Whether the attribute is visible to teammates when creating a ticket in Inbox.

          visible_to_contacts: Whether the attribute is visible to contacts when creating a ticket in
              Messenger.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticket_type_id:
            raise ValueError(f"Expected a non-empty value for `ticket_type_id` but received {ticket_type_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/ticket_types/{ticket_type_id}/attributes/{id}",
            body=maybe_transform(
                {
                    "allow_multiple_values": allow_multiple_values,
                    "archived": archived,
                    "description": description,
                    "list_items": list_items,
                    "multiline": multiline,
                    "name": name,
                    "required_to_create": required_to_create,
                    "required_to_create_for_contacts": required_to_create_for_contacts,
                    "visible_on_create": visible_on_create,
                    "visible_to_contacts": visible_to_contacts,
                },
                attribute_update_params.AttributeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketTypeAttribute,
        )


class AsyncAttributesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttributesResourceWithRawResponse:
        return AsyncAttributesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttributesResourceWithStreamingResponse:
        return AsyncAttributesResourceWithStreamingResponse(self)

    async def create(
        self,
        ticket_type_id: str,
        *,
        data_type: Literal["string", "list", "integer", "decimal", "boolean", "datetime", "files"],
        description: str,
        name: str,
        allow_multiple_values: bool | NotGiven = NOT_GIVEN,
        list_items: str | NotGiven = NOT_GIVEN,
        multiline: bool | NotGiven = NOT_GIVEN,
        required_to_create: bool | NotGiven = NOT_GIVEN,
        required_to_create_for_contacts: bool | NotGiven = NOT_GIVEN,
        visible_on_create: bool | NotGiven = NOT_GIVEN,
        visible_to_contacts: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TicketTypeAttribute]:
        """
        You can create a new attribute for a ticket type.

        Args:
          data_type: The data type of the attribute

          description: The description of the attribute presented to the teammate or contact

          name: The name of the ticket type attribute

          allow_multiple_values: Whether the attribute allows multiple files to be attached to it (only
              applicable to file attributes)

          list_items: A comma delimited list of items for the attribute value (only applicable to list
              attributes)

          multiline: Whether the attribute allows multiple lines of text (only applicable to string
              attributes)

          required_to_create: Whether the attribute is required to be filled in when teammates are creating
              the ticket in Inbox.

          required_to_create_for_contacts: Whether the attribute is required to be filled in when contacts are creating the
              ticket in Messenger.

          visible_on_create: Whether the attribute is visible to teammates when creating a ticket in Inbox.

          visible_to_contacts: Whether the attribute is visible to contacts when creating a ticket in
              Messenger.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticket_type_id:
            raise ValueError(f"Expected a non-empty value for `ticket_type_id` but received {ticket_type_id!r}")
        return await self._post(
            f"/ticket_types/{ticket_type_id}/attributes",
            body=await async_maybe_transform(
                {
                    "data_type": data_type,
                    "description": description,
                    "name": name,
                    "allow_multiple_values": allow_multiple_values,
                    "list_items": list_items,
                    "multiline": multiline,
                    "required_to_create": required_to_create,
                    "required_to_create_for_contacts": required_to_create_for_contacts,
                    "visible_on_create": visible_on_create,
                    "visible_to_contacts": visible_to_contacts,
                },
                attribute_create_params.AttributeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketTypeAttribute,
        )

    async def update(
        self,
        id: str,
        *,
        ticket_type_id: str,
        allow_multiple_values: bool | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        list_items: str | NotGiven = NOT_GIVEN,
        multiline: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        required_to_create: bool | NotGiven = NOT_GIVEN,
        required_to_create_for_contacts: bool | NotGiven = NOT_GIVEN,
        visible_on_create: bool | NotGiven = NOT_GIVEN,
        visible_to_contacts: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TicketTypeAttribute]:
        """
        You can update an existing attribute for a ticket type.

        Args:
          allow_multiple_values: Whether the attribute allows multiple files to be attached to it (only
              applicable to file attributes)

          archived: Whether the attribute should be archived and not shown during creation of the
              ticket (it will still be present on previously created tickets)

          description: The description of the attribute presented to the teammate or contact

          list_items: A comma delimited list of items for the attribute value (only applicable to list
              attributes)

          multiline: Whether the attribute allows multiple lines of text (only applicable to string
              attributes)

          name: The name of the ticket type attribute

          required_to_create: Whether the attribute is required to be filled in when teammates are creating
              the ticket in Inbox.

          required_to_create_for_contacts: Whether the attribute is required to be filled in when contacts are creating the
              ticket in Messenger.

          visible_on_create: Whether the attribute is visible to teammates when creating a ticket in Inbox.

          visible_to_contacts: Whether the attribute is visible to contacts when creating a ticket in
              Messenger.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticket_type_id:
            raise ValueError(f"Expected a non-empty value for `ticket_type_id` but received {ticket_type_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/ticket_types/{ticket_type_id}/attributes/{id}",
            body=await async_maybe_transform(
                {
                    "allow_multiple_values": allow_multiple_values,
                    "archived": archived,
                    "description": description,
                    "list_items": list_items,
                    "multiline": multiline,
                    "name": name,
                    "required_to_create": required_to_create,
                    "required_to_create_for_contacts": required_to_create_for_contacts,
                    "visible_on_create": visible_on_create,
                    "visible_to_contacts": visible_to_contacts,
                },
                attribute_update_params.AttributeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketTypeAttribute,
        )


class AttributesResourceWithRawResponse:
    def __init__(self, attributes: AttributesResource) -> None:
        self._attributes = attributes

        self.create = to_raw_response_wrapper(
            attributes.create,
        )
        self.update = to_raw_response_wrapper(
            attributes.update,
        )


class AsyncAttributesResourceWithRawResponse:
    def __init__(self, attributes: AsyncAttributesResource) -> None:
        self._attributes = attributes

        self.create = async_to_raw_response_wrapper(
            attributes.create,
        )
        self.update = async_to_raw_response_wrapper(
            attributes.update,
        )


class AttributesResourceWithStreamingResponse:
    def __init__(self, attributes: AttributesResource) -> None:
        self._attributes = attributes

        self.create = to_streamed_response_wrapper(
            attributes.create,
        )
        self.update = to_streamed_response_wrapper(
            attributes.update,
        )


class AsyncAttributesResourceWithStreamingResponse:
    def __init__(self, attributes: AsyncAttributesResource) -> None:
        self._attributes = attributes

        self.create = async_to_streamed_response_wrapper(
            attributes.create,
        )
        self.update = async_to_streamed_response_wrapper(
            attributes.update,
        )
