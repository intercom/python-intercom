# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..._resource import SyncAPIResource, AsyncAPIResource
from .external_pages import (
    ExternalPages,
    AsyncExternalPages,
    ExternalPagesWithRawResponse,
    AsyncExternalPagesWithRawResponse,
)
from .content_import_sources import (
    ContentImportSources,
    AsyncContentImportSources,
    ContentImportSourcesWithRawResponse,
    AsyncContentImportSourcesWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["AI", "AsyncAI"]


class AI(SyncAPIResource):
    content_import_sources: ContentImportSources
    external_pages: ExternalPages
    with_raw_response: AIWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.content_import_sources = ContentImportSources(client)
        self.external_pages = ExternalPages(client)
        self.with_raw_response = AIWithRawResponse(self)


class AsyncAI(AsyncAPIResource):
    content_import_sources: AsyncContentImportSources
    external_pages: AsyncExternalPages
    with_raw_response: AsyncAIWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.content_import_sources = AsyncContentImportSources(client)
        self.external_pages = AsyncExternalPages(client)
        self.with_raw_response = AsyncAIWithRawResponse(self)


class AIWithRawResponse:
    def __init__(self, ai: AI) -> None:
        self.content_import_sources = ContentImportSourcesWithRawResponse(ai.content_import_sources)
        self.external_pages = ExternalPagesWithRawResponse(ai.external_pages)


class AsyncAIWithRawResponse:
    def __init__(self, ai: AsyncAI) -> None:
        self.content_import_sources = AsyncContentImportSourcesWithRawResponse(ai.content_import_sources)
        self.external_pages = AsyncExternalPagesWithRawResponse(ai.external_pages)
