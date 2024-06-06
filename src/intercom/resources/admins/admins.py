# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import admin_away_params
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
from .activity_logs import (
    ActivityLogsResource,
    AsyncActivityLogsResource,
    ActivityLogsResourceWithRawResponse,
    AsyncActivityLogsResourceWithRawResponse,
    ActivityLogsResourceWithStreamingResponse,
    AsyncActivityLogsResourceWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)
from ...types.admin_list import AdminList
from ...types.shared.admin import Admin

__all__ = ["AdminsResource", "AsyncAdminsResource"]


class AdminsResource(SyncAPIResource):
    @cached_property
    def activity_logs(self) -> ActivityLogsResource:
        return ActivityLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdminsResourceWithRawResponse:
        return AdminsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminsResourceWithStreamingResponse:
        return AdminsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Admin]:
        """
        You can retrieve the details of a single admin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/admins/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Admin,
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
    ) -> AdminList:
        """You can fetch a list of admins for a given workspace."""
        return self._get(
            "/admins",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminList,
        )

    def away(
        self,
        id: int,
        *,
        away_mode_enabled: bool,
        away_mode_reassign: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Admin]:
        """
        You can set an Admin as away for the Inbox.

        Args:
          away_mode_enabled: Set to "true" to change the status of the admin to away.

          away_mode_reassign: Set to "true" to assign any new conversation replies to your default inbox.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/admins/{id}/away",
            body=maybe_transform(
                {
                    "away_mode_enabled": away_mode_enabled,
                    "away_mode_reassign": away_mode_reassign,
                },
                admin_away_params.AdminAwayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Admin,
        )


class AsyncAdminsResource(AsyncAPIResource):
    @cached_property
    def activity_logs(self) -> AsyncActivityLogsResource:
        return AsyncActivityLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdminsResourceWithRawResponse:
        return AsyncAdminsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminsResourceWithStreamingResponse:
        return AsyncAdminsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Admin]:
        """
        You can retrieve the details of a single admin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/admins/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Admin,
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
    ) -> AdminList:
        """You can fetch a list of admins for a given workspace."""
        return await self._get(
            "/admins",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminList,
        )

    async def away(
        self,
        id: int,
        *,
        away_mode_enabled: bool,
        away_mode_reassign: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Admin]:
        """
        You can set an Admin as away for the Inbox.

        Args:
          away_mode_enabled: Set to "true" to change the status of the admin to away.

          away_mode_reassign: Set to "true" to assign any new conversation replies to your default inbox.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/admins/{id}/away",
            body=await async_maybe_transform(
                {
                    "away_mode_enabled": away_mode_enabled,
                    "away_mode_reassign": away_mode_reassign,
                },
                admin_away_params.AdminAwayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Admin,
        )


class AdminsResourceWithRawResponse:
    def __init__(self, admins: AdminsResource) -> None:
        self._admins = admins

        self.retrieve = to_raw_response_wrapper(
            admins.retrieve,
        )
        self.list = to_raw_response_wrapper(
            admins.list,
        )
        self.away = to_raw_response_wrapper(
            admins.away,
        )

    @cached_property
    def activity_logs(self) -> ActivityLogsResourceWithRawResponse:
        return ActivityLogsResourceWithRawResponse(self._admins.activity_logs)


class AsyncAdminsResourceWithRawResponse:
    def __init__(self, admins: AsyncAdminsResource) -> None:
        self._admins = admins

        self.retrieve = async_to_raw_response_wrapper(
            admins.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            admins.list,
        )
        self.away = async_to_raw_response_wrapper(
            admins.away,
        )

    @cached_property
    def activity_logs(self) -> AsyncActivityLogsResourceWithRawResponse:
        return AsyncActivityLogsResourceWithRawResponse(self._admins.activity_logs)


class AdminsResourceWithStreamingResponse:
    def __init__(self, admins: AdminsResource) -> None:
        self._admins = admins

        self.retrieve = to_streamed_response_wrapper(
            admins.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            admins.list,
        )
        self.away = to_streamed_response_wrapper(
            admins.away,
        )

    @cached_property
    def activity_logs(self) -> ActivityLogsResourceWithStreamingResponse:
        return ActivityLogsResourceWithStreamingResponse(self._admins.activity_logs)


class AsyncAdminsResourceWithStreamingResponse:
    def __init__(self, admins: AsyncAdminsResource) -> None:
        self._admins = admins

        self.retrieve = async_to_streamed_response_wrapper(
            admins.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            admins.list,
        )
        self.away = async_to_streamed_response_wrapper(
            admins.away,
        )

    @cached_property
    def activity_logs(self) -> AsyncActivityLogsResourceWithStreamingResponse:
        return AsyncActivityLogsResourceWithStreamingResponse(self._admins.activity_logs)
