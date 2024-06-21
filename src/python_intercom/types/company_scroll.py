# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.company import Company
from .shared.cursor_pages import CursorPages

__all__ = ["CompanyScroll"]


class CompanyScroll(BaseModel):
    data: Optional[List[Company]] = None

    pages: Optional[CursorPages] = None
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    scroll_param: Optional[str] = None
    """
    The scroll parameter to use in the next request to fetch the next page of
    results.
    """

    total_count: Optional[int] = None
    """The total number of companies"""

    type: Optional[Literal["list"]] = None
    """The type of object - `list`"""
