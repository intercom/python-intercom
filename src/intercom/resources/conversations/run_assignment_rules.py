# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.shared import Conversation

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["RunAssignmentRules", "AsyncRunAssignmentRules"]


class RunAssignmentRules(SyncAPIResource):
    with_raw_response: RunAssignmentRulesWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = RunAssignmentRulesWithRawResponse(self)

    def create(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can let a conversation be automatically assigned following assignment rules.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/conversations/{id}/run_assignment_rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class AsyncRunAssignmentRules(AsyncAPIResource):
    with_raw_response: AsyncRunAssignmentRulesWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncRunAssignmentRulesWithRawResponse(self)

    async def create(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can let a conversation be automatically assigned following assignment rules.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/conversations/{id}/run_assignment_rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class RunAssignmentRulesWithRawResponse:
    def __init__(self, run_assignment_rules: RunAssignmentRules) -> None:
        self.create = to_raw_response_wrapper(
            run_assignment_rules.create,
        )


class AsyncRunAssignmentRulesWithRawResponse:
    def __init__(self, run_assignment_rules: AsyncRunAssignmentRules) -> None:
        self.create = async_to_raw_response_wrapper(
            run_assignment_rules.create,
        )
