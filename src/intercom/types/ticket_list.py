# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.ticket import Ticket

__all__ = ["TicketList", "Pages", "PagesNext"]


class PagesNext(BaseModel):
    per_page: Optional[int] = None
    """The number of results to fetch per page."""

    starting_after: Optional[str] = None
    """The cursor to use in the next request to get the next page of results."""


class Pages(BaseModel):
    next: Optional[PagesNext] = None

    page: Optional[int] = None
    """The current page"""

    per_page: Optional[int] = None
    """Number of results per page"""

    total_pages: Optional[int] = None
    """Total number of pages"""

    type: Optional[Literal["pages"]] = None
    """the type of object `pages`."""


class TicketList(BaseModel):
    pages: Optional[Pages] = None
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
