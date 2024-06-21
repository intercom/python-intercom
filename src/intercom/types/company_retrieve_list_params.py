# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CompanyRetrieveListParams"]


class CompanyRetrieveListParams(TypedDict, total=False):
    company_id: str
    """The `company_id` of the company to filter by."""

    name: str
    """The `name` of the company to filter by."""

    page: int
    """The page of results to fetch. Defaults to first page"""

    per_page: int
    """How many results to display per page. Defaults to 15"""

    segment_id: str
    """The `segment_id` of the company to filter by."""

    tag_id: str
    """The `tag_id` of the company to filter by."""

    intercom_version: Annotated[
        Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ],
        PropertyInfo(alias="Intercom-Version"),
    ]
    """
    Intercom API version.By default, it's equal to the version set in the app
    package.
    """
