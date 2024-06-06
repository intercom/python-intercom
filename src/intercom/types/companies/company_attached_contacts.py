# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.contact import Contact

__all__ = ["CompanyAttachedContacts", "Pages", "PagesNext"]


class PagesNext(BaseModel):
    page: Optional[int] = None

    starting_after: Optional[str] = None


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


class CompanyAttachedContacts(BaseModel):
    data: Optional[List[Contact]] = None
    """An array containing Contact Objects"""

    pages: Optional[Pages] = None
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    total_count: Optional[int] = None
    """The total number of contacts"""

    type: Optional[Literal["list"]] = None
    """The type of object - `list`"""
