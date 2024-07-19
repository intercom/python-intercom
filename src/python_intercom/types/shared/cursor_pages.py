# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .starting_after_paging import StartingAfterPaging

__all__ = ["CursorPages"]


class CursorPages(BaseModel):
    next: Optional[StartingAfterPaging] = None

    page: Optional[int] = None
    """The current page"""

    per_page: Optional[int] = None
    """Number of results per page"""

    total_pages: Optional[int] = None
    """Total number of pages"""

    type: Optional[Literal["pages"]] = None
    """the type of object `pages`."""
