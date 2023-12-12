# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .shared import Admin
from .._models import BaseModel

__all__ = ["AdminList"]


class AdminList(BaseModel):
    admins: Optional[List[Optional[Admin]]] = None
    """A list of admins associated with a given workspace."""

    type: Optional[str] = None
    """String representing the object's type. Always has the value `admin.list`."""
