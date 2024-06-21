# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

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
