# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["Admin", "TeamPriorityLevel"]


class TeamPriorityLevel(TypedDict, total=False):
    primary_team_ids: Optional[List[int]]
    """The primary team ids for the team"""

    secondary_team_ids: Optional[List[int]]
    """The secondary team ids for the team"""


class Admin(TypedDict, total=False):
    id: str
    """The id representing the admin."""

    avatar: Optional[str]
    """Image for the associated team or teammate"""

    away_mode_enabled: bool
    """Identifies if this admin is currently set in away mode."""

    away_mode_reassign: bool
    """
    Identifies if this admin is set to automatically reassign new conversations to
    the apps default inbox.
    """

    email: str
    """The email of the admin."""

    has_inbox_seat: bool
    """
    Identifies if this admin has a paid inbox seat to restrict/allow features that
    require them.
    """

    job_title: str
    """The job title of the admin."""

    name: str
    """The name of the admin."""

    team_ids: List[int]
    """This object represents the avatar associated with the admin."""

    team_priority_level: Optional[TeamPriorityLevel]
    """Admin priority levels for teams"""

    type: str
    """String representing the object's type. Always has the value `admin`."""
