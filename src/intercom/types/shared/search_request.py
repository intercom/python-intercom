# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["SearchRequest", "Query", "QuerySingleFilterSearchRequest", "Pagination"]


class QuerySingleFilterSearchRequest(BaseModel):
    field: Optional[str] = None
    """The Intercom defined id representing the company."""

    operator: Optional[Literal["=", "!=", "IN", "NIN", "<", ">", "~", "!~", "^", "$"]] = None
    """The Intercom defined id representing the company."""

    value: Optional[str] = None
    """The Intercom defined id representing the company."""


Query = Union[QuerySingleFilterSearchRequest, "MultipleFilterSearchRequest"]


class Pagination(BaseModel):
    page: Optional[int] = None

    starting_after: Optional[str] = None


class SearchRequest(BaseModel):
    query: Query

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
