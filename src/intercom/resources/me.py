# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.admin_with_app import AdminWithApp

__all__ = ["MeResource", "AsyncMeResource"]


class MeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MeResourceWithRawResponse:
        return MeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeResourceWithStreamingResponse:
        return MeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AdminWithApp]:
        """
        You can view the currently authorised admin along with the embedded app object
        (a "workspace" in legacy terminology).

        > 🚧 Single Sign On
        >
        > If you are building a custom "Log in with Intercom" flow for your site, and
        > you call the `/me` endpoint to identify the logged-in user, you should not
        > accept any sign-ins from users with unverified email addresses as it poses a
        > potential impersonation security risk.
        """
        return self._get(
            "/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminWithApp,
        )


class AsyncMeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMeResourceWithRawResponse:
        return AsyncMeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeResourceWithStreamingResponse:
        return AsyncMeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AdminWithApp]:
        """
        You can view the currently authorised admin along with the embedded app object
        (a "workspace" in legacy terminology).

        > 🚧 Single Sign On
        >
        > If you are building a custom "Log in with Intercom" flow for your site, and
        > you call the `/me` endpoint to identify the logged-in user, you should not
        > accept any sign-ins from users with unverified email addresses as it poses a
        > potential impersonation security risk.
        """
        return await self._get(
            "/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdminWithApp,
        )


class MeResourceWithRawResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.retrieve = to_raw_response_wrapper(
            me.retrieve,
        )


class AsyncMeResourceWithRawResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.retrieve = async_to_raw_response_wrapper(
            me.retrieve,
        )


class MeResourceWithStreamingResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.retrieve = to_streamed_response_wrapper(
            me.retrieve,
        )


class AsyncMeResourceWithStreamingResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.retrieve = async_to_streamed_response_wrapper(
            me.retrieve,
        )
