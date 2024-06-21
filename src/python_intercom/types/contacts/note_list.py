# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.note import Note
from ..shared.cursor_pages import CursorPages

__all__ = ["NoteList"]


class NoteList(BaseModel):
    data: Optional[List[Note]] = None
    """An array of notes."""

    pages: Optional[CursorPages] = None
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    total_count: Optional[int] = None
    """A count of the total number of notes."""

    type: Optional[str] = None
    """String representing the object's type. Always has the value `list`."""
