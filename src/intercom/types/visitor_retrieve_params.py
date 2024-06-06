# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VisitorRetrieveParams"]


class VisitorRetrieveParams(TypedDict, total=False):
    user_id: Required[str]
    """The user_id of the Visitor you want to retrieve."""
