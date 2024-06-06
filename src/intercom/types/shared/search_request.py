# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["SearchRequest", "Query", "QuerySingleFilterSearchRequest", "Pagination"]


class QuerySingleFilterSearchRequest(BaseModel):
    field: Optional[str] = None
    """The accepted field that you want to search on."""

    operator: Optional[Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]] = None
    """
    The accepted operators you can use to define how you want to search for the
    value.
    """

    value: Optional[str] = None
    """The value that you want to search on."""


Query = Union[QuerySingleFilterSearchRequest, "MultipleFilterSearchRequest"]


class Pagination(BaseModel):
    per_page: Optional[int] = None
    """The number of results to fetch per page."""

    starting_after: Optional[str] = None
    """The cursor to use in the next request to get the next page of results."""


class SearchRequest(BaseModel):
    query: Query
    """Search using Intercoms Search APIs with a single filter."""

    pagination: Optional[Pagination] = None


from .multiple_filter_search_request import MultipleFilterSearchRequest

if PYDANTIC_V2:
    SearchRequest.model_rebuild()
    QuerySingleFilterSearchRequest.model_rebuild()
    Pagination.model_rebuild()
else:
    SearchRequest.update_forward_refs()  # type: ignore
    QuerySingleFilterSearchRequest.update_forward_refs()  # type: ignore
    Pagination.update_forward_refs()  # type: ignore
