# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SingleFilterSearchRequest"]


class SingleFilterSearchRequest(TypedDict, total=False):
    field: str
    """The accepted field that you want to search on."""

    operator: Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]
    """
    The accepted operators you can use to define how you want to search for the
    value.
    """

    value: str
    """The value that you want to search on."""
