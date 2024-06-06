# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .content import (
    ContentResource,
    AsyncContentResource,
    ContentResourceWithRawResponse,
    AsyncContentResourceWithRawResponse,
    ContentResourceWithStreamingResponse,
    AsyncContentResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .content.content import ContentResource, AsyncContentResource

__all__ = ["DownloadResource", "AsyncDownloadResource"]


class DownloadResource(SyncAPIResource):
    @cached_property
    def content(self) -> ContentResource:
        return ContentResource(self._client)

    @cached_property
    def with_raw_response(self) -> DownloadResourceWithRawResponse:
        return DownloadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadResourceWithStreamingResponse:
        return DownloadResourceWithStreamingResponse(self)


class AsyncDownloadResource(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContentResource:
        return AsyncContentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDownloadResourceWithRawResponse:
        return AsyncDownloadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadResourceWithStreamingResponse:
        return AsyncDownloadResourceWithStreamingResponse(self)


class DownloadResourceWithRawResponse:
    def __init__(self, download: DownloadResource) -> None:
        self._download = download

    @cached_property
    def content(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self._download.content)


class AsyncDownloadResourceWithRawResponse:
    def __init__(self, download: AsyncDownloadResource) -> None:
        self._download = download

    @cached_property
    def content(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self._download.content)


class DownloadResourceWithStreamingResponse:
    def __init__(self, download: DownloadResource) -> None:
        self._download = download

    @cached_property
    def content(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self._download.content)


class AsyncDownloadResourceWithStreamingResponse:
    def __init__(self, download: AsyncDownloadResource) -> None:
        self._download = download

    @cached_property
    def content(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self._download.content)
