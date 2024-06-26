# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DataAttributeUpdateParams"]


class DataAttributeUpdateParams(TypedDict, total=False):
    archived: bool
    """Whether the attribute is to be archived or not."""

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
