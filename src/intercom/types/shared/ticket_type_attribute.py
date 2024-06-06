# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TicketTypeAttribute"]


class TicketTypeAttribute(BaseModel):
    id: Optional[str] = None
    """The id representing the ticket type attribute."""

    archived: Optional[bool] = None
    """Whether the ticket type attribute is archived or not."""

    created_at: Optional[int] = None
    """The date and time the ticket type attribute was created."""

    data_type: Optional[str] = None
    """
    The type of the data attribute (allowed values: "string list integer decimal
    boolean datetime files")
    """

    default: Optional[bool] = None
    """Whether the attribute is built in or not."""

    description: Optional[str] = None
    """The description of the ticket type attribute"""

    input_options: Optional[object] = None
    """Input options for the attribute"""

    name: Optional[str] = None
    """The name of the ticket type attribute"""

    order: Optional[int] = None
    """The order of the attribute against other attributes"""

    required_to_create: Optional[bool] = None
    """Whether the attribute is required or not for teammates."""

    required_to_create_for_contacts: Optional[bool] = None
    """Whether the attribute is required or not for contacts."""

    ticket_type_id: Optional[int] = None
    """The id of the ticket type that the attribute belongs to."""

    type: Optional[str] = None
    """String representing the object's type.

    Always has the value `ticket_type_attribute`.
    """

    updated_at: Optional[int] = None
    """The date and time the ticket type attribute was last updated."""

    visible_on_create: Optional[bool] = None
    """Whether the attribute is visible or not to teammates."""

    visible_to_contacts: Optional[bool] = None
    """Whether the attribute is visible or not to contacts."""

    workspace_id: Optional[str] = None
    """The id of the workspace that the ticket type attribute belongs to."""
