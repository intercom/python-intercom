# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversationCreateParams", "From"]


class ConversationCreateParams(TypedDict, total=False):
    body: Required[str]
    """The content of the message. HTML is not supported."""

    from_: Required[Annotated[From, PropertyInfo(alias="from")]]


class From(TypedDict, total=False):
    id: Required[str]
    """The identifier for the contact which is given by Intercom."""

    type: Required[Literal["lead", "user", "contact"]]
    """The role associated to the contact - user or lead."""
