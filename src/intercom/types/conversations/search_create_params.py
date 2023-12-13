# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "SearchCreateParams",
    "Query",
    "QuerySingleFilterSearchRequest",
    "QueryMultipleFilterSearchRequest",
    "QueryMultipleFilterSearchRequestValueUnionMember0",
    "QueryMultipleFilterSearchRequestValueUnionMember0ValueUnionMember1",
    "QueryMultipleFilterSearchRequestValueUnionMember1",
    "Pagination",
]


class SearchCreateParams(TypedDict, total=False):
    query: Required[Query]

    pagination: Optional[Pagination]


class QuerySingleFilterSearchRequest(TypedDict, total=False):
    field: str
    """The Intercom defined id representing the company."""

    operator: Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]
    """The Intercom defined id representing the company."""

    value: str
    """The Intercom defined id representing the company."""


class QueryMultipleFilterSearchRequestValueUnionMember0ValueUnionMember1(TypedDict, total=False):
    field: str
    """The Intercom defined id representing the company."""

    operator: Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]
    """The Intercom defined id representing the company."""

    value: str
    """The Intercom defined id representing the company."""


class QueryMultipleFilterSearchRequestValueUnionMember0(TypedDict, total=False):
    operator: Literal["AND", "OR"]
    """An operator to allow boolean inspection between multiple fields."""

    value: Union[List[object], List[QueryMultipleFilterSearchRequestValueUnionMember0ValueUnionMember1]]
    """Add mutiple filters."""


class QueryMultipleFilterSearchRequestValueUnionMember1(TypedDict, total=False):
    field: str
    """The Intercom defined id representing the company."""

    operator: Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]
    """The Intercom defined id representing the company."""

    value: str
    """The Intercom defined id representing the company."""


class QueryMultipleFilterSearchRequest(TypedDict, total=False):
    operator: Literal["AND", "OR"]
    """An operator to allow boolean inspection between multiple fields."""

    value: Union[
        List[QueryMultipleFilterSearchRequestValueUnionMember0], List[QueryMultipleFilterSearchRequestValueUnionMember1]
    ]
    """Add mutiple filters."""


Query = Union[QuerySingleFilterSearchRequest, QueryMultipleFilterSearchRequest]


class Pagination(TypedDict, total=False):
    page: int

    starting_after: str
