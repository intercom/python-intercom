# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional, overload
from typing_extensions import Literal

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from ...types import (
    ticket_reply_params,
    ticket_create_params,
    ticket_search_params,
    ticket_update_by_id_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ...types.ticket_list import TicketList
from ...types.ticket_reply import TicketReply
from ...types.shared.ticket import Ticket

__all__ = ["TicketsResource", "AsyncTicketsResource"]


class TicketsResource(SyncAPIResource):
    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TicketsResourceWithRawResponse:
        return TicketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TicketsResourceWithStreamingResponse:
        return TicketsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        contacts: Iterable[ticket_create_params.Contact],
        ticket_type_id: str,
        ticket_attributes: Dict[str, Union[Optional[str], float, bool, Iterable[object]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Ticket]:
        """
        You can create a new ticket.

        Args:
          contacts: The list of contacts (users or leads) affected by this ticket. Currently only
              one is allowed

          ticket_type_id: The ID of the type of ticket you want to create

          ticket_attributes: The attributes set on the ticket. When setting the default title and description
              attributes, the attribute keys that should be used are `_default_title_` and
              `_default_description_`. When setting ticket type attributes of the list
              attribute type, the key should be the attribute name and the value of the
              attribute should be the list item id, obtainable by
              [listing the ticket type](ref:get_ticket-types). For example, if the ticket type
              has an attribute called `priority` of type `list`, the key should be `priority`
              and the value of the attribute should be the guid of the list item (e.g.
              `de1825a0-0164-4070-8ca6-13e22462fa7e`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tickets",
            body=maybe_transform(
                {
                    "contacts": contacts,
                    "ticket_type_id": ticket_type_id,
                    "ticket_attributes": ticket_attributes,
                },
                ticket_create_params.TicketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ticket,
        )

    @overload
    def reply(
        self,
        id: str,
        *,
        body: str,
        intercom_user_id: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        """
        You can reply to a ticket with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the ticket to target.

          body: The text body of the comment.

          intercom_user_id: The identifier for the contact as given by Intercom.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def reply(
        self,
        id: str,
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        user_id: str,
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        """
        You can reply to a ticket with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the ticket to target.

          body: The text body of the comment.

          user_id: The external_id you have defined for the contact.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def reply(
        self,
        id: str,
        *,
        body: str,
        email: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        """
        You can reply to a ticket with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the ticket to target.

          body: The text body of the comment.

          email: The email you have defined for the user.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def reply(
        self,
        id: str,
        *,
        admin_id: str,
        message_type: Literal["comment", "note", "quick_reply"],
        type: Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        reply_options: Iterable[ticket_reply_params.AdminReplyTicketRequestReplyOption] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        """
        You can reply to a ticket with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the ticket to target.

          admin_id: The id of the admin who is authoring the comment.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          body: The text body of the reply.\nNotes accept some HTML formatting. Must be present
              for comment and note message types.

          reply_options: The quick reply options to display. Must be present for quick_reply message
              types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["body", "intercom_user_id", "message_type", "type"],
        ["body", "message_type", "type", "user_id"],
        ["body", "email", "message_type", "type"],
        ["admin_id", "message_type", "type"],
    )
    def reply(
        self,
        id: str,
        *,
        body: str | NotGiven = NOT_GIVEN,
        intercom_user_id: str | NotGiven = NOT_GIVEN,
        message_type: Literal["comment"] | Literal["comment", "note", "quick_reply"],
        type: Literal["user"] | Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        admin_id: str | NotGiven = NOT_GIVEN,
        reply_options: Iterable[ticket_reply_params.AdminReplyTicketRequestReplyOption] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/tickets/{id}/reply",
            body=maybe_transform(
                {
                    "body": body,
                    "intercom_user_id": intercom_user_id,
                    "message_type": message_type,
                    "type": type,
                    "attachment_urls": attachment_urls,
                    "user_id": user_id,
                    "email": email,
                    "admin_id": admin_id,
                    "reply_options": reply_options,
                },
                ticket_reply_params.TicketReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketReply,
        )

    def retrieve_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Ticket]:
        """
        You can fetch the details of a single ticket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/tickets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ticket,
        )

    def search(
        self,
        *,
        query: ticket_search_params.Query,
        pagination: Optional[ticket_search_params.Pagination] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketList:
        """
        You can search for multiple tickets by the value of their attributes in order to
        fetch exactly which ones you want.

        To search for tickets, you send a POST request to
        https://api.intercom.io/tickets/search. This will accept a query object in the
        body which will define your filters.

        > 🚧 Nesting & Limitations
        >
        > You can nest these filters in order to get even more granular insights that
        > pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4). There are some
        > limitations to the amount of multiples there can be:
        >
        > - There's a limit of max 2 nested filters
        > - There's a limit of max 15 filters for each AND or OR group

        ### Accepted Fields

        Most keys listed as part of the Ticket model are searchable, whether writeable
        or not. The value you search for has to match the accepted type, otherwise the
        query will fail (ie. as `created_at` accepts a date, the `value` cannot be a
        string such as `"foobar"`).

        | Field                 | Type                                                           |
        | :-------------------- | :------------------------------------------------------------- |
        | id                    | String                                                         |
        | created_at            | Date (UNIX timestamp)                                          |
        | updated_at            | Date (UNIX timestamp)                                          |
        | title                 | String                                                         |
        | description           | String                                                         |
        | category              | String                                                         |
        | ticket_type_id        | String                                                         |
        | contact_ids           | String                                                         |
        | teammate_ids          | String                                                         |
        | admin_assignee_id     | String                                                         |
        | team_assignee_id      | String                                                         |
        | open                  | Boolean                                                        |
        | state                 | String                                                         |
        | snoozed_until         | Date (UNIX timestamp)                                          |
        | ticket_attribute.{id} | String or Boolean or Date (UNIX timestamp) or Float or Integer |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tickets/search",
            body=maybe_transform(
                {
                    "query": query,
                    "pagination": pagination,
                },
                ticket_search_params.TicketSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketList,
        )

    def update_by_id(
        self,
        id: str,
        *,
        assignment: ticket_update_by_id_params.Assignment | NotGiven = NOT_GIVEN,
        is_shared: bool | NotGiven = NOT_GIVEN,
        open: bool | NotGiven = NOT_GIVEN,
        snoozed_until: int | NotGiven = NOT_GIVEN,
        state: Literal["in_progress", "waiting_on_customer", "resolved"] | NotGiven = NOT_GIVEN,
        ticket_attributes: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Ticket]:
        """
        You can update a ticket.

        Args:
          is_shared: Specify whether the ticket is visible to users.

          open: Specify if a ticket is open. Set to false to close a ticket. Closing a ticket
              will also unsnooze it.

          snoozed_until: The time you want the ticket to reopen.

          state: The state of the ticket.

          ticket_attributes: The attributes set on the ticket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/tickets/{id}",
            body=maybe_transform(
                {
                    "assignment": assignment,
                    "is_shared": is_shared,
                    "open": open,
                    "snoozed_until": snoozed_until,
                    "state": state,
                    "ticket_attributes": ticket_attributes,
                },
                ticket_update_by_id_params.TicketUpdateByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ticket,
        )


class AsyncTicketsResource(AsyncAPIResource):
    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTicketsResourceWithRawResponse:
        return AsyncTicketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTicketsResourceWithStreamingResponse:
        return AsyncTicketsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        contacts: Iterable[ticket_create_params.Contact],
        ticket_type_id: str,
        ticket_attributes: Dict[str, Union[Optional[str], float, bool, Iterable[object]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Ticket]:
        """
        You can create a new ticket.

        Args:
          contacts: The list of contacts (users or leads) affected by this ticket. Currently only
              one is allowed

          ticket_type_id: The ID of the type of ticket you want to create

          ticket_attributes: The attributes set on the ticket. When setting the default title and description
              attributes, the attribute keys that should be used are `_default_title_` and
              `_default_description_`. When setting ticket type attributes of the list
              attribute type, the key should be the attribute name and the value of the
              attribute should be the list item id, obtainable by
              [listing the ticket type](ref:get_ticket-types). For example, if the ticket type
              has an attribute called `priority` of type `list`, the key should be `priority`
              and the value of the attribute should be the guid of the list item (e.g.
              `de1825a0-0164-4070-8ca6-13e22462fa7e`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tickets",
            body=await async_maybe_transform(
                {
                    "contacts": contacts,
                    "ticket_type_id": ticket_type_id,
                    "ticket_attributes": ticket_attributes,
                },
                ticket_create_params.TicketCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ticket,
        )

    @overload
    async def reply(
        self,
        id: str,
        *,
        body: str,
        intercom_user_id: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        """
        You can reply to a ticket with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the ticket to target.

          body: The text body of the comment.

          intercom_user_id: The identifier for the contact as given by Intercom.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def reply(
        self,
        id: str,
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        user_id: str,
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        """
        You can reply to a ticket with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the ticket to target.

          body: The text body of the comment.

          user_id: The external_id you have defined for the contact.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def reply(
        self,
        id: str,
        *,
        body: str,
        email: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        """
        You can reply to a ticket with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the ticket to target.

          body: The text body of the comment.

          email: The email you have defined for the user.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def reply(
        self,
        id: str,
        *,
        admin_id: str,
        message_type: Literal["comment", "note", "quick_reply"],
        type: Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        reply_options: Iterable[ticket_reply_params.AdminReplyTicketRequestReplyOption] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        """
        You can reply to a ticket with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the ticket to target.

          admin_id: The id of the admin who is authoring the comment.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          body: The text body of the reply.\nNotes accept some HTML formatting. Must be present
              for comment and note message types.

          reply_options: The quick reply options to display. Must be present for quick_reply message
              types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["body", "intercom_user_id", "message_type", "type"],
        ["body", "message_type", "type", "user_id"],
        ["body", "email", "message_type", "type"],
        ["admin_id", "message_type", "type"],
    )
    async def reply(
        self,
        id: str,
        *,
        body: str | NotGiven = NOT_GIVEN,
        intercom_user_id: str | NotGiven = NOT_GIVEN,
        message_type: Literal["comment"] | Literal["comment", "note", "quick_reply"],
        type: Literal["user"] | Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        admin_id: str | NotGiven = NOT_GIVEN,
        reply_options: Iterable[ticket_reply_params.AdminReplyTicketRequestReplyOption] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/tickets/{id}/reply",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "intercom_user_id": intercom_user_id,
                    "message_type": message_type,
                    "type": type,
                    "attachment_urls": attachment_urls,
                    "user_id": user_id,
                    "email": email,
                    "admin_id": admin_id,
                    "reply_options": reply_options,
                },
                ticket_reply_params.TicketReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketReply,
        )

    async def retrieve_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Ticket]:
        """
        You can fetch the details of a single ticket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/tickets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ticket,
        )

    async def search(
        self,
        *,
        query: ticket_search_params.Query,
        pagination: Optional[ticket_search_params.Pagination] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketList:
        """
        You can search for multiple tickets by the value of their attributes in order to
        fetch exactly which ones you want.

        To search for tickets, you send a POST request to
        https://api.intercom.io/tickets/search. This will accept a query object in the
        body which will define your filters.

        > 🚧 Nesting & Limitations
        >
        > You can nest these filters in order to get even more granular insights that
        > pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4). There are some
        > limitations to the amount of multiples there can be:
        >
        > - There's a limit of max 2 nested filters
        > - There's a limit of max 15 filters for each AND or OR group

        ### Accepted Fields

        Most keys listed as part of the Ticket model are searchable, whether writeable
        or not. The value you search for has to match the accepted type, otherwise the
        query will fail (ie. as `created_at` accepts a date, the `value` cannot be a
        string such as `"foobar"`).

        | Field                 | Type                                                           |
        | :-------------------- | :------------------------------------------------------------- |
        | id                    | String                                                         |
        | created_at            | Date (UNIX timestamp)                                          |
        | updated_at            | Date (UNIX timestamp)                                          |
        | title                 | String                                                         |
        | description           | String                                                         |
        | category              | String                                                         |
        | ticket_type_id        | String                                                         |
        | contact_ids           | String                                                         |
        | teammate_ids          | String                                                         |
        | admin_assignee_id     | String                                                         |
        | team_assignee_id      | String                                                         |
        | open                  | Boolean                                                        |
        | state                 | String                                                         |
        | snoozed_until         | Date (UNIX timestamp)                                          |
        | ticket_attribute.{id} | String or Boolean or Date (UNIX timestamp) or Float or Integer |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tickets/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "pagination": pagination,
                },
                ticket_search_params.TicketSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketList,
        )

    async def update_by_id(
        self,
        id: str,
        *,
        assignment: ticket_update_by_id_params.Assignment | NotGiven = NOT_GIVEN,
        is_shared: bool | NotGiven = NOT_GIVEN,
        open: bool | NotGiven = NOT_GIVEN,
        snoozed_until: int | NotGiven = NOT_GIVEN,
        state: Literal["in_progress", "waiting_on_customer", "resolved"] | NotGiven = NOT_GIVEN,
        ticket_attributes: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Ticket]:
        """
        You can update a ticket.

        Args:
          is_shared: Specify whether the ticket is visible to users.

          open: Specify if a ticket is open. Set to false to close a ticket. Closing a ticket
              will also unsnooze it.

          snoozed_until: The time you want the ticket to reopen.

          state: The state of the ticket.

          ticket_attributes: The attributes set on the ticket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/tickets/{id}",
            body=await async_maybe_transform(
                {
                    "assignment": assignment,
                    "is_shared": is_shared,
                    "open": open,
                    "snoozed_until": snoozed_until,
                    "state": state,
                    "ticket_attributes": ticket_attributes,
                },
                ticket_update_by_id_params.TicketUpdateByIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ticket,
        )


class TicketsResourceWithRawResponse:
    def __init__(self, tickets: TicketsResource) -> None:
        self._tickets = tickets

        self.create = to_raw_response_wrapper(
            tickets.create,
        )
        self.reply = to_raw_response_wrapper(
            tickets.reply,
        )
        self.retrieve_by_id = to_raw_response_wrapper(
            tickets.retrieve_by_id,
        )
        self.search = to_raw_response_wrapper(
            tickets.search,
        )
        self.update_by_id = to_raw_response_wrapper(
            tickets.update_by_id,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._tickets.tags)


class AsyncTicketsResourceWithRawResponse:
    def __init__(self, tickets: AsyncTicketsResource) -> None:
        self._tickets = tickets

        self.create = async_to_raw_response_wrapper(
            tickets.create,
        )
        self.reply = async_to_raw_response_wrapper(
            tickets.reply,
        )
        self.retrieve_by_id = async_to_raw_response_wrapper(
            tickets.retrieve_by_id,
        )
        self.search = async_to_raw_response_wrapper(
            tickets.search,
        )
        self.update_by_id = async_to_raw_response_wrapper(
            tickets.update_by_id,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._tickets.tags)


class TicketsResourceWithStreamingResponse:
    def __init__(self, tickets: TicketsResource) -> None:
        self._tickets = tickets

        self.create = to_streamed_response_wrapper(
            tickets.create,
        )
        self.reply = to_streamed_response_wrapper(
            tickets.reply,
        )
        self.retrieve_by_id = to_streamed_response_wrapper(
            tickets.retrieve_by_id,
        )
        self.search = to_streamed_response_wrapper(
            tickets.search,
        )
        self.update_by_id = to_streamed_response_wrapper(
            tickets.update_by_id,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._tickets.tags)


class AsyncTicketsResourceWithStreamingResponse:
    def __init__(self, tickets: AsyncTicketsResource) -> None:
        self._tickets = tickets

        self.create = async_to_streamed_response_wrapper(
            tickets.create,
        )
        self.reply = async_to_streamed_response_wrapper(
            tickets.reply,
        )
        self.retrieve_by_id = async_to_streamed_response_wrapper(
            tickets.retrieve_by_id,
        )
        self.search = async_to_streamed_response_wrapper(
            tickets.search,
        )
        self.update_by_id = async_to_streamed_response_wrapper(
            tickets.update_by_id,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._tickets.tags)
