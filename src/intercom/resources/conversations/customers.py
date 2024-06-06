# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ..._base_client import (
    make_request_options,
)
from ...types.conversations import customer_create_params, customer_delete_params
from ...types.shared.conversation import Conversation

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self)

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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

    def delete(
        self,
        contact_id: str,
        *,
        conversation_id: str,
        admin_id: str,
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
          admin_id: The `id` of the admin who is performing the action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._delete(
            f"/conversations/{conversation_id}/customers/{contact_id}",
            body=maybe_transform({"admin_id": admin_id}, customer_delete_params.CustomerDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self)

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conversations/{id}/customers",
            body=await async_maybe_transform(
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

    async def delete(
        self,
        contact_id: str,
        *,
        conversation_id: str,
        admin_id: str,
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
          admin_id: The `id` of the admin who is performing the action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._delete(
            f"/conversations/{conversation_id}/customers/{contact_id}",
            body=await async_maybe_transform({"admin_id": admin_id}, customer_delete_params.CustomerDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.delete = to_raw_response_wrapper(
            customers.delete,
        )


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.delete = async_to_raw_response_wrapper(
            customers.delete,
        )


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.delete = to_streamed_response_wrapper(
            customers.delete,
        )


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            customers.delete,
        )
