# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["Tag", "AppliedBy"]


class AppliedBy(TypedDict, total=False):
    id: Optional[str]

    type: str


class Tag(TypedDict, total=False):
    id: str
    """The id of the tag"""

    applied_at: int
    """The time when the tag was applied to the object"""

    applied_by: AppliedBy
    """reference to another object"""

    name: str
    """The name of the tag"""

    type: str
    """value is "tag" """
