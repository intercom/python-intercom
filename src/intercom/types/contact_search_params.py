# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

from ..types import shared_params

__all__ = ["ContactSearchParams", "Query", "QuerySingleFilterSearchRequest", "Pagination"]


class ContactSearchParams(TypedDict, total=False):
    query: Required[Query]
    """Search using Intercoms Search APIs with a single filter."""

    pagination: Optional[Pagination]


class QuerySingleFilterSearchRequest(TypedDict, total=False):
    field: str
    """The accepted field that you want to search on."""

    operator: Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]
    """
    The accepted operators you can use to define how you want to search for the
    value.
    """

    value: str
    """The value that you want to search on."""


Query = Union[QuerySingleFilterSearchRequest, shared_params.MultipleFilterSearchRequest]


class Pagination(TypedDict, total=False):
    per_page: int
    """The number of results to fetch per page."""

    starting_after: Optional[str]
    """The cursor to use in the next request to get the next page of results."""
