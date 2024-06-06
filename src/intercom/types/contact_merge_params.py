# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactMergeParams"]


class ContactMergeParams(TypedDict, total=False):
    from_: Annotated[str, PropertyInfo(alias="from")]
    """The unique identifier for the contact to merge away from. Must be a lead."""

    into: str
    """The unique identifier for the contact to merge into. Must be a user."""
