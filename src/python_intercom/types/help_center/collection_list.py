# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .collection import Collection
from ..shared.cursor_pages import CursorPages

__all__ = ["CollectionList"]


class CollectionList(BaseModel):
    data: Optional[List[Collection]] = None
    """An array of collection objects"""

    pages: Optional[CursorPages] = None
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    total_count: Optional[int] = None
    """A count of the total number of collections."""

    type: Optional[Literal["list"]] = None
    """The type of the object - `list`."""
