# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TagCreateParams"]


class TagCreateParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the tag which is given by Intercom"""

    admin_id: Required[str]
    """The unique identifier for the admin which is given by Intercom."""
