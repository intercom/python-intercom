# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional, overload
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
from .parts import (
    PartsResource,
    AsyncPartsResource,
    PartsResourceWithRawResponse,
    AsyncPartsResourceWithRawResponse,
    PartsResourceWithStreamingResponse,
    AsyncPartsResourceWithStreamingResponse,
)
from .reply import (
    ReplyResource,
    AsyncReplyResource,
    ReplyResourceWithRawResponse,
    AsyncReplyResourceWithRawResponse,
    ReplyResourceWithStreamingResponse,
    AsyncReplyResourceWithStreamingResponse,
)
from ...types import (
    conversation_list_params,
    conversation_create_params,
    conversation_redact_params,
    conversation_search_params,
    conversation_update_params,
    conversation_convert_params,
    conversation_retrieve_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from .customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
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
from .run_assignment_rules import (
    RunAssignmentRulesResource,
    AsyncRunAssignmentRulesResource,
    RunAssignmentRulesResourceWithRawResponse,
    AsyncRunAssignmentRulesResourceWithRawResponse,
    RunAssignmentRulesResourceWithStreamingResponse,
    AsyncRunAssignmentRulesResourceWithStreamingResponse,
)
from ...types.shared.ticket import Ticket
from ...types.shared.message import Message
from ...types.conversation_list import ConversationList
from ...types.shared.conversation import Conversation
from ...types.shared.paginated_response import PaginatedResponse

__all__ = ["ConversationsResource", "AsyncConversationsResource"]


class ConversationsResource(SyncAPIResource):
    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def reply(self) -> ReplyResource:
        return ReplyResource(self._client)

    @cached_property
    def parts(self) -> PartsResource:
        return PartsResource(self._client)

    @cached_property
    def run_assignment_rules(self) -> RunAssignmentRulesResource:
        return RunAssignmentRulesResource(self._client)

    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        return ConversationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: str,
        from_: conversation_create_params.From,
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
    ) -> Message:
        """You can create a conversation that has been initiated by a contact (ie.

        user or
        lead). The conversation can be an in-app message only.

        {% admonition type="info" name="Sending for visitors" %} You can also send a
        message from a visitor by specifying their `user_id` or `id` value in the `from`
        field, along with a `type` field value of `contact`. This visitor will be
        automatically converted to a contact with a lead role once the conversation is
        created. {% /admonition %}

        This will return the Message model that has been created.

        Args:
          body: The content of the message. HTML is not supported.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
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
    ) -> Conversation:
        """
        You can fetch the details of a single conversation.

        This will return a single Conversation model with all its conversation parts.

        {% admonition type="warning" name="Hard limit of 500 parts" %} The maximum
        number of conversation parts that can be returned via the API is 500. If you
        have more than that we will return the 500 most recent conversation parts.
        {% /admonition %}

        For AI agent conversation metadata, please note that you need to have the agent
        enabled in your workspace, which is a
        [paid feature](https://www.intercom.com/help/en/articles/8205718-fin-resolutions#h_97f8c2e671).

        Args:
          display_as: Set to plaintext to retrieve conversation messages in plain text.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
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
    ) -> Conversation:
        """
        You can update an existing conversation.

        {% admonition type="info" name="Replying and other actions" %} If you want to
        reply to a coveration or take an action such as assign, unassign, open, close or
        snooze, take a look at the reply and manage endpoints. {% /admonition %}

        Args:
          display_as: Set to plaintext to retrieve conversation messages in plain text.

          custom_attributes: An object containing the different custom attributes associated to the
              conversation as key-value pairs. For relationship attributes the value will be a
              list of custom object instance models.

          read: Mark a conversation as read within Intercom.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
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
    ) -> PaginatedResponse:
        """
        You can fetch a list of all conversations.

        You can optionally request the result page size and the cursor to start after to
        fetch the result. {% admonition type="warning" name="Pagination" %} You can use
        pagination to limit the number of results returned. The default is `20` results
        per page. See the
        [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis)
        for more details on how to use the `starting_after` param. {% /admonition %}

        Args:
          per_page: How many results per page

          starting_after: String used to get the next page of conversations.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
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

    def convert(
        self,
        id: int,
        *,
        ticket_type_id: str,
        attributes: Dict[str, Union[Optional[str], float, bool, Iterable[object]]] | NotGiven = NOT_GIVEN,
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

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
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
    ) -> Conversation:
        """
        You can redact a conversation part or the source message of a conversation (as
        seen in the source object).

        {% admonition type="info" name="Redacting parts and messages" %} If you are
        redacting a conversation part, it must have a `body`. If you are redacting a
        source message, it must have been created by a contact. We will return a
        `conversation_part_not_redactable` error if these criteria are not met.
        {% /admonition %}

        Args:
          conversation_id: The id of the conversation.

          conversation_part_id: The id of the conversation_part.

          type: The type of resource being redacted.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

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
    ) -> Conversation:
        """
        You can redact a conversation part or the source message of a conversation (as
        seen in the source object).

        {% admonition type="info" name="Redacting parts and messages" %} If you are
        redacting a conversation part, it must have a `body`. If you are redacting a
        source message, it must have been created by a contact. We will return a
        `conversation_part_not_redactable` error if these criteria are not met.
        {% /admonition %}

        Args:
          conversation_id: The id of the conversation.

          source_id: The id of the source.

          type: The type of resource being redacted.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

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
        source_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
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

    def search(
        self,
        *,
        query: conversation_search_params.Query,
        pagination: Optional[conversation_search_params.Pagination] | NotGiven = NOT_GIVEN,
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
    ) -> ConversationList:
        """
        You can search for multiple conversations by the value of their attributes in
        order to fetch exactly which ones you want.

        To search for conversations, you need to send a `POST` request to
        `https://api.intercom.io/conversations/search`.

        This will accept a query object in the body which will define your filters in
        order to search for conversations.
        {% admonition type="warning" name="Optimizing search queries" %} Search queries
        can be complex, so optimizing them can help the performance of your search. Use
        the `AND` and `OR` operators to combine multiple filters to get the exact
        results you need and utilize pagination to limit the number of results returned.
        The default is `20` results per page and maximum is `150`. See the
        [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#example-search-conversations-request)
        for more details on how to use the `starting_after` param. {% /admonition %}

        ### Nesting & Limitations

        You can nest these filters in order to get even more granular insights that
        pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4). There are some
        limitations to the amount of multiple's there can be:

        - There's a limit of max 2 nested filters
        - There's a limit of max 15 filters for each AND or OR group

        ### Accepted Fields

        Most keys listed as part of the The conversation model is searchable, whether
        writeable or not. The value you search for has to match the accepted type,
        otherwise the query will fail (ie. as `created_at` accepts a date, the `value`
        cannot be a string such as `"foorbar"`).

        | Field                                                                                                                                        | Type                  |
        | :------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------- |
        | id                                                                                                                                           | String                |
        | created_at                                                                                                                                   | Date (UNIX timestamp) |
        | updated_at                                                                                                                                   | Date (UNIX timestamp) |
        | source.type                                                                                                                                  | String                |
        | Accepted fields are `conversation`, `email`, `facebook`, `instagram`, `phone_call`, `phone_switch`, `push`, `sms`, `twitter` and `whatsapp`. |
        | source.id                                                                                                                                    | String                |
        | source.delivered_as                                                                                                                          | String                |
        | source.subject                                                                                                                               | String                |
        | source.body                                                                                                                                  | String                |
        | source.author.id                                                                                                                             | String                |
        | source.author.type                                                                                                                           | String                |
        | source.author.name                                                                                                                           | String                |
        | source.author.email                                                                                                                          | String                |
        | source.url                                                                                                                                   | String                |
        | contact_ids                                                                                                                                  | String                |
        | teammate_ids                                                                                                                                 | String                |
        | admin_assignee_id                                                                                                                            | String                |
        | team_assignee_id                                                                                                                             | String                |
        | channel_initiated                                                                                                                            | String                |
        | open                                                                                                                                         | Boolean               |
        | read                                                                                                                                         | Boolean               |
        | state                                                                                                                                        | String                |
        | waiting_since                                                                                                                                | Date (UNIX timestamp) |
        | snoozed_until                                                                                                                                | Date (UNIX timestamp) |
        | tag_ids                                                                                                                                      | String                |
        | priority                                                                                                                                     | String                |
        | statistics.time_to_assignment                                                                                                                | Integer               |
        | statistics.time_to_admin_reply                                                                                                               | Integer               |
        | statistics.time_to_first_close                                                                                                               | Integer               |
        | statistics.time_to_last_close                                                                                                                | Integer               |
        | statistics.median_time_to_reply                                                                                                              | Integer               |
        | statistics.first_contact_reply_at                                                                                                            | Date (UNIX timestamp) |
        | statistics.first_assignment_at                                                                                                               | Date (UNIX timestamp) |
        | statistics.first_admin_reply_at                                                                                                              | Date (UNIX timestamp) |
        | statistics.first_close_at                                                                                                                    | Date (UNIX timestamp) |
        | statistics.last_assignment_at                                                                                                                | Date (UNIX timestamp) |
        | statistics.last_assignment_admin_reply_at                                                                                                    | Date (UNIX timestamp) |
        | statistics.last_contact_reply_at                                                                                                             | Date (UNIX timestamp) |
        | statistics.last_admin_reply_at                                                                                                               | Date (UNIX timestamp) |
        | statistics.last_close_at                                                                                                                     | Date (UNIX timestamp) |
        | statistics.last_closed_by_id                                                                                                                 | String                |
        | statistics.count_reopens                                                                                                                     | Integer               |
        | statistics.count_assignments                                                                                                                 | Integer               |
        | statistics.count_conversation_parts                                                                                                          | Integer               |
        | conversation_rating.requested_at                                                                                                             | Date (UNIX timestamp) |
        | conversation_rating.replied_at                                                                                                               | Date (UNIX timestamp) |
        | conversation_rating.score                                                                                                                    | Integer               |
        | conversation_rating.remark                                                                                                                   | String                |
        | conversation_rating.contact_id                                                                                                               | String                |
        | conversation_rating.admin_d                                                                                                                  | String                |
        | ai_agent_participated                                                                                                                        | Boolean               |
        | ai_agent.resolution_state                                                                                                                    | String                |
        | ai_agent.last_answer_type                                                                                                                    | String                |
        | ai_agent.rating                                                                                                                              | Integer               |
        | ai_agent.rating_remark                                                                                                                       | String                |
        | ai_agent.source_type                                                                                                                         | String                |
        | ai_agent.source_title                                                                                                                        | String                |

        ### Accepted Operators

        The table below shows the operators you can use to define how you want to search
        for the value. The operator should be put in as a string (`"="`). The operator
        has to be compatible with the field's type (eg. you cannot search with `>` for a
        given string value as it's only compatible for integer's and dates).

        | Operator | Valid Types                   | Description                                                |
        | :------- | :---------------------------- | :--------------------------------------------------------- |
        | =        | All                           | Equals                                                     |
        | !=       | All                           | Doesn't Equal                                              |
        | IN       | All                           | In Shortcut for `OR` queries Values most be in Array       |
        | NIN      | All                           | Not In Shortcut for `OR !` queries Values must be in Array |
        | >        | Integer Date (UNIX Timestamp) | Greater (or equal) than                                    |
        | <        | Integer Date (UNIX Timestamp) | Lower (or equal) than                                      |
        | ~        | String                        | Contains                                                   |
        | !~       | String                        | Doesn't Contain                                            |
        | ^        | String                        | Starts With                                                |
        | $        | String                        | Ends With                                                  |

        Args:
          query: Search using Intercoms Search APIs with a single filter.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._post(
            "/conversations/search",
            body=maybe_transform(
                {
                    "query": query,
                    "pagination": pagination,
                },
                conversation_search_params.ConversationSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationList,
        )


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def reply(self) -> AsyncReplyResource:
        return AsyncReplyResource(self._client)

    @cached_property
    def parts(self) -> AsyncPartsResource:
        return AsyncPartsResource(self._client)

    @cached_property
    def run_assignment_rules(self) -> AsyncRunAssignmentRulesResource:
        return AsyncRunAssignmentRulesResource(self._client)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: str,
        from_: conversation_create_params.From,
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
    ) -> Message:
        """You can create a conversation that has been initiated by a contact (ie.

        user or
        lead). The conversation can be an in-app message only.

        {% admonition type="info" name="Sending for visitors" %} You can also send a
        message from a visitor by specifying their `user_id` or `id` value in the `from`
        field, along with a `type` field value of `contact`. This visitor will be
        automatically converted to a contact with a lead role once the conversation is
        created. {% /admonition %}

        This will return the Message model that has been created.

        Args:
          body: The content of the message. HTML is not supported.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._post(
            "/conversations",
            body=await async_maybe_transform(
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
    ) -> Conversation:
        """
        You can fetch the details of a single conversation.

        This will return a single Conversation model with all its conversation parts.

        {% admonition type="warning" name="Hard limit of 500 parts" %} The maximum
        number of conversation parts that can be returned via the API is 500. If you
        have more than that we will return the 500 most recent conversation parts.
        {% /admonition %}

        For AI agent conversation metadata, please note that you need to have the agent
        enabled in your workspace, which is a
        [paid feature](https://www.intercom.com/help/en/articles/8205718-fin-resolutions#h_97f8c2e671).

        Args:
          display_as: Set to plaintext to retrieve conversation messages in plain text.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._get(
            f"/conversations/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
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
    ) -> Conversation:
        """
        You can update an existing conversation.

        {% admonition type="info" name="Replying and other actions" %} If you want to
        reply to a coveration or take an action such as assign, unassign, open, close or
        snooze, take a look at the reply and manage endpoints. {% /admonition %}

        Args:
          display_as: Set to plaintext to retrieve conversation messages in plain text.

          custom_attributes: An object containing the different custom attributes associated to the
              conversation as key-value pairs. For relationship attributes the value will be a
              list of custom object instance models.

          read: Mark a conversation as read within Intercom.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._put(
            f"/conversations/{id}",
            body=await async_maybe_transform(
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
                query=await async_maybe_transform(
                    {"display_as": display_as}, conversation_update_params.ConversationUpdateParams
                ),
            ),
            cast_to=Conversation,
        )

    async def list(
        self,
        *,
        per_page: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
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
    ) -> PaginatedResponse:
        """
        You can fetch a list of all conversations.

        You can optionally request the result page size and the cursor to start after to
        fetch the result. {% admonition type="warning" name="Pagination" %} You can use
        pagination to limit the number of results returned. The default is `20` results
        per page. See the
        [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#pagination-for-list-apis)
        for more details on how to use the `starting_after` param. {% /admonition %}

        Args:
          per_page: How many results per page

          starting_after: String used to get the next page of conversations.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._get(
            "/conversations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "per_page": per_page,
                        "starting_after": starting_after,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=PaginatedResponse,
        )

    async def convert(
        self,
        id: int,
        *,
        ticket_type_id: str,
        attributes: Dict[str, Union[Optional[str], float, bool, Iterable[object]]] | NotGiven = NOT_GIVEN,
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

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._post(
            f"/conversations/{id}/convert",
            body=await async_maybe_transform(
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
    ) -> Conversation:
        """
        You can redact a conversation part or the source message of a conversation (as
        seen in the source object).

        {% admonition type="info" name="Redacting parts and messages" %} If you are
        redacting a conversation part, it must have a `body`. If you are redacting a
        source message, it must have been created by a contact. We will return a
        `conversation_part_not_redactable` error if these criteria are not met.
        {% /admonition %}

        Args:
          conversation_id: The id of the conversation.

          conversation_part_id: The id of the conversation_part.

          type: The type of resource being redacted.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

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
    ) -> Conversation:
        """
        You can redact a conversation part or the source message of a conversation (as
        seen in the source object).

        {% admonition type="info" name="Redacting parts and messages" %} If you are
        redacting a conversation part, it must have a `body`. If you are redacting a
        source message, it must have been created by a contact. We will return a
        `conversation_part_not_redactable` error if these criteria are not met.
        {% /admonition %}

        Args:
          conversation_id: The id of the conversation.

          source_id: The id of the source.

          type: The type of resource being redacted.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

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
        source_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._post(
            "/conversations/redact",
            body=await async_maybe_transform(
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

    async def search(
        self,
        *,
        query: conversation_search_params.Query,
        pagination: Optional[conversation_search_params.Pagination] | NotGiven = NOT_GIVEN,
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
    ) -> ConversationList:
        """
        You can search for multiple conversations by the value of their attributes in
        order to fetch exactly which ones you want.

        To search for conversations, you need to send a `POST` request to
        `https://api.intercom.io/conversations/search`.

        This will accept a query object in the body which will define your filters in
        order to search for conversations.
        {% admonition type="warning" name="Optimizing search queries" %} Search queries
        can be complex, so optimizing them can help the performance of your search. Use
        the `AND` and `OR` operators to combine multiple filters to get the exact
        results you need and utilize pagination to limit the number of results returned.
        The default is `20` results per page and maximum is `150`. See the
        [pagination section](https://developers.intercom.com/docs/build-an-integration/learn-more/rest-apis/pagination/#example-search-conversations-request)
        for more details on how to use the `starting_after` param. {% /admonition %}

        ### Nesting & Limitations

        You can nest these filters in order to get even more granular insights that
        pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4). There are some
        limitations to the amount of multiple's there can be:

        - There's a limit of max 2 nested filters
        - There's a limit of max 15 filters for each AND or OR group

        ### Accepted Fields

        Most keys listed as part of the The conversation model is searchable, whether
        writeable or not. The value you search for has to match the accepted type,
        otherwise the query will fail (ie. as `created_at` accepts a date, the `value`
        cannot be a string such as `"foorbar"`).

        | Field                                                                                                                                        | Type                  |
        | :------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------- |
        | id                                                                                                                                           | String                |
        | created_at                                                                                                                                   | Date (UNIX timestamp) |
        | updated_at                                                                                                                                   | Date (UNIX timestamp) |
        | source.type                                                                                                                                  | String                |
        | Accepted fields are `conversation`, `email`, `facebook`, `instagram`, `phone_call`, `phone_switch`, `push`, `sms`, `twitter` and `whatsapp`. |
        | source.id                                                                                                                                    | String                |
        | source.delivered_as                                                                                                                          | String                |
        | source.subject                                                                                                                               | String                |
        | source.body                                                                                                                                  | String                |
        | source.author.id                                                                                                                             | String                |
        | source.author.type                                                                                                                           | String                |
        | source.author.name                                                                                                                           | String                |
        | source.author.email                                                                                                                          | String                |
        | source.url                                                                                                                                   | String                |
        | contact_ids                                                                                                                                  | String                |
        | teammate_ids                                                                                                                                 | String                |
        | admin_assignee_id                                                                                                                            | String                |
        | team_assignee_id                                                                                                                             | String                |
        | channel_initiated                                                                                                                            | String                |
        | open                                                                                                                                         | Boolean               |
        | read                                                                                                                                         | Boolean               |
        | state                                                                                                                                        | String                |
        | waiting_since                                                                                                                                | Date (UNIX timestamp) |
        | snoozed_until                                                                                                                                | Date (UNIX timestamp) |
        | tag_ids                                                                                                                                      | String                |
        | priority                                                                                                                                     | String                |
        | statistics.time_to_assignment                                                                                                                | Integer               |
        | statistics.time_to_admin_reply                                                                                                               | Integer               |
        | statistics.time_to_first_close                                                                                                               | Integer               |
        | statistics.time_to_last_close                                                                                                                | Integer               |
        | statistics.median_time_to_reply                                                                                                              | Integer               |
        | statistics.first_contact_reply_at                                                                                                            | Date (UNIX timestamp) |
        | statistics.first_assignment_at                                                                                                               | Date (UNIX timestamp) |
        | statistics.first_admin_reply_at                                                                                                              | Date (UNIX timestamp) |
        | statistics.first_close_at                                                                                                                    | Date (UNIX timestamp) |
        | statistics.last_assignment_at                                                                                                                | Date (UNIX timestamp) |
        | statistics.last_assignment_admin_reply_at                                                                                                    | Date (UNIX timestamp) |
        | statistics.last_contact_reply_at                                                                                                             | Date (UNIX timestamp) |
        | statistics.last_admin_reply_at                                                                                                               | Date (UNIX timestamp) |
        | statistics.last_close_at                                                                                                                     | Date (UNIX timestamp) |
        | statistics.last_closed_by_id                                                                                                                 | String                |
        | statistics.count_reopens                                                                                                                     | Integer               |
        | statistics.count_assignments                                                                                                                 | Integer               |
        | statistics.count_conversation_parts                                                                                                          | Integer               |
        | conversation_rating.requested_at                                                                                                             | Date (UNIX timestamp) |
        | conversation_rating.replied_at                                                                                                               | Date (UNIX timestamp) |
        | conversation_rating.score                                                                                                                    | Integer               |
        | conversation_rating.remark                                                                                                                   | String                |
        | conversation_rating.contact_id                                                                                                               | String                |
        | conversation_rating.admin_d                                                                                                                  | String                |
        | ai_agent_participated                                                                                                                        | Boolean               |
        | ai_agent.resolution_state                                                                                                                    | String                |
        | ai_agent.last_answer_type                                                                                                                    | String                |
        | ai_agent.rating                                                                                                                              | Integer               |
        | ai_agent.rating_remark                                                                                                                       | String                |
        | ai_agent.source_type                                                                                                                         | String                |
        | ai_agent.source_title                                                                                                                        | String                |

        ### Accepted Operators

        The table below shows the operators you can use to define how you want to search
        for the value. The operator should be put in as a string (`"="`). The operator
        has to be compatible with the field's type (eg. you cannot search with `>` for a
        given string value as it's only compatible for integer's and dates).

        | Operator | Valid Types                   | Description                                                |
        | :------- | :---------------------------- | :--------------------------------------------------------- |
        | =        | All                           | Equals                                                     |
        | !=       | All                           | Doesn't Equal                                              |
        | IN       | All                           | In Shortcut for `OR` queries Values most be in Array       |
        | NIN      | All                           | Not In Shortcut for `OR !` queries Values must be in Array |
        | >        | Integer Date (UNIX Timestamp) | Greater (or equal) than                                    |
        | <        | Integer Date (UNIX Timestamp) | Lower (or equal) than                                      |
        | ~        | String                        | Contains                                                   |
        | !~       | String                        | Doesn't Contain                                            |
        | ^        | String                        | Starts With                                                |
        | $        | String                        | Ends With                                                  |

        Args:
          query: Search using Intercoms Search APIs with a single filter.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._post(
            "/conversations/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "pagination": pagination,
                },
                conversation_search_params.ConversationSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationList,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

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
        self.convert = to_raw_response_wrapper(
            conversations.convert,
        )
        self.redact = to_raw_response_wrapper(
            conversations.redact,
        )
        self.search = to_raw_response_wrapper(
            conversations.search,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._conversations.tags)

    @cached_property
    def reply(self) -> ReplyResourceWithRawResponse:
        return ReplyResourceWithRawResponse(self._conversations.reply)

    @cached_property
    def parts(self) -> PartsResourceWithRawResponse:
        return PartsResourceWithRawResponse(self._conversations.parts)

    @cached_property
    def run_assignment_rules(self) -> RunAssignmentRulesResourceWithRawResponse:
        return RunAssignmentRulesResourceWithRawResponse(self._conversations.run_assignment_rules)

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._conversations.customers)


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

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
        self.convert = async_to_raw_response_wrapper(
            conversations.convert,
        )
        self.redact = async_to_raw_response_wrapper(
            conversations.redact,
        )
        self.search = async_to_raw_response_wrapper(
            conversations.search,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._conversations.tags)

    @cached_property
    def reply(self) -> AsyncReplyResourceWithRawResponse:
        return AsyncReplyResourceWithRawResponse(self._conversations.reply)

    @cached_property
    def parts(self) -> AsyncPartsResourceWithRawResponse:
        return AsyncPartsResourceWithRawResponse(self._conversations.parts)

    @cached_property
    def run_assignment_rules(self) -> AsyncRunAssignmentRulesResourceWithRawResponse:
        return AsyncRunAssignmentRulesResourceWithRawResponse(self._conversations.run_assignment_rules)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._conversations.customers)


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_streamed_response_wrapper(
            conversations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            conversations.update,
        )
        self.list = to_streamed_response_wrapper(
            conversations.list,
        )
        self.convert = to_streamed_response_wrapper(
            conversations.convert,
        )
        self.redact = to_streamed_response_wrapper(
            conversations.redact,
        )
        self.search = to_streamed_response_wrapper(
            conversations.search,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._conversations.tags)

    @cached_property
    def reply(self) -> ReplyResourceWithStreamingResponse:
        return ReplyResourceWithStreamingResponse(self._conversations.reply)

    @cached_property
    def parts(self) -> PartsResourceWithStreamingResponse:
        return PartsResourceWithStreamingResponse(self._conversations.parts)

    @cached_property
    def run_assignment_rules(self) -> RunAssignmentRulesResourceWithStreamingResponse:
        return RunAssignmentRulesResourceWithStreamingResponse(self._conversations.run_assignment_rules)

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._conversations.customers)


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_streamed_response_wrapper(
            conversations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            conversations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            conversations.list,
        )
        self.convert = async_to_streamed_response_wrapper(
            conversations.convert,
        )
        self.redact = async_to_streamed_response_wrapper(
            conversations.redact,
        )
        self.search = async_to_streamed_response_wrapper(
            conversations.search,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._conversations.tags)

    @cached_property
    def reply(self) -> AsyncReplyResourceWithStreamingResponse:
        return AsyncReplyResourceWithStreamingResponse(self._conversations.reply)

    @cached_property
    def parts(self) -> AsyncPartsResourceWithStreamingResponse:
        return AsyncPartsResourceWithStreamingResponse(self._conversations.parts)

    @cached_property
    def run_assignment_rules(self) -> AsyncRunAssignmentRulesResourceWithStreamingResponse:
        return AsyncRunAssignmentRulesResourceWithStreamingResponse(self._conversations.run_assignment_rules)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._conversations.customers)
