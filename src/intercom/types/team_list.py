# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .team import Team
from .._models import BaseModel

__all__ = ["TeamList"]


class TeamList(BaseModel):
    teams: Optional[List[Team]] = None
    """A list of team objects"""

    type: Optional[Literal["team.list"]] = None
    """The type of the object"""
