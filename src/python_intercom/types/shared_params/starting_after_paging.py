# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["StartingAfterPaging"]


class StartingAfterPaging(TypedDict, total=False):
    per_page: int
    """The number of results to fetch per page."""

    starting_after: Optional[str]
    """The cursor to use in the next request to get the next page of results."""
