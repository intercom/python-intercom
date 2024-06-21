# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .article import Article
from .._models import BaseModel
from .shared.cursor_pages import CursorPages

__all__ = [
    "ArticleSearchResponse",
    "Data",
    "DataHighlight",
    "DataHighlightHighlightedSummary",
    "DataHighlightHighlightedTitle",
]


class DataHighlightHighlightedSummary(BaseModel):
    text: Optional[str] = None
    """The text of the title."""

    type: Optional[Literal["highlight", "plain"]] = None
    """The type of text - `highlight` or `plain`."""


class DataHighlightHighlightedTitle(BaseModel):
    text: Optional[str] = None
    """The text of the title."""

    type: Optional[Literal["highlight", "plain"]] = None
    """The type of text - `highlight` or `plain`."""


class DataHighlight(BaseModel):
    article_id: Optional[str] = None
    """The ID of the corresponding article."""

    highlighted_summary: Optional[List[List[DataHighlightHighlightedSummary]]] = None
    """An Article description and body text highlighted."""

    highlighted_title: Optional[List[DataHighlightHighlightedTitle]] = None
    """An Article title highlighted."""


class Data(BaseModel):
    articles: Optional[List[Article]] = None
    """An array of Article objects"""

    highlights: Optional[List[DataHighlight]] = None
    """A corresponding array of highlighted Article content"""


class ArticleSearchResponse(BaseModel):
    data: Optional[Data] = None
    """An object containing the results of the search."""

    pages: Optional[CursorPages] = None
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    total_count: Optional[int] = None
    """The total number of Articles matching the search query"""

    type: Optional[Literal["list"]] = None
    """The type of the object - `list`."""
