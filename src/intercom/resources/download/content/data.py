# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...._base_client import make_request_options

if TYPE_CHECKING:
    from ...._client import Intercom, AsyncIntercom

__all__ = ["Data", "AsyncData"]


class Data(SyncAPIResource):
    with_raw_response: DataWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = DataWithRawResponse(self)

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
    ) -> None:
        """
        When a job has a status of complete, and thus a filled download_url, you can
        download your data by hitting that provided URL, formatted like so:
        https://api.intercom.io/download/content/data/xyz1234.

        Your exported message data will be streamed continuously back down to you in a
        gzipped CSV format.

        > 📘 Octet header required
        >
        > You will have to specify the header Accept: `application/octet-stream` when
        > hitting this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/download/content/data/{job_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncData(AsyncAPIResource):
    with_raw_response: AsyncDataWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncDataWithRawResponse(self)

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
    ) -> None:
        """
        When a job has a status of complete, and thus a filled download_url, you can
        download your data by hitting that provided URL, formatted like so:
        https://api.intercom.io/download/content/data/xyz1234.

        Your exported message data will be streamed continuously back down to you in a
        gzipped CSV format.

        > 📘 Octet header required
        >
        > You will have to specify the header Accept: `application/octet-stream` when
        > hitting this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/download/content/data/{job_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DataWithRawResponse:
    def __init__(self, data: Data) -> None:
        self.retrieve = to_raw_response_wrapper(
            data.retrieve,
        )


class AsyncDataWithRawResponse:
    def __init__(self, data: AsyncData) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            data.retrieve,
        )
