# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ...types.ai import (
    ContentImportSource,
    ContentImportSourcesList,
    content_import_source_create_params,
    content_import_source_update_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["ContentImportSources", "AsyncContentImportSources"]


class ContentImportSources(SyncAPIResource):
    with_raw_response: ContentImportSourcesWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = ContentImportSourcesWithRawResponse(self)

    def create(
        self,
        *,
        sync_behavior: Literal["api"],
        url: str,
        status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentImportSource:
        """
        You can create a new content import source by sending a POST request to this
        endpoint.

        Args:
          sync_behavior: If you intend to create or update External Pages via the API, this should be set
              to `api`.

          url: The URL of the content import source.

          status: The status of the content import source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/content_import_sources",
            body=maybe_transform(
                {
                    "sync_behavior": sync_behavior,
                    "url": url,
                    "status": status,
                },
                content_import_source_create_params.ContentImportSourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentImportSource,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentImportSource:
        """
        Retrieve a content import source

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/ai/content_import_sources/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentImportSource,
        )

    def update(
        self,
        id: str,
        *,
        sync_behavior: Literal["api", "automated", "manual"],
        url: str,
        status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentImportSource:
        """
        You can update an existing content import source.

        Args:
          sync_behavior: If you intend to create or update External Pages via the API, this should be set
              to `api`. You can not change the value to or from api.

          url: The URL of the content import source. This may only be different from the
              existing value if the sync behavior is API.

          status: The status of the content import source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/ai/content_import_sources/{id}",
            body=maybe_transform(
                {
                    "sync_behavior": sync_behavior,
                    "url": url,
                    "status": status,
                },
                content_import_source_update_params.ContentImportSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentImportSource,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentImportSourcesList:
        """You can retrieve a list of all content import sources for a workspace."""
        return self._get(
            "/ai/content_import_sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentImportSourcesList,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        You can delete a content import source by making a DELETE request this endpoint.
        This will also delete all external pages that were imported from this source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/ai/content_import_sources/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncContentImportSources(AsyncAPIResource):
    with_raw_response: AsyncContentImportSourcesWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncContentImportSourcesWithRawResponse(self)

    async def create(
        self,
        *,
        sync_behavior: Literal["api"],
        url: str,
        status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentImportSource:
        """
        You can create a new content import source by sending a POST request to this
        endpoint.

        Args:
          sync_behavior: If you intend to create or update External Pages via the API, this should be set
              to `api`.

          url: The URL of the content import source.

          status: The status of the content import source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/content_import_sources",
            body=maybe_transform(
                {
                    "sync_behavior": sync_behavior,
                    "url": url,
                    "status": status,
                },
                content_import_source_create_params.ContentImportSourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentImportSource,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentImportSource:
        """
        Retrieve a content import source

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/ai/content_import_sources/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentImportSource,
        )

    async def update(
        self,
        id: str,
        *,
        sync_behavior: Literal["api", "automated", "manual"],
        url: str,
        status: Literal["active", "deactivated"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentImportSource:
        """
        You can update an existing content import source.

        Args:
          sync_behavior: If you intend to create or update External Pages via the API, this should be set
              to `api`. You can not change the value to or from api.

          url: The URL of the content import source. This may only be different from the
              existing value if the sync behavior is API.

          status: The status of the content import source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/ai/content_import_sources/{id}",
            body=maybe_transform(
                {
                    "sync_behavior": sync_behavior,
                    "url": url,
                    "status": status,
                },
                content_import_source_update_params.ContentImportSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentImportSource,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentImportSourcesList:
        """You can retrieve a list of all content import sources for a workspace."""
        return await self._get(
            "/ai/content_import_sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentImportSourcesList,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        You can delete a content import source by making a DELETE request this endpoint.
        This will also delete all external pages that were imported from this source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/ai/content_import_sources/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ContentImportSourcesWithRawResponse:
    def __init__(self, content_import_sources: ContentImportSources) -> None:
        self.create = to_raw_response_wrapper(
            content_import_sources.create,
        )
        self.retrieve = to_raw_response_wrapper(
            content_import_sources.retrieve,
        )
        self.update = to_raw_response_wrapper(
            content_import_sources.update,
        )
        self.list = to_raw_response_wrapper(
            content_import_sources.list,
        )
        self.delete = to_raw_response_wrapper(
            content_import_sources.delete,
        )


class AsyncContentImportSourcesWithRawResponse:
    def __init__(self, content_import_sources: AsyncContentImportSources) -> None:
        self.create = async_to_raw_response_wrapper(
            content_import_sources.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            content_import_sources.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            content_import_sources.update,
        )
        self.list = async_to_raw_response_wrapper(
            content_import_sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            content_import_sources.delete,
        )
