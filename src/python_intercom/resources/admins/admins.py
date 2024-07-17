# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import admin_set_away_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
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
from ..._base_client import make_request_options
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
    ) -> Optional[Admin]:
        """
        You can retrieve the details of a single admin.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
    ) -> AdminList:
        """
        You can fetch a list of admins for a given workspace.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._get(
            "/admins",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminList,
        )

    def set_away(
        self,
        id: int,
        *,
        away_mode_enabled: bool,
        away_mode_reassign: bool,
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
    ) -> Optional[Admin]:
        """
        You can set an Admin as away for the Inbox.

        Args:
          away_mode_enabled: Set to "true" to change the status of the admin to away.

          away_mode_reassign: Set to "true" to assign any new conversation replies to your default inbox.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._put(
            f"/admins/{id}/away",
            body=maybe_transform(
                {
                    "away_mode_enabled": away_mode_enabled,
                    "away_mode_reassign": away_mode_reassign,
                },
                admin_set_away_params.AdminSetAwayParams,
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
    ) -> Optional[Admin]:
        """
        You can retrieve the details of a single admin.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
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
    ) -> AdminList:
        """
        You can fetch a list of admins for a given workspace.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/admins",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminList,
        )

    async def set_away(
        self,
        id: int,
        *,
        away_mode_enabled: bool,
        away_mode_reassign: bool,
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
    ) -> Optional[Admin]:
        """
        You can set an Admin as away for the Inbox.

        Args:
          away_mode_enabled: Set to "true" to change the status of the admin to away.

          away_mode_reassign: Set to "true" to assign any new conversation replies to your default inbox.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._put(
            f"/admins/{id}/away",
            body=await async_maybe_transform(
                {
                    "away_mode_enabled": away_mode_enabled,
                    "away_mode_reassign": away_mode_reassign,
                },
                admin_set_away_params.AdminSetAwayParams,
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
        self.set_away = to_raw_response_wrapper(
            admins.set_away,
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
        self.set_away = async_to_raw_response_wrapper(
            admins.set_away,
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
        self.set_away = to_streamed_response_wrapper(
            admins.set_away,
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
        self.set_away = async_to_streamed_response_wrapper(
            admins.set_away,
        )

    @cached_property
    def activity_logs(self) -> AsyncActivityLogsResourceWithStreamingResponse:
        return AsyncActivityLogsResourceWithStreamingResponse(self._admins.activity_logs)
