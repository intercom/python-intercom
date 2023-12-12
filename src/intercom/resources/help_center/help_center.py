# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..._resource import SyncAPIResource, AsyncAPIResource
from .collections import (
    Collections,
    AsyncCollections,
    CollectionsWithRawResponse,
    AsyncCollectionsWithRawResponse,
)
from .help_centers import (
    HelpCenters,
    AsyncHelpCenters,
    HelpCentersWithRawResponse,
    AsyncHelpCentersWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["HelpCenter", "AsyncHelpCenter"]


class HelpCenter(SyncAPIResource):
    collections: Collections
    help_centers: HelpCenters
    with_raw_response: HelpCenterWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.collections = Collections(client)
        self.help_centers = HelpCenters(client)
        self.with_raw_response = HelpCenterWithRawResponse(self)


class AsyncHelpCenter(AsyncAPIResource):
    collections: AsyncCollections
    help_centers: AsyncHelpCenters
    with_raw_response: AsyncHelpCenterWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.collections = AsyncCollections(client)
        self.help_centers = AsyncHelpCenters(client)
        self.with_raw_response = AsyncHelpCenterWithRawResponse(self)


class HelpCenterWithRawResponse:
    def __init__(self, help_center: HelpCenter) -> None:
        self.collections = CollectionsWithRawResponse(help_center.collections)
        self.help_centers = HelpCentersWithRawResponse(help_center.help_centers)


class AsyncHelpCenterWithRawResponse:
    def __init__(self, help_center: AsyncHelpCenter) -> None:
        self.collections = AsyncCollectionsWithRawResponse(help_center.collections)
        self.help_centers = AsyncHelpCentersWithRawResponse(help_center.help_centers)
