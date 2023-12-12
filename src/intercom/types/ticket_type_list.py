# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel
from .ticket_type import TicketType

__all__ = ["TicketTypeList"]


class TicketTypeList(BaseModel):
    ticket_types: Optional[List[Optional[TicketType]]] = None
    """A list of ticket_types associated with a given workspace."""

    type: Optional[str] = None
    """String representing the object's type. Always has the value `ticket_type.list`."""
