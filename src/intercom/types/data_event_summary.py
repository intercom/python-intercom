# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataEventSummary", "Event"]


class Event(BaseModel):
    count: Optional[int] = None
    """The number of times the event was sent"""

    description: Optional[str] = None
    """The description of the event"""

    first: Optional[str] = None
    """The first time the event was sent"""

    last: Optional[str] = None
    """The last time the event was sent"""

    name: Optional[str] = None
    """The name of the event"""


class DataEventSummary(BaseModel):
    email: Optional[str] = None
    """The email address of the user"""

    events: Optional[List[Optional[Event]]] = None
    """A summary of data events"""

    intercom_user_id: Optional[str] = None
    """The Intercom user ID of the user"""

    type: Optional[Literal["event.summary"]] = None
    """The type of the object"""

    user_id: Optional[str] = None
    """The user ID of the user"""
