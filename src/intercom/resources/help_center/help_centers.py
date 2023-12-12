# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.help_center import HelpCenter, HelpCenterList

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["HelpCenters", "AsyncHelpCenters"]


class HelpCenters(SyncAPIResource):
    with_raw_response: HelpCentersWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = HelpCentersWithRawResponse(self)

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
    ) -> HelpCenter:
        """
        You can fetch the details of a single Help Center by making a GET request to
        `https://api.intercom.io/help_center/help_center/<id>`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/help_center/help_centers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HelpCenter,
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
    ) -> HelpCenterList:
        """
        You can list all Help Centers by making a GET request to
        `https://api.intercom.io/help_center/help_centers`.
        """
        return self._get(
            "/help_center/help_centers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HelpCenterList,
        )


class AsyncHelpCenters(AsyncAPIResource):
    with_raw_response: AsyncHelpCentersWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncHelpCentersWithRawResponse(self)

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
    ) -> HelpCenter:
        """
        You can fetch the details of a single Help Center by making a GET request to
        `https://api.intercom.io/help_center/help_center/<id>`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/help_center/help_centers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HelpCenter,
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
    ) -> HelpCenterList:
        """
        You can list all Help Centers by making a GET request to
        `https://api.intercom.io/help_center/help_centers`.
        """
        return await self._get(
            "/help_center/help_centers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HelpCenterList,
        )


class HelpCentersWithRawResponse:
    def __init__(self, help_centers: HelpCenters) -> None:
        self.retrieve = to_raw_response_wrapper(
            help_centers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            help_centers.list,
        )


class AsyncHelpCentersWithRawResponse:
    def __init__(self, help_centers: AsyncHelpCenters) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            help_centers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            help_centers.list,
        )
