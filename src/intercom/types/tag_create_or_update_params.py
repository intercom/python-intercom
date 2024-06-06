# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = [
    "TagCreateOrUpdateParams",
    "CreateOrUpdateTagRequest",
    "TagCompanyRequest",
    "TagCompanyRequestCompany",
    "UntagCompanyRequest",
    "UntagCompanyRequestCompany",
    "TagMultipleUsersRequest",
    "TagMultipleUsersRequestUser",
]


class CreateOrUpdateTagRequest(TypedDict, total=False):
    name: Required[str]
    """
    The name of the tag, which will be created if not found, or the new name for the
    tag if this is an update request. Names are case insensitive.
    """

    id: str
    """The id of tag to updates."""


class TagCompanyRequest(TypedDict, total=False):
    companies: Required[Iterable[TagCompanyRequestCompany]]
    """The id or company_id of the company can be passed as input parameters."""

    name: Required[str]
    """The name of the tag, which will be created if not found."""


class TagCompanyRequestCompany(TypedDict, total=False):
    id: str
    """The Intercom defined id representing the company."""

    company_id: str
    """The company id you have defined for the company."""


class UntagCompanyRequest(TypedDict, total=False):
    companies: Required[Iterable[UntagCompanyRequestCompany]]
    """The id or company_id of the company can be passed as input parameters."""

    name: Required[str]
    """The name of the tag which will be untagged from the company"""


class UntagCompanyRequestCompany(TypedDict, total=False):
    id: str
    """The Intercom defined id representing the company."""

    company_id: str
    """The company id you have defined for the company."""

    untag: bool
    """Always set to true"""


class TagMultipleUsersRequest(TypedDict, total=False):
    name: Required[str]
    """The name of the tag, which will be created if not found."""

    users: Required[Iterable[TagMultipleUsersRequestUser]]


class TagMultipleUsersRequestUser(TypedDict, total=False):
    id: str
    """The Intercom defined id representing the user."""


TagCreateOrUpdateParams = Union[
    CreateOrUpdateTagRequest, TagCompanyRequest, UntagCompanyRequest, TagMultipleUsersRequest
]
