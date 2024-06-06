# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..types.shared.subscription_type_list import SubscriptionTypeList

__all__ = ["SubscriptionTypesResource", "AsyncSubscriptionTypesResource"]


class SubscriptionTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionTypesResourceWithRawResponse:
        return SubscriptionTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionTypesResourceWithStreamingResponse:
        return SubscriptionTypesResourceWithStreamingResponse(self)

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


class AsyncSubscriptionTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionTypesResourceWithRawResponse:
        return AsyncSubscriptionTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionTypesResourceWithStreamingResponse:
        return AsyncSubscriptionTypesResourceWithStreamingResponse(self)

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


class SubscriptionTypesResourceWithRawResponse:
    def __init__(self, subscription_types: SubscriptionTypesResource) -> None:
        self._subscription_types = subscription_types

        self.list = to_raw_response_wrapper(
            subscription_types.list,
        )


class AsyncSubscriptionTypesResourceWithRawResponse:
    def __init__(self, subscription_types: AsyncSubscriptionTypesResource) -> None:
        self._subscription_types = subscription_types

        self.list = async_to_raw_response_wrapper(
            subscription_types.list,
        )


class SubscriptionTypesResourceWithStreamingResponse:
    def __init__(self, subscription_types: SubscriptionTypesResource) -> None:
        self._subscription_types = subscription_types

        self.list = to_streamed_response_wrapper(
            subscription_types.list,
        )


class AsyncSubscriptionTypesResourceWithStreamingResponse:
    def __init__(self, subscription_types: AsyncSubscriptionTypesResource) -> None:
        self._subscription_types = subscription_types

        self.list = async_to_streamed_response_wrapper(
            subscription_types.list,
        )
