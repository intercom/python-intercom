# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActivityLogListParams"]


class ActivityLogListParams(TypedDict, total=False):
    created_at_after: Required[str]
    """The start date that you request data for.

    It must be formatted as a UNIX timestamp.
    """

    created_at_before: str
    """The end date that you request data for.

    It must be formatted as a UNIX timestamp.
    """
