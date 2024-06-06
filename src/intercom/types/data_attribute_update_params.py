# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["DataAttributeUpdateParams"]


class DataAttributeUpdateParams(TypedDict, total=False):
    archived: bool
    """Whether the attribute is to be archived or not."""

    description: str
    """The readable description you see in the UI for the attribute."""

    options: List[str]
    """To create list attributes.

    Provide a set of hashes with `value` as the key of the options you want to make.
    `data_type` must be `string`.
    """
