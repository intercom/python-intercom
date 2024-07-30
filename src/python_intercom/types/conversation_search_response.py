# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.conversation import Conversation
from .shared.cursor_pages import CursorPages

__all__ = ["ConversationSearchResponse"]


class ConversationSearchResponse(BaseModel):
    conversations: Optional[List[Conversation]] = None
    """The list of conversation objects"""

    pages: Optional[CursorPages] = None
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    total_count: Optional[int] = None
    """A count of the total number of objects."""

    type: Optional[Literal["conversation.list"]] = None
    """Always conversation.list"""
