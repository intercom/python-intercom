# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..types import DataExport, data_export_content_data_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Intercom, AsyncIntercom

__all__ = ["DataExports", "AsyncDataExports"]


class DataExports(SyncAPIResource):
    with_raw_response: DataExportsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = DataExportsWithRawResponse(self)

    def content_data(
        self,
        *,
        created_at_after: int,
        created_at_before: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataExport:
        """
        To create your export job, you need to send a `POST` request to the export
        endpoint `https://api.intercom.io/export/content/data`.

        The only parameters you need to provide are the range of dates that you want
        exported.

        > 🚧 Limit of one active job
        >
        > You can only have one active job per workspace. You will receive a HTTP status
        > code of 429 with the message Exceeded rate limit of 1 pending message data
        > export jobs if you attempt to create a second concurrent job.

        > ❗️ Updated_at not included
        >
        > It should be noted that the timeframe only includes messages sent during the
        > time period and not messages that were only updated during this period. For
        > example, if a message was updated yesterday but sent two days ago, you would
        > need to set the created_at_after date before the message was sent to include
        > that in your retrieval job.

        > 📘 Date ranges are inclusive
        >
        > Requesting data for 2018-06-01 until 2018-06-30 will get all data for those
        > days including those specified - e.g. 2018-06-01 00:00:00 until 2018-06-30
        > 23:59:99.

        Args:
          created_at_after: The start date that you request data for. It must be formatted as a unix
              timestamp.

          created_at_before: The end date that you request data for. It must be formatted as a unix
              timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/export/content/data",
            body=maybe_transform(
                {
                    "created_at_after": created_at_after,
                    "created_at_before": created_at_before,
                },
                data_export_content_data_params.DataExportContentDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExport,
        )


class AsyncDataExports(AsyncAPIResource):
    with_raw_response: AsyncDataExportsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncDataExportsWithRawResponse(self)

    async def content_data(
        self,
        *,
        created_at_after: int,
        created_at_before: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataExport:
        """
        To create your export job, you need to send a `POST` request to the export
        endpoint `https://api.intercom.io/export/content/data`.

        The only parameters you need to provide are the range of dates that you want
        exported.

        > 🚧 Limit of one active job
        >
        > You can only have one active job per workspace. You will receive a HTTP status
        > code of 429 with the message Exceeded rate limit of 1 pending message data
        > export jobs if you attempt to create a second concurrent job.

        > ❗️ Updated_at not included
        >
        > It should be noted that the timeframe only includes messages sent during the
        > time period and not messages that were only updated during this period. For
        > example, if a message was updated yesterday but sent two days ago, you would
        > need to set the created_at_after date before the message was sent to include
        > that in your retrieval job.

        > 📘 Date ranges are inclusive
        >
        > Requesting data for 2018-06-01 until 2018-06-30 will get all data for those
        > days including those specified - e.g. 2018-06-01 00:00:00 until 2018-06-30
        > 23:59:99.

        Args:
          created_at_after: The start date that you request data for. It must be formatted as a unix
              timestamp.

          created_at_before: The end date that you request data for. It must be formatted as a unix
              timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/export/content/data",
            body=maybe_transform(
                {
                    "created_at_after": created_at_after,
                    "created_at_before": created_at_before,
                },
                data_export_content_data_params.DataExportContentDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExport,
        )


class DataExportsWithRawResponse:
    def __init__(self, data_exports: DataExports) -> None:
        self.content_data = to_raw_response_wrapper(
            data_exports.content_data,
        )


class AsyncDataExportsWithRawResponse:
    def __init__(self, data_exports: AsyncDataExports) -> None:
        self.content_data = async_to_raw_response_wrapper(
            data_exports.content_data,
        )
