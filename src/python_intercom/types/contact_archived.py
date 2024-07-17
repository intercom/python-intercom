# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ContactArchived"]


class ContactArchived(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the contact which is given by Intercom."""

    archived: Optional[bool] = None
    """Whether the contact is archived or not."""

    external_id: Optional[str] = None
    """The unique identifier for the contact which is provided by the Client."""

    type: Optional[Literal["contact"]] = None
    """always contact"""
