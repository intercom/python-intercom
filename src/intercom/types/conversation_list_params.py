# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
    per_page: int
    """How many results per page"""

    starting_after: str
    """String used to get the next page of conversations."""
