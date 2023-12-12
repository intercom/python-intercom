# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..segment import Segment
from ..._models import BaseModel

__all__ = ["ContactSegments"]


class ContactSegments(BaseModel):
    data: Optional[List[Segment]] = None
    """Segment objects associated with the contact."""

    type: Optional[Literal["list"]] = None
    """The type of the object"""
