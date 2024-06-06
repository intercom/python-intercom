# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .collections import (
    CollectionsResource,
    AsyncCollectionsResource,
    CollectionsResourceWithRawResponse,
    AsyncCollectionsResourceWithRawResponse,
    CollectionsResourceWithStreamingResponse,
    AsyncCollectionsResourceWithStreamingResponse,
)
from .help_centers import (
    HelpCentersResource,
    AsyncHelpCentersResource,
    HelpCentersResourceWithRawResponse,
    AsyncHelpCentersResourceWithRawResponse,
    HelpCentersResourceWithStreamingResponse,
    AsyncHelpCentersResourceWithStreamingResponse,
)

__all__ = ["HelpCenterResource", "AsyncHelpCenterResource"]


class HelpCenterResource(SyncAPIResource):
    @cached_property
    def collections(self) -> CollectionsResource:
        return CollectionsResource(self._client)

    @cached_property
    def help_centers(self) -> HelpCentersResource:
        return HelpCentersResource(self._client)

    @cached_property
    def with_raw_response(self) -> HelpCenterResourceWithRawResponse:
        return HelpCenterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HelpCenterResourceWithStreamingResponse:
        return HelpCenterResourceWithStreamingResponse(self)


class AsyncHelpCenterResource(AsyncAPIResource):
    @cached_property
    def collections(self) -> AsyncCollectionsResource:
        return AsyncCollectionsResource(self._client)

    @cached_property
    def help_centers(self) -> AsyncHelpCentersResource:
        return AsyncHelpCentersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHelpCenterResourceWithRawResponse:
        return AsyncHelpCenterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHelpCenterResourceWithStreamingResponse:
        return AsyncHelpCenterResourceWithStreamingResponse(self)


class HelpCenterResourceWithRawResponse:
    def __init__(self, help_center: HelpCenterResource) -> None:
        self._help_center = help_center

    @cached_property
    def collections(self) -> CollectionsResourceWithRawResponse:
        return CollectionsResourceWithRawResponse(self._help_center.collections)

    @cached_property
    def help_centers(self) -> HelpCentersResourceWithRawResponse:
        return HelpCentersResourceWithRawResponse(self._help_center.help_centers)


class AsyncHelpCenterResourceWithRawResponse:
    def __init__(self, help_center: AsyncHelpCenterResource) -> None:
        self._help_center = help_center

    @cached_property
    def collections(self) -> AsyncCollectionsResourceWithRawResponse:
        return AsyncCollectionsResourceWithRawResponse(self._help_center.collections)

    @cached_property
    def help_centers(self) -> AsyncHelpCentersResourceWithRawResponse:
        return AsyncHelpCentersResourceWithRawResponse(self._help_center.help_centers)


class HelpCenterResourceWithStreamingResponse:
    def __init__(self, help_center: HelpCenterResource) -> None:
        self._help_center = help_center

    @cached_property
    def collections(self) -> CollectionsResourceWithStreamingResponse:
        return CollectionsResourceWithStreamingResponse(self._help_center.collections)

    @cached_property
    def help_centers(self) -> HelpCentersResourceWithStreamingResponse:
        return HelpCentersResourceWithStreamingResponse(self._help_center.help_centers)


class AsyncHelpCenterResourceWithStreamingResponse:
    def __init__(self, help_center: AsyncHelpCenterResource) -> None:
        self._help_center = help_center

    @cached_property
    def collections(self) -> AsyncCollectionsResourceWithStreamingResponse:
        return AsyncCollectionsResourceWithStreamingResponse(self._help_center.collections)

    @cached_property
    def help_centers(self) -> AsyncHelpCentersResourceWithStreamingResponse:
        return AsyncHelpCentersResourceWithStreamingResponse(self._help_center.help_centers)
