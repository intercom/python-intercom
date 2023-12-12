# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Admin", "TeamPriorityLevel"]


class TeamPriorityLevel(BaseModel):
    primary_team_ids: Optional[List[int]] = None
    """The primary team ids for the team"""

    secondary_team_ids: Optional[List[int]] = None
    """The secondary team ids for the team"""


class Admin(BaseModel):
    id: Optional[str] = None
    """The id representing the admin."""

    avatar: Optional[str] = None
    """Image for the associated team or teammate"""

    away_mode_enabled: Optional[bool] = None
    """Identifies if this admin is currently set in away mode."""

    away_mode_reassign: Optional[bool] = None
    """
    Identifies if this admin is set to automatically reassign new conversations to
    the apps default inbox.
    """

    email: Optional[str] = None
    """The email of the admin."""

    has_inbox_seat: Optional[bool] = None
    """
    Identifies if this admin has a paid inbox seat to restrict/allow features that
    require them.
    """

    job_title: Optional[str] = None
    """The job title of the admin."""

    name: Optional[str] = None
    """The name of the admin."""

    team_ids: Optional[List[int]] = None
    """This object represents the avatar associated with the admin."""

    team_priority_level: Optional[TeamPriorityLevel] = None
    """Admin priority levels for teams"""

    type: Optional[str] = None
    """String representing the object's type. Always has the value `admin`."""
