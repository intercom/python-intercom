# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypedDict

from ..news import Newsfeed, NewsItem
from .newsfeed import Newsfeed
from .news_item import NewsItem

__all__ = ["PaginatedResponse", "Data", "Pages", "PagesNext"]

Data = Union[NewsItem, Newsfeed]


class PagesNext(TypedDict, total=False):
    page: int

    starting_after: str


class Pages(TypedDict, total=False):
    next: Optional[PagesNext]

    page: int
    """The current page"""

    per_page: int
    """Number of results per page"""

    total_pages: int
    """Total number of pages"""

    type: Literal["pages"]
    """the type of object `pages`."""


class PaginatedResponse(TypedDict, total=False):
    data: List[Data]
    """An array of Objects"""

    pages: Optional[Pages]
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    total_count: int
    """A count of the total number of objects."""

    type: Literal["list", "conversation.list"]
    """The type of object"""
