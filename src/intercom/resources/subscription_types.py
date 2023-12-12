# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options
from ..types.shared import SubscriptionTypeList

if TYPE_CHECKING:
    from .._client import Intercom, AsyncIntercom

__all__ = ["SubscriptionTypes", "AsyncSubscriptionTypes"]


class SubscriptionTypes(SyncAPIResource):
    with_raw_response: SubscriptionTypesWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = SubscriptionTypesWithRawResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionTypeList:
        """You can list all subscription types.

        A list of subscription type objects will be
        returned.
        """
        return self._get(
            "/subscription_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionTypeList,
        )


class AsyncSubscriptionTypes(AsyncAPIResource):
    with_raw_response: AsyncSubscriptionTypesWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncSubscriptionTypesWithRawResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionTypeList:
        """You can list all subscription types.

        A list of subscription type objects will be
        returned.
        """
        return await self._get(
            "/subscription_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionTypeList,
        )


class SubscriptionTypesWithRawResponse:
    def __init__(self, subscription_types: SubscriptionTypes) -> None:
        self.list = to_raw_response_wrapper(
            subscription_types.list,
        )


class AsyncSubscriptionTypesWithRawResponse:
    def __init__(self, subscription_types: AsyncSubscriptionTypes) -> None:
        self.list = async_to_raw_response_wrapper(
            subscription_types.list,
        )
