# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, overload
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ...types.conversations import reply_create_params
from ...types.shared.conversation import Conversation

__all__ = ["ReplyResource", "AsyncReplyResource"]


class ReplyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReplyResourceWithRawResponse:
        return ReplyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReplyResourceWithStreamingResponse:
        return ReplyResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        id: Union[str, Literal["last"]],
        *,
        body: str,
        intercom_user_id: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can reply to a conversation with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the conversation to target.

          body: The text body of the comment.

          intercom_user_id: The identifier for the contact as given by Intercom.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: Union[str, Literal["last"]],
        *,
        body: str,
        email: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can reply to a conversation with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the conversation to target.

          body: The text body of the comment.

          email: The email you have defined for the user.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: Union[str, Literal["last"]],
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        user_id: str,
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can reply to a conversation with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the conversation to target.

          body: The text body of the comment.

          user_id: The external_id you have defined for the contact.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: Union[str, Literal["last"]],
        *,
        admin_id: str,
        message_type: Literal["comment", "note"],
        type: Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can reply to a conversation with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the conversation to target.

          admin_id: The id of the admin who is authoring the comment.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          body: The text body of the reply.\nNotes accept some HTML formatting.\nMust be present
              for comment and note message types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["body", "intercom_user_id", "message_type", "type"],
        ["body", "email", "message_type", "type"],
        ["body", "message_type", "type", "user_id"],
        ["admin_id", "message_type", "type"],
    )
    def create(
        self,
        id: Union[str, Literal["last"]],
        *,
        body: str | NotGiven = NOT_GIVEN,
        intercom_user_id: str | NotGiven = NOT_GIVEN,
        message_type: Literal["comment"] | Literal["comment", "note"],
        type: Literal["user"] | Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        admin_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        return self._post(
            f"/conversations/{id}/reply",
            body=maybe_transform(
                {
                    "body": body,
                    "intercom_user_id": intercom_user_id,
                    "message_type": message_type,
                    "type": type,
                    "attachment_urls": attachment_urls,
                    "email": email,
                    "user_id": user_id,
                    "admin_id": admin_id,
                },
                reply_create_params.ReplyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class AsyncReplyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReplyResourceWithRawResponse:
        return AsyncReplyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReplyResourceWithStreamingResponse:
        return AsyncReplyResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        id: Union[str, Literal["last"]],
        *,
        body: str,
        intercom_user_id: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can reply to a conversation with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the conversation to target.

          body: The text body of the comment.

          intercom_user_id: The identifier for the contact as given by Intercom.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: Union[str, Literal["last"]],
        *,
        body: str,
        email: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can reply to a conversation with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the conversation to target.

          body: The text body of the comment.

          email: The email you have defined for the user.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: Union[str, Literal["last"]],
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        user_id: str,
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can reply to a conversation with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the conversation to target.

          body: The text body of the comment.

          user_id: The external_id you have defined for the contact.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: Union[str, Literal["last"]],
        *,
        admin_id: str,
        message_type: Literal["comment", "note"],
        type: Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        You can reply to a conversation with a message from an admin or on behalf of a
        contact, or with a note for admins.

        Args:
          id: The id of the conversation to target.

          admin_id: The id of the admin who is authoring the comment.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 5
              URLs.

          body: The text body of the reply.\nNotes accept some HTML formatting.\nMust be present
              for comment and note message types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["body", "intercom_user_id", "message_type", "type"],
        ["body", "email", "message_type", "type"],
        ["body", "message_type", "type", "user_id"],
        ["admin_id", "message_type", "type"],
    )
    async def create(
        self,
        id: Union[str, Literal["last"]],
        *,
        body: str | NotGiven = NOT_GIVEN,
        intercom_user_id: str | NotGiven = NOT_GIVEN,
        message_type: Literal["comment"] | Literal["comment", "note"],
        type: Literal["user"] | Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        admin_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        return await self._post(
            f"/conversations/{id}/reply",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "intercom_user_id": intercom_user_id,
                    "message_type": message_type,
                    "type": type,
                    "attachment_urls": attachment_urls,
                    "email": email,
                    "user_id": user_id,
                    "admin_id": admin_id,
                },
                reply_create_params.ReplyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class ReplyResourceWithRawResponse:
    def __init__(self, reply: ReplyResource) -> None:
        self._reply = reply

        self.create = to_raw_response_wrapper(
            reply.create,
        )


class AsyncReplyResourceWithRawResponse:
    def __init__(self, reply: AsyncReplyResource) -> None:
        self._reply = reply

        self.create = async_to_raw_response_wrapper(
            reply.create,
        )


class ReplyResourceWithStreamingResponse:
    def __init__(self, reply: ReplyResource) -> None:
        self._reply = reply

        self.create = to_streamed_response_wrapper(
            reply.create,
        )


class AsyncReplyResourceWithStreamingResponse:
    def __init__(self, reply: AsyncReplyResource) -> None:
        self._reply = reply

        self.create = async_to_streamed_response_wrapper(
            reply.create,
        )
