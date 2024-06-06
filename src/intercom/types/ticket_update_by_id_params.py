# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

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


class Assignment(TypedDict, total=False):
    admin_id: str
    """The ID of the admin performing the action."""

    assignee_id: str
    """The ID of the admin or team to which the ticket is assigned.

    Set this 0 to unassign it.
    """
