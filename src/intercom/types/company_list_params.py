# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CompanyListParams"]


class CompanyListParams(TypedDict, total=False):
    order: str
    """`asc` or `desc`.

    Return the companies in ascending or descending order. Defaults to desc
    """

    page: int
    """The page of results to fetch. Defaults to first page"""

    per_page: int
    """How many results to return per page. Defaults to 15"""
