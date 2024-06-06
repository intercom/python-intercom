# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .admin import Admin
from ..._models import BaseModel

__all__ = ["Note", "Contact"]


class Contact(BaseModel):
    id: Optional[str] = None
    """The id of the contact."""

    type: Optional[str] = None
    """String representing the object's type. Always has the value `contact`."""


class Note(BaseModel):
    id: Optional[str] = None
    """The id of the note."""

    author: Optional[Admin] = None
    """Optional. Represents the Admin that created the note."""

    body: Optional[str] = None
    """The body text of the note."""

    contact: Optional[Contact] = None
    """Represents the contact that the note was created about."""

    created_at: Optional[int] = None
    """The time the note was created."""

    type: Optional[str] = None
    """String representing the object's type. Always has the value `note`."""
