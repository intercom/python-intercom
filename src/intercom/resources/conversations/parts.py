# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import overload
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
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
from ..._base_client import (
    make_request_options,
)
from ...types.conversations import part_create_params
from ...types.shared.conversation import Conversation

__all__ = ["PartsResource", "AsyncPartsResource"]


class PartsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PartsResourceWithRawResponse:
        return PartsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PartsResourceWithStreamingResponse:
        return PartsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        id: str,
        *,
        admin_id: str,
        message_type: Literal["close"],
        type: Literal["admin"],
        body: str | NotGiven = NOT_GIVEN,
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
        For managing conversations you can:

        - Close a conversation
        - Snooze a conversation to reopen on a future date
        - Open a conversation which is `snoozed` or `closed`
        - Assign a conversation to an admin and/or team.

        Args:
          admin_id: The id of the admin who is performing the action.

          body: Optionally you can leave a message in the conversation to provide additional
              context to the user and other teammates.

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
        message_type: Literal["snoozed"],
        snoozed_until: int,
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
        For managing conversations you can:

        - Close a conversation
        - Snooze a conversation to reopen on a future date
        - Open a conversation which is `snoozed` or `closed`
        - Assign a conversation to an admin and/or team.

        Args:
          admin_id: The id of the admin who is performing the action.

          snoozed_until: The time you want the conversation to reopen.

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
        message_type: Literal["open"],
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
        For managing conversations you can:

        - Close a conversation
        - Snooze a conversation to reopen on a future date
        - Open a conversation which is `snoozed` or `closed`
        - Assign a conversation to an admin and/or team.

        Args:
          admin_id: The id of the admin who is performing the action.

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
        assignee_id: str,
        message_type: Literal["assignment"],
        type: Literal["admin", "team"],
        body: str | NotGiven = NOT_GIVEN,
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
        For managing conversations you can:

        - Close a conversation
        - Snooze a conversation to reopen on a future date
        - Open a conversation which is `snoozed` or `closed`
        - Assign a conversation to an admin and/or team.

        Args:
          admin_id: The id of the admin who is performing the action.

          assignee_id: The `id` of the `admin` or `team` which will be assigned the conversation. A
              conversation can be assigned both an admin and a team.\nSet `0` if you want this
              assign to no admin or team (ie. Unassigned).

          body: Optionally you can send a response in the conversation when it is assigned.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["admin_id", "message_type", "type"],
        ["admin_id", "message_type", "snoozed_until"],
        ["admin_id", "message_type"],
        ["admin_id", "assignee_id", "message_type", "type"],
    )
    def create(
        self,
        id: str,
        *,
        admin_id: str,
        message_type: Literal["close"] | Literal["snoozed"] | Literal["open"] | Literal["assignment"],
        type: Literal["admin"] | Literal["admin", "team"] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
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
        snoozed_until: int | NotGiven = NOT_GIVEN,
        assignee_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._post(
            f"/conversations/{id}/parts",
            body=maybe_transform(
                {
                    "admin_id": admin_id,
                    "message_type": message_type,
                    "type": type,
                    "body": body,
                    "snoozed_until": snoozed_until,
                    "assignee_id": assignee_id,
                },
                part_create_params.PartCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class AsyncPartsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPartsResourceWithRawResponse:
        return AsyncPartsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPartsResourceWithStreamingResponse:
        return AsyncPartsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        id: str,
        *,
        admin_id: str,
        message_type: Literal["close"],
        type: Literal["admin"],
        body: str | NotGiven = NOT_GIVEN,
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
        For managing conversations you can:

        - Close a conversation
        - Snooze a conversation to reopen on a future date
        - Open a conversation which is `snoozed` or `closed`
        - Assign a conversation to an admin and/or team.

        Args:
          admin_id: The id of the admin who is performing the action.

          body: Optionally you can leave a message in the conversation to provide additional
              context to the user and other teammates.

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
        message_type: Literal["snoozed"],
        snoozed_until: int,
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
        For managing conversations you can:

        - Close a conversation
        - Snooze a conversation to reopen on a future date
        - Open a conversation which is `snoozed` or `closed`
        - Assign a conversation to an admin and/or team.

        Args:
          admin_id: The id of the admin who is performing the action.

          snoozed_until: The time you want the conversation to reopen.

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
        message_type: Literal["open"],
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
        For managing conversations you can:

        - Close a conversation
        - Snooze a conversation to reopen on a future date
        - Open a conversation which is `snoozed` or `closed`
        - Assign a conversation to an admin and/or team.

        Args:
          admin_id: The id of the admin who is performing the action.

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
        assignee_id: str,
        message_type: Literal["assignment"],
        type: Literal["admin", "team"],
        body: str | NotGiven = NOT_GIVEN,
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
        For managing conversations you can:

        - Close a conversation
        - Snooze a conversation to reopen on a future date
        - Open a conversation which is `snoozed` or `closed`
        - Assign a conversation to an admin and/or team.

        Args:
          admin_id: The id of the admin who is performing the action.

          assignee_id: The `id` of the `admin` or `team` which will be assigned the conversation. A
              conversation can be assigned both an admin and a team.\nSet `0` if you want this
              assign to no admin or team (ie. Unassigned).

          body: Optionally you can send a response in the conversation when it is assigned.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["admin_id", "message_type", "type"],
        ["admin_id", "message_type", "snoozed_until"],
        ["admin_id", "message_type"],
        ["admin_id", "assignee_id", "message_type", "type"],
    )
    async def create(
        self,
        id: str,
        *,
        admin_id: str,
        message_type: Literal["close"] | Literal["snoozed"] | Literal["open"] | Literal["assignment"],
        type: Literal["admin"] | Literal["admin", "team"] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
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
        snoozed_until: int | NotGiven = NOT_GIVEN,
        assignee_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._post(
            f"/conversations/{id}/parts",
            body=await async_maybe_transform(
                {
                    "admin_id": admin_id,
                    "message_type": message_type,
                    "type": type,
                    "body": body,
                    "snoozed_until": snoozed_until,
                    "assignee_id": assignee_id,
                },
                part_create_params.PartCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )


class PartsResourceWithRawResponse:
    def __init__(self, parts: PartsResource) -> None:
        self._parts = parts

        self.create = to_raw_response_wrapper(
            parts.create,
        )


class AsyncPartsResourceWithRawResponse:
    def __init__(self, parts: AsyncPartsResource) -> None:
        self._parts = parts

        self.create = async_to_raw_response_wrapper(
            parts.create,
        )


class PartsResourceWithStreamingResponse:
    def __init__(self, parts: PartsResource) -> None:
        self._parts = parts

        self.create = to_streamed_response_wrapper(
            parts.create,
        )


class AsyncPartsResourceWithStreamingResponse:
    def __init__(self, parts: AsyncPartsResource) -> None:
        self._parts = parts

        self.create = async_to_streamed_response_wrapper(
            parts.create,
        )
