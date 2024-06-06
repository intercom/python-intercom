# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ArticleContent"]


class ArticleContent(BaseModel):
    author_id: Optional[int] = None
    """The ID of the author of the article."""

    body: Optional[str] = None
    """The body of the article."""

    created_at: Optional[int] = None
    """The time when the article was created."""

    description: Optional[str] = None
    """The description of the article."""

    state: Optional[Literal["published", "draft"]] = None
    """Whether the article is `published` or is a `draft` ."""

    title: Optional[str] = None
    """The title of the article."""

    type: Optional[Literal["article_content"]] = None
    """The type of object - `article_content` ."""

    updated_at: Optional[int] = None
    """The time when the article was last updated."""

    url: Optional[str] = None
    """The URL of the article."""
