# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

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


class SnoozeConversationRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is performing the action."""

    message_type: Required[Literal["snoozed"]]

    snoozed_until: Required[int]
    """The time you want the conversation to reopen."""

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


class OpenConversationRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is performing the action."""

    message_type: Required[Literal["open"]]

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


class AssignConversationRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is performing the action."""

    assignee_id: Required[str]
    """The `id` of the `admin` or `team` which will be assigned the conversation.

    A conversation can be assigned both an admin and a team.\nSet `0` if you want
    this assign to no admin or team (ie. Unassigned).
    """

    message_type: Required[Literal["assignment"]]

    type: Required[Literal["admin", "team"]]

    body: str
    """Optionally you can send a response in the conversation when it is assigned."""

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


PartCreateParams = Union[
    CloseConversationRequest, SnoozeConversationRequest, OpenConversationRequest, AssignConversationRequest
]
