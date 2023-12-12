# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .tag import Tag
from ..._models import BaseModel

__all__ = ["TagList"]


class TagList(BaseModel):
    data: Optional[List[Tag]] = None
    """A list of tags objects associated with the workspace ."""

    type: Optional[Literal["list"]] = None
    """The type of the object"""
