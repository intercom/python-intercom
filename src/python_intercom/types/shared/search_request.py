# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel
from .starting_after_paging import StartingAfterPaging
from .single_filter_search_request import SingleFilterSearchRequest

__all__ = ["SearchRequest", "Query"]

Query = Union[SingleFilterSearchRequest, "MultipleFilterSearchRequest"]


class SearchRequest(BaseModel):
    query: Query
    """Search using Intercoms Search APIs with a single filter."""

    pagination: Optional[StartingAfterPaging] = None


from .multiple_filter_search_request import MultipleFilterSearchRequest

if PYDANTIC_V2:
    SearchRequest.model_rebuild()
else:
    SearchRequest.update_forward_refs()  # type: ignore
