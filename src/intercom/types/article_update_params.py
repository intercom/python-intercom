# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..types import shared_params

__all__ = ["ArticleUpdateParams"]


class ArticleUpdateParams(TypedDict, total=False):
    author_id: int
    """The id of the author of the article.

    For multilingual articles, this will be the id of the author of the default
    language's content. Must be a teammate on the help center's workspace.
    """

    body: str
    """The content of the article.

    For multilingual articles, this will be the body of the default language's
    content.
    """

    description: str
    """The description of the article.

    For multilingual articles, this will be the description of the default
    language's content.
    """

    parent_id: str
    """The id of the article's parent collection or section.

    An article without this field stands alone.
    """

    parent_type: str
    """The type of parent, which can either be a `collection` or `section`."""

    state: Literal["published", "draft"]
    """Whether the article will be `published` or will be a `draft`.

    Defaults to draft. For multilingual articles, this will be the state of the
    default language's content.
    """

    title: str
    """
    The title of the article.For multilingual articles, this will be the title of
    the default language's content.
    """

    translated_content: Optional[shared_params.ArticleTranslatedContent]
    """The Translated Content of an Article.

    The keys are the locale codes and the values are the translated content of the
    article.
    """
