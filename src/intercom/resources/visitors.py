# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional, overload

import httpx

from ..types import visitor_update_params, visitor_convert_params, visitor_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    required_args,
    maybe_transform,
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
from .._base_client import (
    make_request_options,
)
from ..types.visitor import Visitor
from ..types.shared.contact import Contact
from ..types.visitor_deleted_object import VisitorDeletedObject

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Visitor]:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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

    def delete_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VisitorDeletedObject:
        """
        You can delete a single visitor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/visitors/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisitorDeletedObject,
        )

    def retrieve_by_id(
        self,
        id: str,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/visitors/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Visitor,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Visitor]:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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

    async def delete_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VisitorDeletedObject:
        """
        You can delete a single visitor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/visitors/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisitorDeletedObject,
        )

    async def retrieve_by_id(
        self,
        id: str,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/visitors/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Visitor,
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
        self.delete_by_id = to_raw_response_wrapper(
            visitors.delete_by_id,
        )
        self.retrieve_by_id = to_raw_response_wrapper(
            visitors.retrieve_by_id,
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
        self.delete_by_id = async_to_raw_response_wrapper(
            visitors.delete_by_id,
        )
        self.retrieve_by_id = async_to_raw_response_wrapper(
            visitors.retrieve_by_id,
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
        self.delete_by_id = to_streamed_response_wrapper(
            visitors.delete_by_id,
        )
        self.retrieve_by_id = to_streamed_response_wrapper(
            visitors.retrieve_by_id,
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
        self.delete_by_id = async_to_streamed_response_wrapper(
            visitors.delete_by_id,
        )
        self.retrieve_by_id = async_to_streamed_response_wrapper(
            visitors.retrieve_by_id,
        )
