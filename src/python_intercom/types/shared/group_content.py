# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GroupContent"]


class GroupContent(BaseModel):
    description: Optional[str] = None
    """The description of the collection. Only available for collections."""

    name: Optional[str] = None
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]] = None
    """The type of object - `group_content` ."""
