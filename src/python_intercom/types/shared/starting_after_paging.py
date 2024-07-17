# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["StartingAfterPaging"]


class StartingAfterPaging(BaseModel):
    per_page: Optional[int] = None
    """The number of results to fetch per page."""

    starting_after: Optional[str] = None
    """The cursor to use in the next request to get the next page of results."""
