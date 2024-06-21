# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CompanyCreateParams"]


class CompanyCreateParams(TypedDict, total=False):
    company_id: str
    """The company id you have defined for the company. Can't be updated"""

    custom_attributes: Dict[str, str]
    """
    A hash of key/value pairs containing any other data about the company you want
    Intercom to store.
    """

    industry: str
    """The industry that this company operates in."""

    monthly_spend: int
    """How much revenue the company generates for your business.

    Note that this will truncate floats. i.e. it only allow for whole integers,
    155.98 will be truncated to 155. Note that this has an upper limit of 2\\**\\**31-1
    or 2147483647..
    """

    name: str
    """The name of the Company"""

    plan: str
    """The name of the plan you have associated with the company."""

    remote_created_at: int
    """The time the company was created by you."""

    size: int
    """The number of employees in this company."""

    website: str
    """The URL for this company's website.

    Please note that the value specified here is not validated. Accepts any string.
    """

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
