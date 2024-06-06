# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.data_export import DataExport

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataResourceWithRawResponse:
        return DataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataResourceWithStreamingResponse:
        return DataResourceWithStreamingResponse(self)

    def retrieve(
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
        You can view the status of your job by sending a `GET` request to the URL
        `https://api.intercom.io/export/content/data/{job_identifier}` - the
        `{job_identifier}` is the value returned in the response when you first created
        the export job. More on it can be seen in the Export Job Model.

        > 🚧 Jobs expire after two days All jobs that have completed processing (and are
        > thus available to download from the provided URL) will have an expiry limit of
        > two days from when the export ob completed. After this, the data will no
        > longer be available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_identifier:
            raise ValueError(f"Expected a non-empty value for `job_identifier` but received {job_identifier!r}")
        return self._get(
            f"/export/content/data/{job_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExport,
        )


class AsyncDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataResourceWithRawResponse:
        return AsyncDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataResourceWithStreamingResponse:
        return AsyncDataResourceWithStreamingResponse(self)

    async def retrieve(
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
        You can view the status of your job by sending a `GET` request to the URL
        `https://api.intercom.io/export/content/data/{job_identifier}` - the
        `{job_identifier}` is the value returned in the response when you first created
        the export job. More on it can be seen in the Export Job Model.

        > 🚧 Jobs expire after two days All jobs that have completed processing (and are
        > thus available to download from the provided URL) will have an expiry limit of
        > two days from when the export ob completed. After this, the data will no
        > longer be available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_identifier:
            raise ValueError(f"Expected a non-empty value for `job_identifier` but received {job_identifier!r}")
        return await self._get(
            f"/export/content/data/{job_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExport,
        )


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.retrieve = to_raw_response_wrapper(
            data.retrieve,
        )


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.retrieve = async_to_raw_response_wrapper(
            data.retrieve,
        )


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.retrieve = to_streamed_response_wrapper(
            data.retrieve,
        )


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.retrieve = async_to_streamed_response_wrapper(
            data.retrieve,
        )
