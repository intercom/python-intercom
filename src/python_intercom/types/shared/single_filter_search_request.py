# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SingleFilterSearchRequest"]


class SingleFilterSearchRequest(BaseModel):
    field: Optional[str] = None
    """The accepted field that you want to search on."""

    operator: Optional[Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]] = None
    """
    The accepted operators you can use to define how you want to search for the
    value.
    """

    value: Optional[str] = None
    """The value that you want to search on."""
