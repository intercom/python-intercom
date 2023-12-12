# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .content import (
    Content,
    AsyncContent,
    ContentWithRawResponse,
    AsyncContentWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Download", "AsyncDownload"]


class Download(SyncAPIResource):
    content: Content
    with_raw_response: DownloadWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.content = Content(client)
        self.with_raw_response = DownloadWithRawResponse(self)


class AsyncDownload(AsyncAPIResource):
    content: AsyncContent
    with_raw_response: AsyncDownloadWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.content = AsyncContent(client)
        self.with_raw_response = AsyncDownloadWithRawResponse(self)


class DownloadWithRawResponse:
    def __init__(self, download: Download) -> None:
        self.content = ContentWithRawResponse(download.content)


class AsyncDownloadWithRawResponse:
    def __init__(self, download: AsyncDownload) -> None:
        self.content = AsyncContentWithRawResponse(download.content)
