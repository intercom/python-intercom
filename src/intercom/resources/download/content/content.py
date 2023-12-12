# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .data import Data, AsyncData, DataWithRawResponse, AsyncDataWithRawResponse
from ...._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ...._client import Intercom, AsyncIntercom

__all__ = ["Content", "AsyncContent"]


class Content(SyncAPIResource):
    data: Data
    with_raw_response: ContentWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.data = Data(client)
        self.with_raw_response = ContentWithRawResponse(self)


class AsyncContent(AsyncAPIResource):
    data: AsyncData
    with_raw_response: AsyncContentWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.data = AsyncData(client)
        self.with_raw_response = AsyncContentWithRawResponse(self)


class ContentWithRawResponse:
    def __init__(self, content: Content) -> None:
        self.data = DataWithRawResponse(content.data)


class AsyncContentWithRawResponse:
    def __init__(self, content: AsyncContent) -> None:
        self.data = AsyncDataWithRawResponse(content.data)
