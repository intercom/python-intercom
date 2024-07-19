# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.admin import Admin

__all__ = ["AdminList"]


class AdminList(BaseModel):
    admins: Optional[List[Optional[Admin]]] = None
    """A list of admins associated with a given workspace."""

    type: Optional[str] = None
    """String representing the object's type. Always has the value `admin.list`."""
