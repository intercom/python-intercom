# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, overload
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    required_args,
    maybe_transform,
    strip_not_given,
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
from ..._base_client import make_request_options
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
        id: str,
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        created_at: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
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
          body: The text body of the comment.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 10
              URLs.

          created_at: The time the reply was created. If not provided, the current time will be used.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        created_at: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
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
          body: The text body of the comment.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 10
              URLs.

          created_at: The time the reply was created. If not provided, the current time will be used.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        created_at: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
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
          body: The text body of the comment.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 10
              URLs.

          created_at: The time the reply was created. If not provided, the current time will be used.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        id: str,
        *,
        admin_id: str,
        message_type: Literal["comment", "note"],
        type: Literal["admin"],
        attachment_files: Iterable[reply_create_params.AdminReplyConversationRequestAttachmentFile]
        | NotGiven = NOT_GIVEN,
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        created_at: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
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
          admin_id: The id of the admin who is authoring the comment.

          attachment_files: A list of files that will be added as attachments. You can include up to 10
              files

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 10
              URLs.

          body: The text body of the reply. Notes accept some HTML formatting. Must be present
              for comment and note message types.

          created_at: The time the reply was created. If not provided, the current time will be used.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body", "message_type", "type"], ["admin_id", "message_type", "type"])
    def create(
        self,
        id: str,
        *,
        body: str | NotGiven = NOT_GIVEN,
        message_type: Literal["comment"] | Literal["comment", "note"],
        type: Literal["user"] | Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        created_at: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        admin_id: str | NotGiven = NOT_GIVEN,
        attachment_files: Iterable[reply_create_params.AdminReplyConversationRequestAttachmentFile]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._post(
            f"/conversations/{id}/reply",
            body=maybe_transform(
                {
                    "body": body,
                    "message_type": message_type,
                    "type": type,
                    "attachment_urls": attachment_urls,
                    "created_at": created_at,
                    "admin_id": admin_id,
                    "attachment_files": attachment_files,
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
        id: str,
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        created_at: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
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
          body: The text body of the comment.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 10
              URLs.

          created_at: The time the reply was created. If not provided, the current time will be used.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        created_at: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
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
          body: The text body of the comment.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 10
              URLs.

          created_at: The time the reply was created. If not provided, the current time will be used.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        body: str,
        message_type: Literal["comment"],
        type: Literal["user"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        created_at: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
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
          body: The text body of the comment.

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 10
              URLs.

          created_at: The time the reply was created. If not provided, the current time will be used.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        id: str,
        *,
        admin_id: str,
        message_type: Literal["comment", "note"],
        type: Literal["admin"],
        attachment_files: Iterable[reply_create_params.AdminReplyConversationRequestAttachmentFile]
        | NotGiven = NOT_GIVEN,
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        created_at: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
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
          admin_id: The id of the admin who is authoring the comment.

          attachment_files: A list of files that will be added as attachments. You can include up to 10
              files

          attachment_urls: A list of image URLs that will be added as attachments. You can include up to 10
              URLs.

          body: The text body of the reply. Notes accept some HTML formatting. Must be present
              for comment and note message types.

          created_at: The time the reply was created. If not provided, the current time will be used.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body", "message_type", "type"], ["admin_id", "message_type", "type"])
    async def create(
        self,
        id: str,
        *,
        body: str | NotGiven = NOT_GIVEN,
        message_type: Literal["comment"] | Literal["comment", "note"],
        type: Literal["user"] | Literal["admin"],
        attachment_urls: List[str] | NotGiven = NOT_GIVEN,
        created_at: int | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        admin_id: str | NotGiven = NOT_GIVEN,
        attachment_files: Iterable[reply_create_params.AdminReplyConversationRequestAttachmentFile]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._post(
            f"/conversations/{id}/reply",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "message_type": message_type,
                    "type": type,
                    "attachment_urls": attachment_urls,
                    "created_at": created_at,
                    "admin_id": admin_id,
                    "attachment_files": attachment_files,
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
