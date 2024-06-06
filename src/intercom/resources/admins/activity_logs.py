# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.admins import activity_log_list_params
from ...types.admins.activity_log_list import ActivityLogList

__all__ = ["ActivityLogsResource", "AsyncActivityLogsResource"]


class ActivityLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivityLogsResourceWithRawResponse:
        return ActivityLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivityLogsResourceWithStreamingResponse:
        return ActivityLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        created_at_after: str,
        created_at_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivityLogList:
        """
        You can get a log of activities by all admins in an app.

        Args:
          created_at_after: The start date that you request data for. It must be formatted as a UNIX
              timestamp.

          created_at_before: The end date that you request data for. It must be formatted as a UNIX
              timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admins/activity_logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_after": created_at_after,
                        "created_at_before": created_at_before,
                    },
                    activity_log_list_params.ActivityLogListParams,
                ),
            ),
            cast_to=ActivityLogList,
        )


class AsyncActivityLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivityLogsResourceWithRawResponse:
        return AsyncActivityLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivityLogsResourceWithStreamingResponse:
        return AsyncActivityLogsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        created_at_after: str,
        created_at_before: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivityLogList:
        """
        You can get a log of activities by all admins in an app.

        Args:
          created_at_after: The start date that you request data for. It must be formatted as a UNIX
              timestamp.

          created_at_before: The end date that you request data for. It must be formatted as a UNIX
              timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admins/activity_logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_at_after": created_at_after,
                        "created_at_before": created_at_before,
                    },
                    activity_log_list_params.ActivityLogListParams,
                ),
            ),
            cast_to=ActivityLogList,
        )


class ActivityLogsResourceWithRawResponse:
    def __init__(self, activity_logs: ActivityLogsResource) -> None:
        self._activity_logs = activity_logs

        self.list = to_raw_response_wrapper(
            activity_logs.list,
        )


class AsyncActivityLogsResourceWithRawResponse:
    def __init__(self, activity_logs: AsyncActivityLogsResource) -> None:
        self._activity_logs = activity_logs

        self.list = async_to_raw_response_wrapper(
            activity_logs.list,
        )


class ActivityLogsResourceWithStreamingResponse:
    def __init__(self, activity_logs: ActivityLogsResource) -> None:
        self._activity_logs = activity_logs

        self.list = to_streamed_response_wrapper(
            activity_logs.list,
        )


class AsyncActivityLogsResourceWithStreamingResponse:
    def __init__(self, activity_logs: AsyncActivityLogsResource) -> None:
        self._activity_logs = activity_logs

        self.list = async_to_streamed_response_wrapper(
            activity_logs.list,
        )
