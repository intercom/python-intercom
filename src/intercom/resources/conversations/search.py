# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.conversations import ConversationList, search_create_params

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Search", "AsyncSearch"]


class Search(SyncAPIResource):
    with_raw_response: SearchWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = SearchWithRawResponse(self)

    def create(
        self,
        *,
        query: search_create_params.Query,
        pagination: Optional[search_create_params.Pagination] | NotGiven = NOT_GIVEN,
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

        To search for conversations, you need to send a POST request to
        https://api.intercom.io/conversations/search. This will accept a query object in
        the body which will define your filters in order to search for conversations.

        > 🚧 Nesting & Limitations
        >
        > You can nest these filters in order to get even more granular insights that
        > pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4). There are some
        > limitations to the amount of multiple's there can be:
        >
        > - There's a limit of max 2 nested filters
        > - There's a limit of max 15 filters for each AND or OR group

        ### Accepted Fields

        Most keys listed as part of the The conversation model is searchable, whether
        writeable or not. The value you search for has to match the accepted type,
        otherwise the query will fail (ie. as `created_at` accepts a date, the `value`
        cannot be a string such as `"foorbar"`).

        | Field                                     | Type                                                                                     |
        | :---------------------------------------- | :--------------------------------------------------------------------------------------- |
        | id                                        | String                                                                                   |
        | created_at                                | Date (UNIX timestamp)                                                                    |
        | updated_at                                | Date (UNIX timestamp)                                                                    |
        | source.type                               | String                                                                                   |
        | source.id                                 | String                                                                                   |
        | source.delivered_as                       | String                                                                                   |
        | source.subject                            | String                                                                                   |
        | source.body                               | String                                                                                   |
        | source.author.id                          | String                                                                                   |
        | source.author.type                        | String                                                                                   |
        | source.author.name                        | String                                                                                   |
        | source.author.email                       | String                                                                                   |
        | source.url                                | String                                                                                   |
        | contact_ids                               | String                                                                                   |
        | teammate_ids                              | String                                                                                   |
        | admin_assignee_id                         | String                                                                                   |
        | team_assignee_id                          | String                                                                                   |
        | channel_initiated                         | String<br>Accepted fields are `conversation`, `push`, `facebook`, `twitter` and `email`. |
        | open                                      | Boolean                                                                                  |
        | read                                      | Boolean                                                                                  |
        | state                                     | String                                                                                   |
        | waiting_since                             | Date (UNIX timestamp)                                                                    |
        | snoozed_until                             | Date (UNIX timestamp)                                                                    |
        | tag_ids                                   | String                                                                                   |
        | priority                                  | String                                                                                   |
        | statistics.time_to_assignment             | Integer                                                                                  |
        | statistics.time_to_admin_reply            | Integer                                                                                  |
        | statistics.time_to_first_close            | Integer                                                                                  |
        | statistics.time_to_last_close             | Integer                                                                                  |
        | statistics.median_time_to_reply           | Integer                                                                                  |
        | statistics.first_contact_reply_at         | Date (UNIX timestamp)                                                                    |
        | statistics.first_assignment_at            | Date (UNIX timestamp)                                                                    |
        | statistics.first_admin_reply_at           | Date (UNIX timestamp)                                                                    |
        | statistics.first_close_at                 | Date (UNIX timestamp)                                                                    |
        | statistics.last_assignment_at             | Date (UNIX timestamp)                                                                    |
        | statistics.last_assignment_admin_reply_at | Date (UNIX timestamp)                                                                    |
        | statistics.last_contact_reply_at          | Date (UNIX timestamp)                                                                    |
        | statistics.last_admin_reply_at            | Date (UNIX timestamp)                                                                    |
        | statistics.last_close_at                  | Date (UNIX timestamp)                                                                    |
        | statistics.last_closed_by_id              | String                                                                                   |
        | statistics.count_reopens                  | Integer                                                                                  |
        | statistics.count_assignments              | Integer                                                                                  |
        | statistics.count_conversation_parts       | Integer                                                                                  |
        | conversation_rating.requested_at          | Date (UNIX timestamp)                                                                    |
        | conversation_rating.replied_at            | Date (UNIX timestamp)                                                                    |
        | conversation_rating.score                 | Integer                                                                                  |
        | conversation_rating.remark                | String                                                                                   |
        | conversation_rating.contact_id            | String                                                                                   |
        | conversation_rating.admin_d               | String                                                                                   |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/conversations/search",
            body=maybe_transform(
                {
                    "query": query,
                    "pagination": pagination,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationList,
        )


class AsyncSearch(AsyncAPIResource):
    with_raw_response: AsyncSearchWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncSearchWithRawResponse(self)

    async def create(
        self,
        *,
        query: search_create_params.Query,
        pagination: Optional[search_create_params.Pagination] | NotGiven = NOT_GIVEN,
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

        To search for conversations, you need to send a POST request to
        https://api.intercom.io/conversations/search. This will accept a query object in
        the body which will define your filters in order to search for conversations.

        > 🚧 Nesting & Limitations
        >
        > You can nest these filters in order to get even more granular insights that
        > pinpoint exactly what you need. Example: (1 OR 2) AND (3 OR 4). There are some
        > limitations to the amount of multiple's there can be:
        >
        > - There's a limit of max 2 nested filters
        > - There's a limit of max 15 filters for each AND or OR group

        ### Accepted Fields

        Most keys listed as part of the The conversation model is searchable, whether
        writeable or not. The value you search for has to match the accepted type,
        otherwise the query will fail (ie. as `created_at` accepts a date, the `value`
        cannot be a string such as `"foorbar"`).

        | Field                                     | Type                                                                                     |
        | :---------------------------------------- | :--------------------------------------------------------------------------------------- |
        | id                                        | String                                                                                   |
        | created_at                                | Date (UNIX timestamp)                                                                    |
        | updated_at                                | Date (UNIX timestamp)                                                                    |
        | source.type                               | String                                                                                   |
        | source.id                                 | String                                                                                   |
        | source.delivered_as                       | String                                                                                   |
        | source.subject                            | String                                                                                   |
        | source.body                               | String                                                                                   |
        | source.author.id                          | String                                                                                   |
        | source.author.type                        | String                                                                                   |
        | source.author.name                        | String                                                                                   |
        | source.author.email                       | String                                                                                   |
        | source.url                                | String                                                                                   |
        | contact_ids                               | String                                                                                   |
        | teammate_ids                              | String                                                                                   |
        | admin_assignee_id                         | String                                                                                   |
        | team_assignee_id                          | String                                                                                   |
        | channel_initiated                         | String<br>Accepted fields are `conversation`, `push`, `facebook`, `twitter` and `email`. |
        | open                                      | Boolean                                                                                  |
        | read                                      | Boolean                                                                                  |
        | state                                     | String                                                                                   |
        | waiting_since                             | Date (UNIX timestamp)                                                                    |
        | snoozed_until                             | Date (UNIX timestamp)                                                                    |
        | tag_ids                                   | String                                                                                   |
        | priority                                  | String                                                                                   |
        | statistics.time_to_assignment             | Integer                                                                                  |
        | statistics.time_to_admin_reply            | Integer                                                                                  |
        | statistics.time_to_first_close            | Integer                                                                                  |
        | statistics.time_to_last_close             | Integer                                                                                  |
        | statistics.median_time_to_reply           | Integer                                                                                  |
        | statistics.first_contact_reply_at         | Date (UNIX timestamp)                                                                    |
        | statistics.first_assignment_at            | Date (UNIX timestamp)                                                                    |
        | statistics.first_admin_reply_at           | Date (UNIX timestamp)                                                                    |
        | statistics.first_close_at                 | Date (UNIX timestamp)                                                                    |
        | statistics.last_assignment_at             | Date (UNIX timestamp)                                                                    |
        | statistics.last_assignment_admin_reply_at | Date (UNIX timestamp)                                                                    |
        | statistics.last_contact_reply_at          | Date (UNIX timestamp)                                                                    |
        | statistics.last_admin_reply_at            | Date (UNIX timestamp)                                                                    |
        | statistics.last_close_at                  | Date (UNIX timestamp)                                                                    |
        | statistics.last_closed_by_id              | String                                                                                   |
        | statistics.count_reopens                  | Integer                                                                                  |
        | statistics.count_assignments              | Integer                                                                                  |
        | statistics.count_conversation_parts       | Integer                                                                                  |
        | conversation_rating.requested_at          | Date (UNIX timestamp)                                                                    |
        | conversation_rating.replied_at            | Date (UNIX timestamp)                                                                    |
        | conversation_rating.score                 | Integer                                                                                  |
        | conversation_rating.remark                | String                                                                                   |
        | conversation_rating.contact_id            | String                                                                                   |
        | conversation_rating.admin_d               | String                                                                                   |

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/conversations/search",
            body=maybe_transform(
                {
                    "query": query,
                    "pagination": pagination,
                },
                search_create_params.SearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationList,
        )


class SearchWithRawResponse:
    def __init__(self, search: Search) -> None:
        self.create = to_raw_response_wrapper(
            search.create,
        )


class AsyncSearchWithRawResponse:
    def __init__(self, search: AsyncSearch) -> None:
        self.create = async_to_raw_response_wrapper(
            search.create,
        )
