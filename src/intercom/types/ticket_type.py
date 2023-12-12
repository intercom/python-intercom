# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .shared import TicketTypeAttribute
from .._models import BaseModel

__all__ = ["TicketType", "TicketTypeAttributes"]


class TicketTypeAttributes(BaseModel):
    ticket_type_attributes: Optional[List[Optional[TicketTypeAttribute]]] = None
    """A list of ticket type attributes associated with a given ticket type."""

    type: Optional[str] = None
    """String representing the object's type.

    Always has the value `ticket_type_attributes.list`.
    """


class TicketType(BaseModel):
    id: Optional[str] = None
    """The id representing the ticket type."""

    archived: Optional[bool] = None
    """Whether the ticket type is archived or not."""

    category: Optional[Literal["Customer", "Back-office", "Tracker"]] = None
    """Category of the Ticket Type."""

    created_at: Optional[int] = None
    """The date and time the ticket type was created."""

    description: Optional[str] = None
    """The description of the ticket type"""

    icon: Optional[str] = None
    """The icon of the ticket type"""

    name: Optional[str] = None
    """The name of the ticket type"""

    ticket_type_attributes: Optional[TicketTypeAttributes] = None
    """A list of attributes associated with a given ticket type."""

    type: Optional[str] = None
    """String representing the object's type. Always has the value `ticket_type`."""

    updated_at: Optional[int] = None
    """The date and time the ticket type was last updated."""

    workspace_id: Optional[str] = None
    """The id of the workspace that the ticket type belongs to."""
