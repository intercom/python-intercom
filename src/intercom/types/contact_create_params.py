# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["ContactCreateParams", "CreateContactWithEmail", "CreateContactWithExternalID", "CreateContactWithRole"]


class CreateContactWithEmail(TypedDict, total=False):
    body: Required[object]


class CreateContactWithExternalID(TypedDict, total=False):
    body: Required[object]


class CreateContactWithRole(TypedDict, total=False):
    body: Required[object]


ContactCreateParams = Union[CreateContactWithEmail, CreateContactWithExternalID, CreateContactWithRole]
