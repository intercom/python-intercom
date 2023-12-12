# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..shared import Company
from ..._models import BaseModel

__all__ = ["ContactAttachedCompanies", "Pages"]


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


class ContactAttachedCompanies(BaseModel):
    companies: Optional[List[Company]] = None
    """An array containing Company Objects"""

    pages: Optional[Pages] = None
    """
    The majority of list resources in the API are paginated to allow clients to
    traverse data over multiple requests.

    Their responses are likely to contain a pages object that hosts pagination links
    which a client can use to paginate through the data without having to construct
    a query. The link relations for the pages field are as follows.
    """

    total_count: Optional[int] = None
    """The total number of companies associated to this contact"""

    type: Optional[Literal["list"]] = None
    """The type of object"""
