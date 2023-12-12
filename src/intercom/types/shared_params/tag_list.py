# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .tag import Tag
from ..shared import Tag

__all__ = ["TagList"]


class TagList(TypedDict, total=False):
    data: List[Tag]
    """A list of tags objects associated with the workspace ."""

    type: Literal["list"]
    """The type of the object"""
