# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SegmentListParams"]


class SegmentListParams(TypedDict, total=False):
    include_count: bool
    """It includes the count of contacts that belong to each segment."""
