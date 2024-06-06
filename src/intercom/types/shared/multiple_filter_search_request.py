# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["MultipleFilterSearchRequest", "ValueSingleFilterSearchRequest"]


class ValueSingleFilterSearchRequest(BaseModel):
    field: Optional[str] = None
    """The accepted field that you want to search on."""

    operator: Optional[Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]] = None
    """
    The accepted operators you can use to define how you want to search for the
    value.
    """

    value: Optional[str] = None
    """The value that you want to search on."""


class MultipleFilterSearchRequest(BaseModel):
    operator: Optional[Literal["AND", "OR"]] = None
    """An operator to allow boolean inspection between multiple fields."""

    value: Union[List[MultipleFilterSearchRequest], List[ValueSingleFilterSearchRequest], None] = None
    """Add mutiple filters."""


if PYDANTIC_V2:
    MultipleFilterSearchRequest.model_rebuild()
    ValueSingleFilterSearchRequest.model_rebuild()
else:
    MultipleFilterSearchRequest.update_forward_refs()  # type: ignore
    ValueSingleFilterSearchRequest.update_forward_refs()  # type: ignore
