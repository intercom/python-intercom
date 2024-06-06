# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Team", "AdminPriorityLevel"]


class AdminPriorityLevel(BaseModel):
    primary_admin_ids: Optional[List[int]] = None
    """The primary admin ids for the team"""

    secondary_admin_ids: Optional[List[int]] = None
    """The secondary admin ids for the team"""


class Team(BaseModel):
    id: Optional[str] = None
    """The id of the team"""

    admin_ids: Optional[List[int]] = None
    """The list of admin IDs that are a part of the team."""

    admin_priority_level: Optional[AdminPriorityLevel] = None
    """Admin priority levels for the team"""

    name: Optional[str] = None
    """The name of the team"""

    type: Optional[str] = None
    """Value is always "team" """
