# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TicketUpdateByIDParams", "Assignment"]


class TicketUpdateByIDParams(TypedDict, total=False):
    assignment: Assignment

    is_shared: bool
    """Specify whether the ticket is visible to users."""

    open: bool
    """Specify if a ticket is open.

    Set to false to close a ticket. Closing a ticket will also unsnooze it.
    """

    snoozed_until: int
    """The time you want the ticket to reopen."""

    state: Literal["in_progress", "waiting_on_customer", "resolved"]
    """The state of the ticket."""

    ticket_attributes: object
    """The attributes set on the ticket."""

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


class Assignment(TypedDict, total=False):
    admin_id: str
    """The ID of the admin performing the action."""

    assignee_id: str
    """The ID of the admin or team to which the ticket is assigned.

    Set this 0 to unassign it.
    """
