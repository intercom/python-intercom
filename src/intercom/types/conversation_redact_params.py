# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversationRedactParams", "RedactConversationPartRequest", "RedactConversationSourceRequest"]


class RedactConversationPartRequest(TypedDict, total=False):
    conversation_id: Required[str]
    """The id of the conversation."""

    conversation_part_id: Required[str]
    """The id of the conversation_part."""

    type: Required[Literal["conversation_part"]]
    """The type of resource being redacted."""

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


class RedactConversationSourceRequest(TypedDict, total=False):
    conversation_id: Required[str]
    """The id of the conversation."""

    source_id: Required[str]
    """The id of the source."""

    type: Required[Literal["source"]]
    """The type of resource being redacted."""

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


ConversationRedactParams = Union[RedactConversationPartRequest, RedactConversationSourceRequest]
