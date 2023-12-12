# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Message"]


class Message(BaseModel):
    id: str
    """The id representing the message."""

    body: str
    """The message body, which may contain HTML."""

    created_at: int
    """The time the conversation was created."""

    message_type: Literal["email", "inapp", "facebook", "twitter"]
    """The type of message that was sent. Can be email, inapp, facebook or twitter."""

    type: str
    """The type of the message"""

    conversation_id: Optional[str] = None
    """The associated conversation_id"""

    subject: Optional[str] = None
    """The subject of the message. Only present if message_type: email."""
