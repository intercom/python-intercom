# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .segment import Segment
from .._models import BaseModel

__all__ = ["SegmentList"]


class SegmentList(BaseModel):
    pages: Optional[object] = None
    """A pagination object, which may be empty, indicating no further pages to fetch."""

    segments: Optional[List[Segment]] = None
    """A list of Segment objects"""

    type: Optional[Literal["segment.list"]] = None
    """The type of the object"""
