# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.ticket import Ticket
from .shared.cursor_pages import CursorPages

__all__ = ["TicketList"]


class TicketList(BaseModel):
    pages: Optional[CursorPages] = None
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    tickets: Optional[List[Optional[Ticket]]] = None
    """The list of ticket objects"""

    total_count: Optional[int] = None
    """A count of the total number of objects."""

    type: Optional[Literal["ticket.list"]] = None
    """Always ticket.list"""
