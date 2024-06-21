# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

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


class TagCompanyRequest(TypedDict, total=False):
    companies: Required[Iterable[TagCompanyRequestCompany]]
    """The id or company_id of the company can be passed as input parameters."""

    name: Required[str]
    """The name of the tag, which will be created if not found."""

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


class TagMultipleUsersRequestUser(TypedDict, total=False):
    id: str
    """The Intercom defined id representing the user."""


TagCreateOrUpdateParams = Union[
    CreateOrUpdateTagRequest, TagCompanyRequest, UntagCompanyRequest, TagMultipleUsersRequest
]
