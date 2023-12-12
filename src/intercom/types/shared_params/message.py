# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["Message"]


class Message(TypedDict, total=False):
    id: Required[str]
    """The id representing the message."""

    body: Required[str]
    """The message body, which may contain HTML."""

    created_at: Required[int]
    """The time the conversation was created."""

    message_type: Required[Literal["email", "inapp", "facebook", "twitter"]]
    """The type of message that was sent. Can be email, inapp, facebook or twitter."""

    type: Required[str]
    """The type of the message"""

    conversation_id: str
    """The associated conversation_id"""

    subject: str
    """The subject of the message. Only present if message_type: email."""
