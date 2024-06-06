# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NoteCreateParams"]


class NoteCreateParams(TypedDict, total=False):
    body: Required[str]
    """The text of the note."""

    admin_id: str
    """The unique identifier of a given admin."""

    contact_id: str
    """The unique identifier of a given contact."""
