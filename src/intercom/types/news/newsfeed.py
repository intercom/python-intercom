# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Newsfeed"]


class Newsfeed(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the newsfeed which is given by Intercom."""

    created_at: Optional[int] = None
    """Timestamp for when the newsfeed was created."""

    name: Optional[str] = None
    """The name of the newsfeed. This name will never be visible to your users."""

    type: Optional[Literal["newsfeed"]] = None
    """The type of object."""

    updated_at: Optional[int] = None
    """Timestamp for when the newsfeed was last updated."""
