# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional, overload
from typing_extensions import Literal

import httpx

from ..types import visitor_update_params, visitor_convert_params, visitor_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    is_given,
    required_args,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.visitor import Visitor
from ..types.shared.contact import Contact

__all__ = ["VisitorsResource", "AsyncVisitorsResource"]


class VisitorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VisitorsResourceWithRawResponse:
        return VisitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VisitorsResourceWithStreamingResponse:
        return VisitorsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        user_id: str,
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
    ) -> Optional[Visitor]:
        """
        You can fetch the details of a single visitor.

        Args:
          user_id: The user_id of the Visitor you want to retrieve.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._get(
            "/visitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"user_id": user_id}, visitor_retrieve_params.VisitorRetrieveParams),
            ),
            cast_to=Visitor,
        )

    @overload
    def update(
        self,
        *,
        body: object,
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
    ) -> Optional[Visitor]:
        """
        Sending a PUT request to `/visitors` will result in an update of an existing
        Visitor.

        **Option 1.** You can update a visitor by passing in the `user_id` of the
        visitor in the Request body.

        **Option 2.** You can update a visitor by passing in the `id` of the visitor in
        the Request body.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        body: object,
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
    ) -> Optional[Visitor]:
        """
        Sending a PUT request to `/visitors` will result in an update of an existing
        Visitor.

        **Option 1.** You can update a visitor by passing in the `user_id` of the
        visitor in the Request body.

        **Option 2.** You can update a visitor by passing in the `id` of the visitor in
        the Request body.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body"])
    def update(
        self,
        *,
        body: object,
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
    ) -> Optional[Visitor]:
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._put(
            "/visitors",
            body=maybe_transform(body, visitor_update_params.VisitorUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Visitor,
        )

    def convert(
        self,
        *,
        type: str,
        user: visitor_convert_params.User,
        visitor: visitor_convert_params.Visitor,
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
    ) -> Contact:
        """
        You can merge a Visitor to a Contact of role type `lead` or `user`.

        > 📘 What happens upon a visitor being converted?
        >
        > If the User exists, then the Visitor will be merged into it, the Visitor
        > deleted and the User returned. If the User does not exist, the Visitor will be
        > converted to a User, with the User identifiers replacing it's Visitor
        > identifiers.

        Args:
          type: Represents the role of the Contact model. Accepts `lead` or `user`.

          user: The unique identifiers retained after converting or merging.

          visitor: The unique identifiers to convert a single Visitor.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return self._post(
            "/visitors/convert",
            body=maybe_transform(
                {
                    "type": type,
                    "user": user,
                    "visitor": visitor,
                },
                visitor_convert_params.VisitorConvertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )


class AsyncVisitorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVisitorsResourceWithRawResponse:
        return AsyncVisitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVisitorsResourceWithStreamingResponse:
        return AsyncVisitorsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        user_id: str,
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
    ) -> Optional[Visitor]:
        """
        You can fetch the details of a single visitor.

        Args:
          user_id: The user_id of the Visitor you want to retrieve.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/visitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"user_id": user_id}, visitor_retrieve_params.VisitorRetrieveParams),
            ),
            cast_to=Visitor,
        )

    @overload
    async def update(
        self,
        *,
        body: object,
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
    ) -> Optional[Visitor]:
        """
        Sending a PUT request to `/visitors` will result in an update of an existing
        Visitor.

        **Option 1.** You can update a visitor by passing in the `user_id` of the
        visitor in the Request body.

        **Option 2.** You can update a visitor by passing in the `id` of the visitor in
        the Request body.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        body: object,
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
    ) -> Optional[Visitor]:
        """
        Sending a PUT request to `/visitors` will result in an update of an existing
        Visitor.

        **Option 1.** You can update a visitor by passing in the `user_id` of the
        visitor in the Request body.

        **Option 2.** You can update a visitor by passing in the `id` of the visitor in
        the Request body.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body"])
    async def update(
        self,
        *,
        body: object,
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
    ) -> Optional[Visitor]:
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._put(
            "/visitors",
            body=await async_maybe_transform(body, visitor_update_params.VisitorUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Visitor,
        )

    async def convert(
        self,
        *,
        type: str,
        user: visitor_convert_params.User,
        visitor: visitor_convert_params.Visitor,
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
    ) -> Contact:
        """
        You can merge a Visitor to a Contact of role type `lead` or `user`.

        > 📘 What happens upon a visitor being converted?
        >
        > If the User exists, then the Visitor will be merged into it, the Visitor
        > deleted and the User returned. If the User does not exist, the Visitor will be
        > converted to a User, with the User identifiers replacing it's Visitor
        > identifiers.

        Args:
          type: Represents the role of the Contact model. Accepts `lead` or `user`.

          user: The unique identifiers retained after converting or merging.

          visitor: The unique identifiers to convert a single Visitor.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Intercom-Version": str(intercom_version) if is_given(intercom_version) else NOT_GIVEN}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/visitors/convert",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "user": user,
                    "visitor": visitor,
                },
                visitor_convert_params.VisitorConvertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )


class VisitorsResourceWithRawResponse:
    def __init__(self, visitors: VisitorsResource) -> None:
        self._visitors = visitors

        self.retrieve = to_raw_response_wrapper(
            visitors.retrieve,
        )
        self.update = to_raw_response_wrapper(
            visitors.update,
        )
        self.convert = to_raw_response_wrapper(
            visitors.convert,
        )


class AsyncVisitorsResourceWithRawResponse:
    def __init__(self, visitors: AsyncVisitorsResource) -> None:
        self._visitors = visitors

        self.retrieve = async_to_raw_response_wrapper(
            visitors.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            visitors.update,
        )
        self.convert = async_to_raw_response_wrapper(
            visitors.convert,
        )


class VisitorsResourceWithStreamingResponse:
    def __init__(self, visitors: VisitorsResource) -> None:
        self._visitors = visitors

        self.retrieve = to_streamed_response_wrapper(
            visitors.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            visitors.update,
        )
        self.convert = to_streamed_response_wrapper(
            visitors.convert,
        )


class AsyncVisitorsResourceWithStreamingResponse:
    def __init__(self, visitors: AsyncVisitorsResource) -> None:
        self._visitors = visitors

        self.retrieve = async_to_streamed_response_wrapper(
            visitors.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            visitors.update,
        )
        self.convert = async_to_streamed_response_wrapper(
            visitors.convert,
        )
