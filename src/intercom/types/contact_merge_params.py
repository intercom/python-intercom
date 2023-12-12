# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ContactMergeParams"]


class ContactMergeParams(TypedDict, total=False):
    into: str
    """The unique identifier for the contact to merge into. Must be a user."""
