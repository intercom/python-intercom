# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TagDeleteParams"]


class TagDeleteParams(TypedDict, total=False):
    conversation_id: Required[str]

    admin_id: Required[str]
    """The unique identifier for the admin which is given by Intercom."""
