# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TagRemoveParams"]


class TagRemoveParams(TypedDict, total=False):
    ticket_id: Required[str]

    admin_id: Required[str]
    """The unique identifier for the admin which is given by Intercom."""
