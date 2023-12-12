# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VisitorDeletedObject"]


class VisitorDeletedObject(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the visitor which is given by Intercom."""

    type: Optional[Literal["visitor"]] = None
    """The type of object which was deleted"""

    user_id: Optional[str] = None
    """Automatically generated identifier for the Visitor."""
