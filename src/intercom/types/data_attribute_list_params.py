# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DataAttributeListParams"]


class DataAttributeListParams(TypedDict, total=False):
    include_archived: bool
    """Include archived attributes in the list.

    By default we return only non archived data attributes.
    """

    model: Literal["contact", "company", "conversation"]
    """Specify the data attribute model to return."""
