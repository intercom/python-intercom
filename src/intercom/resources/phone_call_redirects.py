# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional

import httpx

from ..types import PhoneSwitch, phone_call_redirect_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Intercom, AsyncIntercom

__all__ = ["PhoneCallRedirects", "AsyncPhoneCallRedirects"]


class PhoneCallRedirects(SyncAPIResource):
    with_raw_response: PhoneCallRedirectsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = PhoneCallRedirectsWithRawResponse(self)

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


class AsyncPhoneCallRedirects(AsyncAPIResource):
    with_raw_response: AsyncPhoneCallRedirectsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncPhoneCallRedirectsWithRawResponse(self)

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


class PhoneCallRedirectsWithRawResponse:
    def __init__(self, phone_call_redirects: PhoneCallRedirects) -> None:
        self.create = to_raw_response_wrapper(
            phone_call_redirects.create,
        )


class AsyncPhoneCallRedirectsWithRawResponse:
    def __init__(self, phone_call_redirects: AsyncPhoneCallRedirects) -> None:
        self.create = async_to_raw_response_wrapper(
            phone_call_redirects.create,
        )
