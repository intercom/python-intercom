# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..segment import Segment
from ..._models import BaseModel

__all__ = ["CompanyAttachedSegments"]


class CompanyAttachedSegments(BaseModel):
    data: Optional[List[Segment]] = None
    """An array containing Segment Objects"""

    type: Optional[Literal["list"]] = None
    """The type of object - `list`"""
