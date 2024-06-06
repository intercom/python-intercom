# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Tag", "AppliedBy"]


class AppliedBy(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class Tag(BaseModel):
    id: Optional[str] = None
    """The id of the tag"""

    applied_at: Optional[int] = None
    """The time when the tag was applied to the object"""

    applied_by: Optional[AppliedBy] = None
    """reference to another object"""

    name: Optional[str] = None
    """The name of the tag"""

    type: Optional[str] = None
    """value is "tag" """
