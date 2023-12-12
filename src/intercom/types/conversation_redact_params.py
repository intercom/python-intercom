# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConversationRedactParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    conversation_id: Required[str]
    """The id of the conversation."""

    conversation_part_id: Required[str]
    """The id of the conversation_part."""

    type: Required[Literal["conversation_part"]]
    """The type of resource being redacted."""


class Variant1(TypedDict, total=False):
    conversation_id: Required[str]
    """The id of the conversation."""

    source_id: Required[str]
    """The id of the source."""

    type: Required[Literal["source"]]
    """The type of resource being redacted."""


ConversationRedactParams = Union[Variant0, Variant1]
