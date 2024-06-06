# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AdminAwayParams"]


class AdminAwayParams(TypedDict, total=False):
    away_mode_enabled: Required[bool]
    """Set to "true" to change the status of the admin to away."""

    away_mode_reassign: Required[bool]
    """Set to "true" to assign any new conversation replies to your default inbox."""
