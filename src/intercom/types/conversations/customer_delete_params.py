# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomerDeleteParams"]


class CustomerDeleteParams(TypedDict, total=False):
    conversation_id: Required[str]

    admin_id: Required[str]
    """The `id` of the admin who is performing the action."""
