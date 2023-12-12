# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .admin import Admin
from ..shared import Admin

__all__ = ["Note", "Contact"]


class Contact(TypedDict, total=False):
    id: str
    """The id of the contact."""

    type: str
    """String representing the object's type. Always has the value `contact`."""


class Note(TypedDict, total=False):
    id: str
    """The id of the note."""

    author: Optional[Admin]
    """Optional. Represents the Admin that created the note."""

    body: str
    """The body text of the note."""

    contact: Optional[Contact]
    """Represents the contact that the note was created about."""

    created_at: int
    """The time the note was created."""

    type: str
    """String representing the object's type. Always has the value `note`."""
