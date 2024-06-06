# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["MessageCreateParams", "MessageTypeEmail", "MessageTypeInapp"]


class MessageTypeEmail(TypedDict, total=False):
    body: Required[object]


class MessageTypeInapp(TypedDict, total=False):
    body: Required[object]


MessageCreateParams = Union[MessageTypeEmail, MessageTypeInapp]
