# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Segment"]


class Segment(BaseModel):
    id: Optional[str] = None
    """The unique identifier representing the segment."""

    count: Optional[int] = None
    """The number of items in the user segment.

    It's returned when `include_count=true` is included in the request.
    """

    created_at: Optional[int] = None
    """The time the segment was created."""

    name: Optional[str] = None
    """The name of the segment."""

    person_type: Optional[Literal["contact", "user"]] = None
    """Type of the contact: contact (lead) or user."""

    type: Optional[Literal["segment"]] = None
    """The type of object."""

    updated_at: Optional[int] = None
    """The time the segment was updated."""
