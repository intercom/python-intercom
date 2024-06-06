# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ArticleContent"]


class ArticleContent(TypedDict, total=False):
    author_id: int
    """The ID of the author of the article."""

    body: str
    """The body of the article."""

    created_at: int
    """The time when the article was created."""

    description: str
    """The description of the article."""

    state: Literal["published", "draft"]
    """Whether the article is `published` or is a `draft` ."""

    title: str
    """The title of the article."""

    type: Optional[Literal["article_content"]]
    """The type of object - `article_content` ."""

    updated_at: int
    """The time when the article was last updated."""

    url: str
    """The URL of the article."""
