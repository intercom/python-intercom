# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TicketTypeAttribute"]


class TicketTypeAttribute(TypedDict, total=False):
    id: str
    """The id representing the ticket type attribute."""

    archived: bool
    """Whether the ticket type attribute is archived or not."""

    created_at: int
    """The date and time the ticket type attribute was created."""

    data_type: str
    """
    The type of the data attribute (allowed values: "string list integer decimal
    boolean datetime files")
    """

    default: bool
    """Whether the attribute is built in or not."""

    description: str
    """The description of the ticket type attribute"""

    input_options: object
    """Input options for the attribute"""

    name: str
    """The name of the ticket type attribute"""

    order: int
    """The order of the attribute against other attributes"""

    required_to_create: bool
    """Whether the attribute is required or not for teammates."""

    required_to_create_for_contacts: bool
    """Whether the attribute is required or not for contacts."""

    ticket_type_id: int
    """The id of the ticket type that the attribute belongs to."""

    type: str
    """String representing the object's type.

    Always has the value `ticket_type_attribute`.
    """

    updated_at: int
    """The date and time the ticket type attribute was last updated."""

    visible_on_create: bool
    """Whether the attribute is visible or not to teammates."""

    visible_to_contacts: bool
    """Whether the attribute is visible or not to contacts."""

    workspace_id: str
    """The id of the workspace that the ticket type attribute belongs to."""
