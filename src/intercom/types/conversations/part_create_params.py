# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "PartCreateParams",
    "CloseConversationRequest",
    "SnoozeConversationRequest",
    "OpenConversationRequest",
    "AssignConversationRequest",
]


class CloseConversationRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is performing the action."""

    message_type: Required[Literal["close"]]

    type: Required[Literal["admin"]]

    body: str
    """
    Optionally you can leave a message in the conversation to provide additional
    context to the user and other teammates.
    """


class SnoozeConversationRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is performing the action."""

    message_type: Required[Literal["snoozed"]]

    snoozed_until: Required[int]
    """The time you want the conversation to reopen."""


class OpenConversationRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is performing the action."""

    message_type: Required[Literal["open"]]


class AssignConversationRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is performing the action."""

    assignee_id: Required[str]
    """
    The
    ` id`` of the  `admin`or`team`which will be assigned the conversation.\nA conversation can be assigned both an admin and a team.\nSet`0`
    if you want this assign to no admin or team (ie. Unassigned).
    """

    message_type: Required[Literal["assignment"]]

    type: Required[Literal["admin", "team"]]

    body: str
    """Optionally you can send a response in the conversation when it is assigned."""


PartCreateParams = Union[
    CloseConversationRequest, SnoozeConversationRequest, OpenConversationRequest, AssignConversationRequest
]
