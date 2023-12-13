# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional, overload
from typing_extensions import Literal

import httpx

from .tags import Tags, AsyncTags, TagsWithRawResponse, AsyncTagsWithRawResponse
from ...types import (
    TicketList,
    TicketReply,
    ticket_reply_params,
    ticket_create_params,
    ticket_search_params,
    ticket_update_by_id_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.shared import Ticket

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Tickets", "AsyncTickets"]


class Tickets(SyncAPIResource):
    tags: Tags
    with_raw_response: TicketsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.tags = Tags(client)
        self.with_raw_response = TicketsWithRawResponse(self)

    def create(
        self,
        *,
        contacts: List[ticket_create_params.Contact],
        ticket_type_id: str,
        ticket_attributes: Dict[str, Union[Optional[str], float, bool, List[object]]] | NotGiven = NOT_GIVEN,
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
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        intercom_user_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
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

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          email: The email you have defined for the user.

          intercom_user_id: The identifier for the contact as given by Intercom.

          user_id: The external_id you have defined for the contact.

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
        reply_options: List[ticket_reply_params.AdminReplyTicketRequestReplyOption] | NotGiven = NOT_GIVEN,
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

    @required_args(["body", "message_type", "type"], ["admin_id", "message_type", "type"])
    def reply(
        self,
        id: str,
        *,
        body: str | NotGiven = NOT_GIVEN,
        message_type: Literal["comment"] | Literal["comment", "note", "quick_reply"],
        type: Literal["user"] | Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        intercom_user_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        admin_id: str | NotGiven = NOT_GIVEN,
        reply_options: List[ticket_reply_params.AdminReplyTicketRequestReplyOption] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        return self._post(
            f"/tickets/{id}/reply",
            body=maybe_transform(
                {
                    "body": body,
                    "message_type": message_type,
                    "type": type,
                    "attachment_urls": attachment_urls,
                    "email": email,
                    "intercom_user_id": intercom_user_id,
                    "user_id": user_id,
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


class AsyncTickets(AsyncAPIResource):
    tags: AsyncTags
    with_raw_response: AsyncTicketsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.tags = AsyncTags(client)
        self.with_raw_response = AsyncTicketsWithRawResponse(self)

    async def create(
        self,
        *,
        contacts: List[ticket_create_params.Contact],
        ticket_type_id: str,
        ticket_attributes: Dict[str, Union[Optional[str], float, bool, List[object]]] | NotGiven = NOT_GIVEN,
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
    async def reply(
        self,
        id: str,
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        intercom_user_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
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

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          email: The email you have defined for the user.

          intercom_user_id: The identifier for the contact as given by Intercom.

          user_id: The external_id you have defined for the contact.

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
        reply_options: List[ticket_reply_params.AdminReplyTicketRequestReplyOption] | NotGiven = NOT_GIVEN,
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

    @required_args(["body", "message_type", "type"], ["admin_id", "message_type", "type"])
    async def reply(
        self,
        id: str,
        *,
        body: str | NotGiven = NOT_GIVEN,
        message_type: Literal["comment"] | Literal["comment", "note", "quick_reply"],
        type: Literal["user"] | Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        intercom_user_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        admin_id: str | NotGiven = NOT_GIVEN,
        reply_options: List[ticket_reply_params.AdminReplyTicketRequestReplyOption] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TicketReply:
        return await self._post(
            f"/tickets/{id}/reply",
            body=maybe_transform(
                {
                    "body": body,
                    "message_type": message_type,
                    "type": type,
                    "attachment_urls": attachment_urls,
                    "email": email,
                    "intercom_user_id": intercom_user_id,
                    "user_id": user_id,
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
        return await self._put(
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


class TicketsWithRawResponse:
    def __init__(self, tickets: Tickets) -> None:
        self.tags = TagsWithRawResponse(tickets.tags)

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


class AsyncTicketsWithRawResponse:
    def __init__(self, tickets: AsyncTickets) -> None:
        self.tags = AsyncTagsWithRawResponse(tickets.tags)

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
