# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DataAttributeCreateParams"]


class DataAttributeCreateParams(TypedDict, total=False):
    data_type: Required[Literal["string", "integer", "float", "boolean", "datetime", "date"]]
    """The type of data stored for this attribute."""

    model: Required[Literal["contact", "company"]]
    """The model that the data attribute belongs to."""

    name: Required[str]
    """The name of the data attribute."""

    description: str
    """The readable description you see in the UI for the attribute."""

    messenger_writable: bool
    """Can this attribute be updated by the Messenger"""

    options: List[str]
    """To create list attributes.

    Provide a set of hashes with `value` as the key of the options you want to make.
    `data_type` must be `string`.
    """
