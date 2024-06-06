# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

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


class FilterUserIDQueryParameter(TypedDict, total=False):
    user_id: Required[str]


class FilterIntercomUserIDQueryParameter(TypedDict, total=False):
    intercom_user_id: Required[str]


class FilterEmailQueryParameter(TypedDict, total=False):
    email: Required[str]


Filter = Union[FilterUserIDQueryParameter, FilterIntercomUserIDQueryParameter, FilterEmailQueryParameter]
