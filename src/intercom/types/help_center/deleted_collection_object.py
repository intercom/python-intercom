# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DeletedCollectionObject"]


class DeletedCollectionObject(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the collection which you provided in the URL."""

    deleted: Optional[bool] = None
    """Whether the collection was deleted successfully or not."""

    object: Optional[Literal["collection"]] = None
    """The type of object which was deleted. - `collection`"""
