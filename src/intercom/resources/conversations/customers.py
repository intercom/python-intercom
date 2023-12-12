# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.shared import Conversation
from ...types.conversations import customer_create_params

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Customers", "AsyncCustomers"]


class Customers(SyncAPIResource):
    with_raw_response: CustomersWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = CustomersWithRawResponse(self)

    def create(
        self,
        id: str,
        *,
        admin_id: str | NotGiven = NOT_GIVEN,
        customer: customer_create_params.Customer | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can add participants who are contacts to a conversation, on behalf of either
        another contact or an admin.

        > 🚧 Note about contacts without an email
        >
        > If you add a contact via the email parameter and there is no user/lead found
        > on that workspace with he given email, then we will create a new contact with
        > `role` set to `lead`.

        Args:
          admin_id: The `id` of the admin who is adding the new participant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/conversations/{id}/customers",
            body=maybe_transform(
                {
                    "admin_id": admin_id,
                    "customer": customer,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class AsyncCustomers(AsyncAPIResource):
    with_raw_response: AsyncCustomersWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCustomersWithRawResponse(self)

    async def create(
        self,
        id: str,
        *,
        admin_id: str | NotGiven = NOT_GIVEN,
        customer: customer_create_params.Customer | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can add participants who are contacts to a conversation, on behalf of either
        another contact or an admin.

        > 🚧 Note about contacts without an email
        >
        > If you add a contact via the email parameter and there is no user/lead found
        > on that workspace with he given email, then we will create a new contact with
        > `role` set to `lead`.

        Args:
          admin_id: The `id` of the admin who is adding the new participant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/conversations/{id}/customers",
            body=maybe_transform(
                {
                    "admin_id": admin_id,
                    "customer": customer,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class CustomersWithRawResponse:
    def __init__(self, customers: Customers) -> None:
        self.create = to_raw_response_wrapper(
            customers.create,
        )


class AsyncCustomersWithRawResponse:
    def __init__(self, customers: AsyncCustomers) -> None:
        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
