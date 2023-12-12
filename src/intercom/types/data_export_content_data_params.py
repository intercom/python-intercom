# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DataExportContentDataParams"]


class DataExportContentDataParams(TypedDict, total=False):
    created_at_after: Required[int]
    """The start date that you request data for.

    It must be formatted as a unix timestamp.
    """

    created_at_before: Required[int]
    """The end date that you request data for.

    It must be formatted as a unix timestamp.
    """
