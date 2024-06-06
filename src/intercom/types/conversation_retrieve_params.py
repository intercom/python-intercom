# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationRetrieveParams"]


class ConversationRetrieveParams(TypedDict, total=False):
    display_as: str
    """Set to plaintext to retrieve conversation messages in plain text."""
