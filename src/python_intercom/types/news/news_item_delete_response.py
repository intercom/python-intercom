# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NewsItemDeleteResponse"]


class NewsItemDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the news item which you provided in the URL."""

    deleted: Optional[bool] = None
    """Whether the news item was deleted successfully or not."""

    object: Optional[Literal["news-item"]] = None
    """The type of object which was deleted - news-item."""
