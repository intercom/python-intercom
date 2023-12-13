# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List
from typing_extensions import Literal

import httpx

from ..types import (
    DataAttribute,
    DataAttributeList,
    data_attribute_list_params,
    data_attribute_create_params,
    data_attribute_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Intercom, AsyncIntercom

__all__ = ["DataAttributes", "AsyncDataAttributes"]


class DataAttributes(SyncAPIResource):
    with_raw_response: DataAttributesWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = DataAttributesWithRawResponse(self)

    def create(
        self,
        *,
        data_type: Literal["string", "integer", "float", "boolean", "datetime", "date"],
        model: Literal["contact", "company"],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        options: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataAttribute:
        """
        You can create a data attributes for a `contact` or a `company`.

        Args:
          data_type: The type of data stored for this attribute.

          model: The model that the data attribute belongs to.

          name: The name of the data attribute.

          description: The readable description you see in the UI for the attribute.

          options: To create list attributes. Provide a set of hashes with `value` as the key of
              the options you want to make. `data_type` must be `string`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data_attributes",
            body=maybe_transform(
                {
                    "data_type": data_type,
                    "model": model,
                    "name": name,
                    "description": description,
                    "options": options,
                },
                data_attribute_create_params.DataAttributeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataAttribute,
        )

    def update(
        self,
        id: int,
        *,
        archived: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        options: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataAttribute:
        """
        You can update a data attribute.

        > 🚧 Updating the data type is not possible
        >
        > It is currently a dangerous action to execute changing a data attribute's type
        > via the API. You will need to update the type via the UI instead.

        Args:
          archived: Whether the attribute is to be archived or not.

          description: The readable description you see in the UI for the attribute.

          options: To create list attributes. Provide a set of hashes with `value` as the key of
              the options you want to make. `data_type` must be `string`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/data_attributes/{id}",
            body=maybe_transform(
                {
                    "archived": archived,
                    "description": description,
                    "options": options,
                },
                data_attribute_update_params.DataAttributeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataAttribute,
        )

    def list(
        self,
        *,
        include_archived: bool | NotGiven = NOT_GIVEN,
        model: Literal["contact", "company", "conversation"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataAttributeList:
        """
        You can fetch a list of all data attributes belonging to a workspace for
        contacts, companies or conversations.

        Args:
          include_archived: Include archived attributes in the list. By default we return only non archived
              data attributes.

          model: Specify the data attribute model to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/data_attributes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_archived": include_archived,
                        "model": model,
                    },
                    data_attribute_list_params.DataAttributeListParams,
                ),
            ),
            cast_to=DataAttributeList,
        )


class AsyncDataAttributes(AsyncAPIResource):
    with_raw_response: AsyncDataAttributesWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncDataAttributesWithRawResponse(self)

    async def create(
        self,
        *,
        data_type: Literal["string", "integer", "float", "boolean", "datetime", "date"],
        model: Literal["contact", "company"],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        options: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataAttribute:
        """
        You can create a data attributes for a `contact` or a `company`.

        Args:
          data_type: The type of data stored for this attribute.

          model: The model that the data attribute belongs to.

          name: The name of the data attribute.

          description: The readable description you see in the UI for the attribute.

          options: To create list attributes. Provide a set of hashes with `value` as the key of
              the options you want to make. `data_type` must be `string`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data_attributes",
            body=maybe_transform(
                {
                    "data_type": data_type,
                    "model": model,
                    "name": name,
                    "description": description,
                    "options": options,
                },
                data_attribute_create_params.DataAttributeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataAttribute,
        )

    async def update(
        self,
        id: int,
        *,
        archived: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        options: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataAttribute:
        """
        You can update a data attribute.

        > 🚧 Updating the data type is not possible
        >
        > It is currently a dangerous action to execute changing a data attribute's type
        > via the API. You will need to update the type via the UI instead.

        Args:
          archived: Whether the attribute is to be archived or not.

          description: The readable description you see in the UI for the attribute.

          options: To create list attributes. Provide a set of hashes with `value` as the key of
              the options you want to make. `data_type` must be `string`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/data_attributes/{id}",
            body=maybe_transform(
                {
                    "archived": archived,
                    "description": description,
                    "options": options,
                },
                data_attribute_update_params.DataAttributeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataAttribute,
        )

    async def list(
        self,
        *,
        include_archived: bool | NotGiven = NOT_GIVEN,
        model: Literal["contact", "company", "conversation"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataAttributeList:
        """
        You can fetch a list of all data attributes belonging to a workspace for
        contacts, companies or conversations.

        Args:
          include_archived: Include archived attributes in the list. By default we return only non archived
              data attributes.

          model: Specify the data attribute model to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/data_attributes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_archived": include_archived,
                        "model": model,
                    },
                    data_attribute_list_params.DataAttributeListParams,
                ),
            ),
            cast_to=DataAttributeList,
        )


class DataAttributesWithRawResponse:
    def __init__(self, data_attributes: DataAttributes) -> None:
        self.create = to_raw_response_wrapper(
            data_attributes.create,
        )
        self.update = to_raw_response_wrapper(
            data_attributes.update,
        )
        self.list = to_raw_response_wrapper(
            data_attributes.list,
        )


class AsyncDataAttributesWithRawResponse:
    def __init__(self, data_attributes: AsyncDataAttributes) -> None:
        self.create = async_to_raw_response_wrapper(
            data_attributes.create,
        )
        self.update = async_to_raw_response_wrapper(
            data_attributes.update,
        )
        self.list = async_to_raw_response_wrapper(
            data_attributes.list,
        )
