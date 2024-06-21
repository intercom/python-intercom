# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversationCreateParams", "From"]


class ConversationCreateParams(TypedDict, total=False):
    body: Required[str]
    """The content of the message. HTML is not supported."""

    from_: Required[Annotated[From, PropertyInfo(alias="from")]]

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


class From(TypedDict, total=False):
    id: Required[str]
    """The identifier for the contact which is given by Intercom."""

    type: Required[Literal["lead", "user", "contact"]]
    """The role associated to the contact - user or lead."""
