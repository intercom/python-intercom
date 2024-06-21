# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VisitorConvertParams", "User", "Visitor"]


class VisitorConvertParams(TypedDict, total=False):
    type: Required[str]
    """Represents the role of the Contact model. Accepts `lead` or `user`."""

    user: Required[User]
    """The unique identifiers retained after converting or merging."""

    visitor: Required[Visitor]
    """The unique identifiers to convert a single Visitor."""

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


class User(TypedDict, total=False):
    id: str
    """The unique identifier for the contact which is given by Intercom."""

    email: str
    """The contact's email, retained by default if one is present."""

    user_id: str
    """
    A unique identifier for the contact which is given to Intercom, which will be
    represented as external_id.
    """


class Visitor(TypedDict, total=False):
    id: str
    """The unique identifier for the contact which is given by Intercom."""

    email: str
    """The visitor's email."""

    user_id: str
    """A unique identifier for the contact which is given to Intercom."""
