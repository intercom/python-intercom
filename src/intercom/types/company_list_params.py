# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["CompanyListParams", "Filter", "FilterFilterByTag", "FilterFilterBySegment"]


class CompanyListParams(TypedDict, total=False):
    filter: Required[Filter]
    """The `id` of the tag to filter by."""

    order: str
    """`asc` or `desc`.

    Return the companies in ascending or descending order. Defaults to desc
    """

    page: str
    """what page of results to fetch. Defaults to first page"""

    per_page: str
    """how many results per page. Defaults to 15"""


class FilterFilterByTag(TypedDict, total=False):
    tag_id: Required[str]


class FilterFilterBySegment(TypedDict, total=False):
    segment_id: Required[str]


Filter = Union[FilterFilterByTag, FilterFilterBySegment]
