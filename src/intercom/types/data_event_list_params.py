# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "DataEventListParams",
    "Filter",
    "FilterUserIDQueryParameter",
    "FilterIntercomUserIDQueryParameter",
    "FilterEmailQueryParameter",
]


class DataEventListParams(TypedDict, total=False):
    filter: Required[Filter]

    type: Required[str]
    """The value must be user"""

    summary: bool
    """summary flag"""

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


class FilterUserIDQueryParameter(TypedDict, total=False):
    user_id: Required[str]


class FilterIntercomUserIDQueryParameter(TypedDict, total=False):
    intercom_user_id: Required[str]


class FilterEmailQueryParameter(TypedDict, total=False):
    email: Required[str]


Filter = Union[FilterUserIDQueryParameter, FilterIntercomUserIDQueryParameter, FilterEmailQueryParameter]
