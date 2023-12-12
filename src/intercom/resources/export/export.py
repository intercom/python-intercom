# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ...types import DataExport
from .content import (
    Content,
    AsyncContent,
    ContentWithRawResponse,
    AsyncContentWithRawResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Export", "AsyncExport"]


class Export(SyncAPIResource):
    content: Content
    with_raw_response: ExportWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.content = Content(client)
        self.with_raw_response = ExportWithRawResponse(self)

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
        return self._post(
            f"/export/cancel/{job_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExport,
        )


class AsyncExport(AsyncAPIResource):
    content: AsyncContent
    with_raw_response: AsyncExportWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.content = AsyncContent(client)
        self.with_raw_response = AsyncExportWithRawResponse(self)

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
        return await self._post(
            f"/export/cancel/{job_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExport,
        )


class ExportWithRawResponse:
    def __init__(self, export: Export) -> None:
        self.content = ContentWithRawResponse(export.content)

        self.cancel = to_raw_response_wrapper(
            export.cancel,
        )


class AsyncExportWithRawResponse:
    def __init__(self, export: AsyncExport) -> None:
        self.content = AsyncContentWithRawResponse(export.content)

        self.cancel = async_to_raw_response_wrapper(
            export.cancel,
        )
