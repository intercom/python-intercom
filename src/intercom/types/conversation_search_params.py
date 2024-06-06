# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

from ..types import shared_params

__all__ = ["ConversationSearchParams", "Query", "QuerySingleFilterSearchRequest", "Pagination"]


class ConversationSearchParams(TypedDict, total=False):
    query: Required[Query]

    pagination: Optional[Pagination]


class QuerySingleFilterSearchRequest(TypedDict, total=False):
    field: str
    """The Intercom defined id representing the company."""

    operator: Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]
    """The Intercom defined id representing the company."""

    value: str
    """The Intercom defined id representing the company."""


Query = Union[QuerySingleFilterSearchRequest, shared_params.MultipleFilterSearchRequest]


class Pagination(TypedDict, total=False):
    page: int

    starting_after: str
