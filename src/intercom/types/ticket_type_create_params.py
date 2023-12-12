# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TicketTypeCreateParams"]


class TicketTypeCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the ticket type."""

    category: Literal["Customer", "Back-office", "Tracker"]
    """Category of the Ticket Type."""

    description: str
    """The description of the ticket type."""

    icon: str
    """The icon of the ticket type."""

    is_internal: bool
    """
    Whether the tickets associated with this ticket type are intended for internal
    use only or will be shared with customers. This is currently a limited
    attribute.
    """
