# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["DataEventCreateParams", "IDRequired", "UserIDRequired", "EmailRequired"]


class IDRequired(TypedDict, total=False):
    body: Required[object]


class UserIDRequired(TypedDict, total=False):
    body: Required[object]


class EmailRequired(TypedDict, total=False):
    body: Required[object]


DataEventCreateParams = Union[IDRequired, UserIDRequired, EmailRequired]
