# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .cursor_pages import CursorPages
from ..news.newsfeed import Newsfeed
from ..news.news_item import NewsItem

__all__ = ["PaginatedResponse", "Data"]

Data = Union[NewsItem, Newsfeed]


class PaginatedResponse(BaseModel):
    data: Optional[List[Data]] = None
    """An array of Objects"""

    pages: Optional[CursorPages] = None
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    total_count: Optional[int] = None
    """A count of the total number of objects."""

    type: Optional[Literal["list", "conversation.list"]] = None
    """The type of object"""
