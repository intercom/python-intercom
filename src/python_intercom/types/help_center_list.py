# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .help_center.help_center import HelpCenter

__all__ = ["HelpCenterList"]


class HelpCenterList(BaseModel):
    data: Optional[List[HelpCenter]] = None
    """An array of Help Center objects"""

    type: Optional[Literal["list"]] = None
    """The type of the object - `list`."""
