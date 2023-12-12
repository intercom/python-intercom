# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContactSearchParams", "Query", "Pagination"]


class ContactSearchParams(TypedDict, total=False):
    query: Required[Query]

    pagination: Optional[Pagination]


class Query(TypedDict, total=False):
    field: str
    """The Intercom defined id representing the company."""

    operator: Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]
    """The Intercom defined id representing the company."""

    value: str
    """The Intercom defined id representing the company."""


class Pagination(TypedDict, total=False):
    page: int

    starting_after: str
