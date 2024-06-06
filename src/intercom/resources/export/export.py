# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .content import (
    ContentResource,
    AsyncContentResource,
    ContentResourceWithRawResponse,
    AsyncContentResourceWithRawResponse,
    ContentResourceWithStreamingResponse,
    AsyncContentResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .content.content import ContentResource, AsyncContentResource
from ...types.data_export import DataExport

__all__ = ["ExportResource", "AsyncExportResource"]


class ExportResource(SyncAPIResource):
    @cached_property
    def content(self) -> ContentResource:
        return ContentResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExportResourceWithRawResponse:
        return ExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportResourceWithStreamingResponse:
        return ExportResourceWithStreamingResponse(self)

    def cancel(
        self,
        job_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataExport:
        """
        You can cancel your job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_identifier:
            raise ValueError(f"Expected a non-empty value for `job_identifier` but received {job_identifier!r}")
        return self._post(
            f"/export/cancel/{job_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExport,
        )


class AsyncExportResource(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContentResource:
        return AsyncContentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExportResourceWithRawResponse:
        return AsyncExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportResourceWithStreamingResponse:
        return AsyncExportResourceWithStreamingResponse(self)

    async def cancel(
        self,
        job_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataExport:
        """
        You can cancel your job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_identifier:
            raise ValueError(f"Expected a non-empty value for `job_identifier` but received {job_identifier!r}")
        return await self._post(
            f"/export/cancel/{job_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExport,
        )


class ExportResourceWithRawResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.cancel = to_raw_response_wrapper(
            export.cancel,
        )

    @cached_property
    def content(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self._export.content)


class AsyncExportResourceWithRawResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.cancel = async_to_raw_response_wrapper(
            export.cancel,
        )

    @cached_property
    def content(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self._export.content)


class ExportResourceWithStreamingResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.cancel = to_streamed_response_wrapper(
            export.cancel,
        )

    @cached_property
    def content(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self._export.content)


class AsyncExportResourceWithStreamingResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.cancel = async_to_streamed_response_wrapper(
            export.cancel,
        )

    @cached_property
    def content(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self._export.content)
