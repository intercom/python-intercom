# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TicketTypeUpdateParams"]


class TicketTypeUpdateParams(TypedDict, total=False):
    archived: bool
    """The archived status of the ticket type."""

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

    name: str
    """The name of the ticket type."""

    intercom_version: Annotated[
        Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ],
        PropertyInfo(alias="Intercom-Version"),
    ]
    """
    Intercom API version.By default, it's equal to the version set in the app
    package.
    """
