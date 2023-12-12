# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx

from ...types import AdminList
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .activity_logs import (
    ActivityLogs,
    AsyncActivityLogs,
    ActivityLogsWithRawResponse,
    AsyncActivityLogsWithRawResponse,
)
from ..._base_client import make_request_options
from ...types.shared import Admin

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Admins", "AsyncAdmins"]


class Admins(SyncAPIResource):
    activity_logs: ActivityLogs
    with_raw_response: AdminsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.activity_logs = ActivityLogs(client)
        self.with_raw_response = AdminsWithRawResponse(self)

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


class AsyncAdmins(AsyncAPIResource):
    activity_logs: AsyncActivityLogs
    with_raw_response: AsyncAdminsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.activity_logs = AsyncActivityLogs(client)
        self.with_raw_response = AsyncAdminsWithRawResponse(self)

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


class AdminsWithRawResponse:
    def __init__(self, admins: Admins) -> None:
        self.activity_logs = ActivityLogsWithRawResponse(admins.activity_logs)

        self.retrieve = to_raw_response_wrapper(
            admins.retrieve,
        )
        self.list = to_raw_response_wrapper(
            admins.list,
        )


class AsyncAdminsWithRawResponse:
    def __init__(self, admins: AsyncAdmins) -> None:
        self.activity_logs = AsyncActivityLogsWithRawResponse(admins.activity_logs)

        self.retrieve = async_to_raw_response_wrapper(
            admins.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            admins.list,
        )
