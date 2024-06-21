# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.part_attachment import PartAttachment

__all__ = ["TicketReply", "Author"]


class Author(BaseModel):
    id: Optional[str] = None
    """The id of the author"""

    email: Optional[str] = None
    """The email of the author"""

    name: Optional[str] = None
    """The name of the author"""

    type: Optional[Literal["admin", "bot", "team", "user"]] = None
    """The type of the author"""


class TicketReply(BaseModel):
    id: Optional[str] = None
    """The id representing the part."""

    attachments: Optional[List[PartAttachment]] = None
    """A list of attachments for the part."""

    author: Optional[Author] = None
    """The author that wrote or triggered the part. Can be a bot, admin, team or user."""

    body: Optional[str] = None
    """The message body, which may contain HTML."""

    created_at: Optional[int] = None
    """The time the note was created."""

    part_type: Optional[Literal["note", "comment", "quick_reply"]] = None
    """Type of the part"""

    redacted: Optional[bool] = None
    """Whether or not the ticket part has been redacted."""

    type: Optional[Literal["ticket_part"]] = None
    """Always ticket_part"""

    updated_at: Optional[int] = None
    """The last time the note was updated."""
