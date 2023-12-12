# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["CompanyCreateUpdateParams"]


class CompanyCreateUpdateParams(TypedDict, total=False):
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
