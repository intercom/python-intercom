# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.shared import SubscriptionTypeList
from ...types.contacts import SubscriptionType, subscription_create_params

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    with_raw_response: SubscriptionsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = SubscriptionsWithRawResponse(self)

    def create(
        self,
        contact_id: str,
        *,
        id: str,
        consent_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionType:
        """You can add a specific subscription to a contact.

        In Intercom, we have two
        different subscription types based on user consent - opt-out and opt-in:

        1.Attaching a contact to an opt-out subscription type will opt that user out
        from receiving messages related to that subscription type.

        2.Attaching a contact to an opt-in subscription type will opt that user in to
        receiving messages related to that subscription type.

        This will return a subscription type model for the subscription type that was
        added to the contact.

        Args:
          id: The unique identifier for the subscription which is given by Intercom

          consent_type: The consent_type of a subscription, opt_out or opt_in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/contacts/{contact_id}/subscriptions",
            body=maybe_transform(
                {
                    "id": id,
                    "consent_type": consent_type,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionType,
        )

    def list(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionTypeList:
        """You can fetch a list of subscription types that are attached to a contact.

        These
        can be subscriptions that a user has 'opted-in' to or has 'opted-out' from,
        depending on the subscription type. This will return a list of Subscription Type
        objects that the contact is associated with.

        The data property will show a combined list of:

        1.Opt-out subscription types that the user has opted-out from. 2.Opt-in
        subscription types that the user has opted-in to receiving.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/contacts/{contact_id}/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionTypeList,
        )


class AsyncSubscriptions(AsyncAPIResource):
    with_raw_response: AsyncSubscriptionsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncSubscriptionsWithRawResponse(self)

    async def create(
        self,
        contact_id: str,
        *,
        id: str,
        consent_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionType:
        """You can add a specific subscription to a contact.

        In Intercom, we have two
        different subscription types based on user consent - opt-out and opt-in:

        1.Attaching a contact to an opt-out subscription type will opt that user out
        from receiving messages related to that subscription type.

        2.Attaching a contact to an opt-in subscription type will opt that user in to
        receiving messages related to that subscription type.

        This will return a subscription type model for the subscription type that was
        added to the contact.

        Args:
          id: The unique identifier for the subscription which is given by Intercom

          consent_type: The consent_type of a subscription, opt_out or opt_in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/contacts/{contact_id}/subscriptions",
            body=maybe_transform(
                {
                    "id": id,
                    "consent_type": consent_type,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionType,
        )

    async def list(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionTypeList:
        """You can fetch a list of subscription types that are attached to a contact.

        These
        can be subscriptions that a user has 'opted-in' to or has 'opted-out' from,
        depending on the subscription type. This will return a list of Subscription Type
        objects that the contact is associated with.

        The data property will show a combined list of:

        1.Opt-out subscription types that the user has opted-out from. 2.Opt-in
        subscription types that the user has opted-in to receiving.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/contacts/{contact_id}/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionTypeList,
        )


class SubscriptionsWithRawResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )


class AsyncSubscriptionsWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
