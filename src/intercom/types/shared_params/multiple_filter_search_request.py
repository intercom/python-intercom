# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["MultipleFilterSearchRequest", "ValueSingleFilterSearchRequest"]


class ValueSingleFilterSearchRequest(TypedDict, total=False):
    field: str
    """The Intercom defined id representing the company."""

    operator: Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]
    """The Intercom defined id representing the company."""

    value: str
    """The Intercom defined id representing the company."""


class MultipleFilterSearchRequest(TypedDict, total=False):
    operator: Literal["AND", "OR"]
    """An operator to allow boolean inspection between multiple fields."""

    value: Union[Iterable[MultipleFilterSearchRequest], Iterable[ValueSingleFilterSearchRequest]]
    """Add mutiple filters."""
