# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConversationDeleted"]


class ConversationDeleted(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the conversation."""

    deleted: Optional[bool] = None
    """Whether the conversation is deleted or not."""

    object: Optional[Literal["conversation"]] = None
    """always conversation"""
