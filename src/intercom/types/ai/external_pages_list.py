# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .external_page import ExternalPage

__all__ = ["ExternalPagesList", "Pages"]


class Pages(BaseModel):
    next: Optional[str] = None
    """A link to the next page of results.

    A response that does not contain a next link does not have further data to
    fetch.
    """

    page: Optional[int] = None

    per_page: Optional[int] = None

    total_pages: Optional[int] = None

    type: Optional[Literal["pages"]] = None


class ExternalPagesList(BaseModel):
    data: Optional[List[ExternalPage]] = None
    """An array of External Page objects"""

    pages: Optional[Pages] = None
    """
    The majority of list resources in the API are paginated to allow clients to
    traverse data over multiple requests.

    Their responses are likely to contain a pages object that hosts pagination links
    which a client can use to paginate through the data without having to construct
    a query. The link relations for the pages field are as follows.
    """

    total_count: Optional[int] = None
    """A count of the total number of external pages."""

    type: Optional[Literal["list"]] = None
    """The type of the object - `list`."""
