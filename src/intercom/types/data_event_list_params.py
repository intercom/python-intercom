# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["DataEventListParams", "Filter", "FilterUserID", "FilterIntercomUserID", "FilterEmail"]


class DataEventListParams(TypedDict, total=False):
    filter: Required[Filter]

    type: Required[str]
    """The value must be user"""

    summary: bool
    """summary flag"""


class FilterUserID(TypedDict, total=False):
    user_id: Required[str]


class FilterIntercomUserID(TypedDict, total=False):
    intercom_user_id: Required[str]


class FilterEmail(TypedDict, total=False):
    email: Required[str]


Filter = Union[FilterUserID, FilterIntercomUserID, FilterEmail]
