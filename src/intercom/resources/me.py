# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx

from ..types import AdminWithApp
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Intercom, AsyncIntercom

__all__ = ["Me", "AsyncMe"]


class Me(SyncAPIResource):
    with_raw_response: MeWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = MeWithRawResponse(self)

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


class AsyncMe(AsyncAPIResource):
    with_raw_response: AsyncMeWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncMeWithRawResponse(self)

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


class MeWithRawResponse:
    def __init__(self, me: Me) -> None:
        self.retrieve = to_raw_response_wrapper(
            me.retrieve,
        )


class AsyncMeWithRawResponse:
    def __init__(self, me: AsyncMe) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            me.retrieve,
        )
