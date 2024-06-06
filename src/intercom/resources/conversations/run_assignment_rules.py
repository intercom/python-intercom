# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.shared.conversation import Conversation

__all__ = ["RunAssignmentRulesResource", "AsyncRunAssignmentRulesResource"]


class RunAssignmentRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunAssignmentRulesResourceWithRawResponse:
        return RunAssignmentRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunAssignmentRulesResourceWithStreamingResponse:
        return RunAssignmentRulesResourceWithStreamingResponse(self)

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conversations/{id}/run_assignment_rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class AsyncRunAssignmentRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunAssignmentRulesResourceWithRawResponse:
        return AsyncRunAssignmentRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunAssignmentRulesResourceWithStreamingResponse:
        return AsyncRunAssignmentRulesResourceWithStreamingResponse(self)

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conversations/{id}/run_assignment_rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class RunAssignmentRulesResourceWithRawResponse:
    def __init__(self, run_assignment_rules: RunAssignmentRulesResource) -> None:
        self._run_assignment_rules = run_assignment_rules

        self.create = to_raw_response_wrapper(
            run_assignment_rules.create,
        )


class AsyncRunAssignmentRulesResourceWithRawResponse:
    def __init__(self, run_assignment_rules: AsyncRunAssignmentRulesResource) -> None:
        self._run_assignment_rules = run_assignment_rules

        self.create = async_to_raw_response_wrapper(
            run_assignment_rules.create,
        )


class RunAssignmentRulesResourceWithStreamingResponse:
    def __init__(self, run_assignment_rules: RunAssignmentRulesResource) -> None:
        self._run_assignment_rules = run_assignment_rules

        self.create = to_streamed_response_wrapper(
            run_assignment_rules.create,
        )


class AsyncRunAssignmentRulesResourceWithStreamingResponse:
    def __init__(self, run_assignment_rules: AsyncRunAssignmentRulesResource) -> None:
        self._run_assignment_rules = run_assignment_rules

        self.create = async_to_streamed_response_wrapper(
            run_assignment_rules.create,
        )
