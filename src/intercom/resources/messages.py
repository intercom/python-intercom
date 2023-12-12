# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, overload

import httpx

from ..types import message_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import required_args, maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options
from ..types.shared import Message

if TYPE_CHECKING:
    from .._client import Intercom, AsyncIntercom

__all__ = ["Messages", "AsyncMessages"]


class Messages(SyncAPIResource):
    with_raw_response: MessagesWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = MessagesWithRawResponse(self)

    @overload
    def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """You can create a message that has been initiated by an admin.

        The conversation
        can be either an in-app message or an email.

        > 🚧 Sending for visitors
        >
        > There can be a short delay between when a contact is created and when a
        > contact becomes available to be messaged through the API. A 404 Not Found
        > error will be returned in this case.

        This will return the Message model that has been created.

        > 🚧 Retrieving Associated Conversations
        >
        > As this is a message, there will be no conversation present until the contact
        > responds. Once they do, you will have to search for a contact's conversations
        > with the id of the message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """You can create a message that has been initiated by an admin.

        The conversation
        can be either an in-app message or an email.

        > 🚧 Sending for visitors
        >
        > There can be a short delay between when a contact is created and when a
        > contact becomes available to be messaged through the API. A 404 Not Found
        > error will be returned in this case.

        This will return the Message model that has been created.

        > 🚧 Retrieving Associated Conversations
        >
        > As this is a message, there will be no conversation present until the contact
        > responds. Once they do, you will have to search for a contact's conversations
        > with the id of the message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body"], ["body"])
    def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        return self._post(
            "/messages",
            body=maybe_transform(body, message_create_params.MessageCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )


class AsyncMessages(AsyncAPIResource):
    with_raw_response: AsyncMessagesWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncMessagesWithRawResponse(self)

    @overload
    async def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """You can create a message that has been initiated by an admin.

        The conversation
        can be either an in-app message or an email.

        > 🚧 Sending for visitors
        >
        > There can be a short delay between when a contact is created and when a
        > contact becomes available to be messaged through the API. A 404 Not Found
        > error will be returned in this case.

        This will return the Message model that has been created.

        > 🚧 Retrieving Associated Conversations
        >
        > As this is a message, there will be no conversation present until the contact
        > responds. Once they do, you will have to search for a contact's conversations
        > with the id of the message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """You can create a message that has been initiated by an admin.

        The conversation
        can be either an in-app message or an email.

        > 🚧 Sending for visitors
        >
        > There can be a short delay between when a contact is created and when a
        > contact becomes available to be messaged through the API. A 404 Not Found
        > error will be returned in this case.

        This will return the Message model that has been created.

        > 🚧 Retrieving Associated Conversations
        >
        > As this is a message, there will be no conversation present until the contact
        > responds. Once they do, you will have to search for a contact's conversations
        > with the id of the message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body"], ["body"])
    async def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        return await self._post(
            "/messages",
            body=maybe_transform(body, message_create_params.MessageCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )


class MessagesWithRawResponse:
    def __init__(self, messages: Messages) -> None:
        self.create = to_raw_response_wrapper(
            messages.create,
        )


class AsyncMessagesWithRawResponse:
    def __init__(self, messages: AsyncMessages) -> None:
        self.create = async_to_raw_response_wrapper(
            messages.create,
        )
