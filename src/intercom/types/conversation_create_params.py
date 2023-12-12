# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConversationCreateParams", "From"]


class ConversationCreateParams(TypedDict, total=False):
    body: Required[str]
    """The content of the message. HTML is not supported."""


class From(TypedDict, total=False):
    id: Required[str]
    """The identifier for the contact which is given by Intercom."""

    type: Required[Literal["lead", "user", "contact"]]
    """The role associated to the contact - user or lead."""
