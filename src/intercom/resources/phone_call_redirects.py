# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import phone_call_redirect_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
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
from ..types.phone_switch import PhoneSwitch

__all__ = ["PhoneCallRedirectsResource", "AsyncPhoneCallRedirectsResource"]


class PhoneCallRedirectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneCallRedirectsResourceWithRawResponse:
        return PhoneCallRedirectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneCallRedirectsResourceWithStreamingResponse:
        return PhoneCallRedirectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        phone: str,
        custom_attributes: Dict[str, phone_call_redirect_create_params.CustomAttributes] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PhoneSwitch]:
        """You can use the API to deflect phone calls to the Intercom Messenger.

        Calling
        this endpoint will send an SMS with a link to the Messenger to the phone number
        specified.

        If custom attributes are specified, they will be added to the user or lead's
        custom data attributes.

        Args:
          phone: Phone number in E.164 format, that will receive the SMS to continue the
              conversation in the Messenger.

          custom_attributes: An object containing the different custom attributes associated to the
              conversation as key-value pairs. For relationship attributes the value will be a
              list of custom object instance models.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/phone_call_redirects",
            body=maybe_transform(
                {
                    "phone": phone,
                    "custom_attributes": custom_attributes,
                },
                phone_call_redirect_create_params.PhoneCallRedirectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneSwitch,
        )


class AsyncPhoneCallRedirectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneCallRedirectsResourceWithRawResponse:
        return AsyncPhoneCallRedirectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneCallRedirectsResourceWithStreamingResponse:
        return AsyncPhoneCallRedirectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        phone: str,
        custom_attributes: Dict[str, phone_call_redirect_create_params.CustomAttributes] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PhoneSwitch]:
        """You can use the API to deflect phone calls to the Intercom Messenger.

        Calling
        this endpoint will send an SMS with a link to the Messenger to the phone number
        specified.

        If custom attributes are specified, they will be added to the user or lead's
        custom data attributes.

        Args:
          phone: Phone number in E.164 format, that will receive the SMS to continue the
              conversation in the Messenger.

          custom_attributes: An object containing the different custom attributes associated to the
              conversation as key-value pairs. For relationship attributes the value will be a
              list of custom object instance models.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/phone_call_redirects",
            body=await async_maybe_transform(
                {
                    "phone": phone,
                    "custom_attributes": custom_attributes,
                },
                phone_call_redirect_create_params.PhoneCallRedirectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneSwitch,
        )


class PhoneCallRedirectsResourceWithRawResponse:
    def __init__(self, phone_call_redirects: PhoneCallRedirectsResource) -> None:
        self._phone_call_redirects = phone_call_redirects

        self.create = to_raw_response_wrapper(
            phone_call_redirects.create,
        )


class AsyncPhoneCallRedirectsResourceWithRawResponse:
    def __init__(self, phone_call_redirects: AsyncPhoneCallRedirectsResource) -> None:
        self._phone_call_redirects = phone_call_redirects

        self.create = async_to_raw_response_wrapper(
            phone_call_redirects.create,
        )


class PhoneCallRedirectsResourceWithStreamingResponse:
    def __init__(self, phone_call_redirects: PhoneCallRedirectsResource) -> None:
        self._phone_call_redirects = phone_call_redirects

        self.create = to_streamed_response_wrapper(
            phone_call_redirects.create,
        )


class AsyncPhoneCallRedirectsResourceWithStreamingResponse:
    def __init__(self, phone_call_redirects: AsyncPhoneCallRedirectsResource) -> None:
        self._phone_call_redirects = phone_call_redirects

        self.create = async_to_streamed_response_wrapper(
            phone_call_redirects.create,
        )
