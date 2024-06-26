# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, TypedDict

from ...types import shared_params

__all__ = ["MultipleFilterSearchRequest"]


class MultipleFilterSearchRequest(TypedDict, total=False):
    operator: Literal["AND", "OR"]
    """An operator to allow boolean inspection between multiple fields."""

    value: Union[Iterable[MultipleFilterSearchRequest], Iterable[shared_params.SingleFilterSearchRequest]]
    """Add mutiple filters."""
