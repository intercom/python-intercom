# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional, overload
from typing_extensions import Literal

import httpx

from .tags import Tags, AsyncTags, TagsWithRawResponse, AsyncTagsWithRawResponse
from .parts import Parts, AsyncParts, PartsWithRawResponse, AsyncPartsWithRawResponse
from .reply import Reply, AsyncReply, ReplyWithRawResponse, AsyncReplyWithRawResponse
from .search import (
    Search,
    AsyncSearch,
    SearchWithRawResponse,
    AsyncSearchWithRawResponse,
)
from ...types import (
    ConversationDeleted,
    conversation_list_params,
    conversation_create_params,
    conversation_redact_params,
    conversation_update_params,
    conversation_convert_params,
    conversation_retrieve_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform
from .customers import (
    Customers,
    AsyncCustomers,
    CustomersWithRawResponse,
    AsyncCustomersWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.shared import Ticket, Message, Conversation, PaginatedResponse
from .run_assignment_rules import (
    RunAssignmentRules,
    AsyncRunAssignmentRules,
    RunAssignmentRulesWithRawResponse,
    AsyncRunAssignmentRulesWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Conversations", "AsyncConversations"]


class Conversations(SyncAPIResource):
    tags: Tags
    search: Search
    reply: Reply
    parts: Parts
    run_assignment_rules: RunAssignmentRules
    customers: Customers
    with_raw_response: ConversationsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.tags = Tags(client)
        self.search = Search(client)
        self.reply = Reply(client)
        self.parts = Parts(client)
        self.run_assignment_rules = RunAssignmentRules(client)
        self.customers = Customers(client)
        self.with_raw_response = ConversationsWithRawResponse(self)

    def create(
        self,
        *,
        body: str,
        from_: conversation_create_params.From,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """You can create a conversation that has been initiated by a contact (ie.

        user or
        lead). The conversation can be an in-app message only.

        > 📘 Sending for visitors
        >
        > You can also send a message from a visitor by specifying their `user_id` or
        > `id` value in the `from` field, along with a `type` field value of `contact`.
        > This visitor will be automatically converted to a contact with a lead role
        > once the conversation is created.

        This will return the Message model that has been created.

        Args:
          body: The content of the message. HTML is not supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/conversations",
            body=maybe_transform(
                {
                    "body": body,
                    "from_": from_,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def retrieve(
        self,
        id: int,
        *,
        display_as: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can fetch the details of a single conversation.

        This will return a single Conversation model with all its conversation parts.

        > 🚧 Hard limit of 500 parts
        >
        > The maximum number of conversation parts that can be returned via the API
        > is 500. If you have more than that we will return the 500 most recent
        > conversation parts.

        > 📘 Bot name in conversation parts
        >
        > For conversation parts generated by a bot, bot name will depend on the
        > following:

        - Customers that never turned on AI answers will have `operator` as the bot name
        - Customers that have turned on AI answers at some point will have `fin` as the
          bot name

        Args:
          display_as: Set to plaintext to retrieve conversation messages in plain text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/conversations/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"display_as": display_as}, conversation_retrieve_params.ConversationRetrieveParams
                ),
            ),
            cast_to=Conversation,
        )

    def update(
        self,
        id: int,
        *,
        display_as: str | NotGiven = NOT_GIVEN,
        custom_attributes: Dict[str, conversation_update_params.CustomAttributes] | NotGiven = NOT_GIVEN,
        read: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can update an existing conversation.

        > 📘
        >
        > If you want to update a conversation with either a reply (or actions such as
        > assign, unassign, open, close or snooze) then take a look at their own
        > sections respectively as they currently require different endpoints and
        > parameters.

        Args:
          display_as: Set to plaintext to retrieve conversation messages in plain text.

          custom_attributes: An object containing the different custom attributes associated to the
              conversation as key-value pairs. For relationship attributes the value will be a
              list of custom object instance models.

          read: Mark a conversation as read within Intercom.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/conversations/{id}",
            body=maybe_transform(
                {
                    "custom_attributes": custom_attributes,
                    "read": read,
                },
                conversation_update_params.ConversationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"display_as": display_as}, conversation_update_params.ConversationUpdateParams),
            ),
            cast_to=Conversation,
        )

    def list(
        self,
        *,
        per_page: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponse:
        """
        You can fetch a list of all conversations.

        You can optionally request the result page size and the cursor to start after to
        fetch the result

        Args:
          per_page: How many results per page

          starting_after: String used to get the next page of conversations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/conversations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "per_page": per_page,
                        "starting_after": starting_after,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=PaginatedResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationDeleted:
        """
        You can delete a single conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/conversations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationDeleted,
        )

    def convert(
        self,
        id: int,
        *,
        ticket_type_id: str,
        attributes: Dict[str, Union[Optional[str], float, bool, List[object]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Ticket]:
        """
        You can convert a conversation to a ticket.

        Args:
          ticket_type_id: The ID of the type of ticket you want to convert the conversation to

          attributes: The attributes set on the ticket. When setting the default title and description
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
            f"/conversations/{id}/convert",
            body=maybe_transform(
                {
                    "ticket_type_id": ticket_type_id,
                    "attributes": attributes,
                },
                conversation_convert_params.ConversationConvertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ticket,
        )

    @overload
    def redact(
        self,
        *,
        conversation_id: str,
        conversation_part_id: str,
        type: Literal["conversation_part"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can redact a conversation part or the source message of a conversation (as
        seen in the source object).

        > 📘 Which parts and source messages can I redact?
        >
        > If you are redacting a conversation part, it must have a `body`. If you are
        > redacting a source message, it must have been created by a contact. We will
        > return a `conversation_part_not_redactable` error if these criteria are not
        > met.

        Args:
          conversation_id: The id of the conversation.

          conversation_part_id: The id of the conversation_part.

          type: The type of resource being redacted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def redact(
        self,
        *,
        conversation_id: str,
        source_id: str,
        type: Literal["source"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can redact a conversation part or the source message of a conversation (as
        seen in the source object).

        > 📘 Which parts and source messages can I redact?
        >
        > If you are redacting a conversation part, it must have a `body`. If you are
        > redacting a source message, it must have been created by a contact. We will
        > return a `conversation_part_not_redactable` error if these criteria are not
        > met.

        Args:
          conversation_id: The id of the conversation.

          source_id: The id of the source.

          type: The type of resource being redacted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["conversation_id", "conversation_part_id", "type"], ["conversation_id", "source_id", "type"])
    def redact(
        self,
        *,
        conversation_id: str,
        conversation_part_id: str | NotGiven = NOT_GIVEN,
        type: Literal["conversation_part"] | Literal["source"],
        source_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        return self._post(
            "/conversations/redact",
            body=maybe_transform(
                {
                    "conversation_id": conversation_id,
                    "conversation_part_id": conversation_part_id,
                    "type": type,
                    "source_id": source_id,
                },
                conversation_redact_params.ConversationRedactParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class AsyncConversations(AsyncAPIResource):
    tags: AsyncTags
    search: AsyncSearch
    reply: AsyncReply
    parts: AsyncParts
    run_assignment_rules: AsyncRunAssignmentRules
    customers: AsyncCustomers
    with_raw_response: AsyncConversationsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.tags = AsyncTags(client)
        self.search = AsyncSearch(client)
        self.reply = AsyncReply(client)
        self.parts = AsyncParts(client)
        self.run_assignment_rules = AsyncRunAssignmentRules(client)
        self.customers = AsyncCustomers(client)
        self.with_raw_response = AsyncConversationsWithRawResponse(self)

    async def create(
        self,
        *,
        body: str,
        from_: conversation_create_params.From,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """You can create a conversation that has been initiated by a contact (ie.

        user or
        lead). The conversation can be an in-app message only.

        > 📘 Sending for visitors
        >
        > You can also send a message from a visitor by specifying their `user_id` or
        > `id` value in the `from` field, along with a `type` field value of `contact`.
        > This visitor will be automatically converted to a contact with a lead role
        > once the conversation is created.

        This will return the Message model that has been created.

        Args:
          body: The content of the message. HTML is not supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/conversations",
            body=maybe_transform(
                {
                    "body": body,
                    "from_": from_,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def retrieve(
        self,
        id: int,
        *,
        display_as: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can fetch the details of a single conversation.

        This will return a single Conversation model with all its conversation parts.

        > 🚧 Hard limit of 500 parts
        >
        > The maximum number of conversation parts that can be returned via the API
        > is 500. If you have more than that we will return the 500 most recent
        > conversation parts.

        > 📘 Bot name in conversation parts
        >
        > For conversation parts generated by a bot, bot name will depend on the
        > following:

        - Customers that never turned on AI answers will have `operator` as the bot name
        - Customers that have turned on AI answers at some point will have `fin` as the
          bot name

        Args:
          display_as: Set to plaintext to retrieve conversation messages in plain text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/conversations/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"display_as": display_as}, conversation_retrieve_params.ConversationRetrieveParams
                ),
            ),
            cast_to=Conversation,
        )

    async def update(
        self,
        id: int,
        *,
        display_as: str | NotGiven = NOT_GIVEN,
        custom_attributes: Dict[str, conversation_update_params.CustomAttributes] | NotGiven = NOT_GIVEN,
        read: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can update an existing conversation.

        > 📘
        >
        > If you want to update a conversation with either a reply (or actions such as
        > assign, unassign, open, close or snooze) then take a look at their own
        > sections respectively as they currently require different endpoints and
        > parameters.

        Args:
          display_as: Set to plaintext to retrieve conversation messages in plain text.

          custom_attributes: An object containing the different custom attributes associated to the
              conversation as key-value pairs. For relationship attributes the value will be a
              list of custom object instance models.

          read: Mark a conversation as read within Intercom.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/conversations/{id}",
            body=maybe_transform(
                {
                    "custom_attributes": custom_attributes,
                    "read": read,
                },
                conversation_update_params.ConversationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"display_as": display_as}, conversation_update_params.ConversationUpdateParams),
            ),
            cast_to=Conversation,
        )

    async def list(
        self,
        *,
        per_page: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponse:
        """
        You can fetch a list of all conversations.

        You can optionally request the result page size and the cursor to start after to
        fetch the result

        Args:
          per_page: How many results per page

          starting_after: String used to get the next page of conversations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/conversations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "per_page": per_page,
                        "starting_after": starting_after,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=PaginatedResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationDeleted:
        """
        You can delete a single conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/conversations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationDeleted,
        )

    async def convert(
        self,
        id: int,
        *,
        ticket_type_id: str,
        attributes: Dict[str, Union[Optional[str], float, bool, List[object]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Ticket]:
        """
        You can convert a conversation to a ticket.

        Args:
          ticket_type_id: The ID of the type of ticket you want to convert the conversation to

          attributes: The attributes set on the ticket. When setting the default title and description
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
            f"/conversations/{id}/convert",
            body=maybe_transform(
                {
                    "ticket_type_id": ticket_type_id,
                    "attributes": attributes,
                },
                conversation_convert_params.ConversationConvertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Ticket,
        )

    @overload
    async def redact(
        self,
        *,
        conversation_id: str,
        conversation_part_id: str,
        type: Literal["conversation_part"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can redact a conversation part or the source message of a conversation (as
        seen in the source object).

        > 📘 Which parts and source messages can I redact?
        >
        > If you are redacting a conversation part, it must have a `body`. If you are
        > redacting a source message, it must have been created by a contact. We will
        > return a `conversation_part_not_redactable` error if these criteria are not
        > met.

        Args:
          conversation_id: The id of the conversation.

          conversation_part_id: The id of the conversation_part.

          type: The type of resource being redacted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def redact(
        self,
        *,
        conversation_id: str,
        source_id: str,
        type: Literal["source"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can redact a conversation part or the source message of a conversation (as
        seen in the source object).

        > 📘 Which parts and source messages can I redact?
        >
        > If you are redacting a conversation part, it must have a `body`. If you are
        > redacting a source message, it must have been created by a contact. We will
        > return a `conversation_part_not_redactable` error if these criteria are not
        > met.

        Args:
          conversation_id: The id of the conversation.

          source_id: The id of the source.

          type: The type of resource being redacted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["conversation_id", "conversation_part_id", "type"], ["conversation_id", "source_id", "type"])
    async def redact(
        self,
        *,
        conversation_id: str,
        conversation_part_id: str | NotGiven = NOT_GIVEN,
        type: Literal["conversation_part"] | Literal["source"],
        source_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        return await self._post(
            "/conversations/redact",
            body=maybe_transform(
                {
                    "conversation_id": conversation_id,
                    "conversation_part_id": conversation_part_id,
                    "type": type,
                    "source_id": source_id,
                },
                conversation_redact_params.ConversationRedactParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class ConversationsWithRawResponse:
    def __init__(self, conversations: Conversations) -> None:
        self.tags = TagsWithRawResponse(conversations.tags)
        self.search = SearchWithRawResponse(conversations.search)
        self.reply = ReplyWithRawResponse(conversations.reply)
        self.parts = PartsWithRawResponse(conversations.parts)
        self.run_assignment_rules = RunAssignmentRulesWithRawResponse(conversations.run_assignment_rules)
        self.customers = CustomersWithRawResponse(conversations.customers)

        self.create = to_raw_response_wrapper(
            conversations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            conversations.update,
        )
        self.list = to_raw_response_wrapper(
            conversations.list,
        )
        self.delete = to_raw_response_wrapper(
            conversations.delete,
        )
        self.convert = to_raw_response_wrapper(
            conversations.convert,
        )
        self.redact = to_raw_response_wrapper(
            conversations.redact,
        )


class AsyncConversationsWithRawResponse:
    def __init__(self, conversations: AsyncConversations) -> None:
        self.tags = AsyncTagsWithRawResponse(conversations.tags)
        self.search = AsyncSearchWithRawResponse(conversations.search)
        self.reply = AsyncReplyWithRawResponse(conversations.reply)
        self.parts = AsyncPartsWithRawResponse(conversations.parts)
        self.run_assignment_rules = AsyncRunAssignmentRulesWithRawResponse(conversations.run_assignment_rules)
        self.customers = AsyncCustomersWithRawResponse(conversations.customers)

        self.create = async_to_raw_response_wrapper(
            conversations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            conversations.update,
        )
        self.list = async_to_raw_response_wrapper(
            conversations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            conversations.delete,
        )
        self.convert = async_to_raw_response_wrapper(
            conversations.convert,
        )
        self.redact = async_to_raw_response_wrapper(
            conversations.redact,
        )
