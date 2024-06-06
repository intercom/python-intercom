# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["GroupContent"]


class GroupContent(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""
