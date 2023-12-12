# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeletedArticleObject"]


class DeletedArticleObject(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the article which you provided in the URL."""

    deleted: Optional[bool] = None
    """Whether the article was deleted successfully or not."""

    object: Optional[Literal["article"]] = None
    """The type of object which was deleted. - article"""
