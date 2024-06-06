# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["MultipleFilterSearchRequest", "ValueSingleFilterSearchRequest"]


class ValueSingleFilterSearchRequest(TypedDict, total=False):
    field: str
    """The accepted field that you want to search on."""

    operator: Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]
    """
    The accepted operators you can use to define how you want to search for the
    value.
    """

    value: str
    """The value that you want to search on."""


class MultipleFilterSearchRequest(TypedDict, total=False):
    operator: Literal["AND", "OR"]
    """An operator to allow boolean inspection between multiple fields."""

    value: Union[Iterable[MultipleFilterSearchRequest], Iterable[ValueSingleFilterSearchRequest]]
    """Add mutiple filters."""
