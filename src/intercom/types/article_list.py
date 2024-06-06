# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.article_translated_content import ArticleTranslatedContent

__all__ = ["ArticleList", "Data", "Pages", "PagesNext"]


class Data(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the article which is given by Intercom."""

    author_id: Optional[int] = None
    """The id of the author of the article.

    For multilingual articles, this will be the id of the author of the default
    language's content. Must be a teammate on the help center's workspace.
    """

    body: Optional[str] = None
    """The body of the article in HTML.

    For multilingual articles, this will be the body of the default language's
    content.
    """

    created_at: Optional[int] = None
    """The time when the article was created.

    For multilingual articles, this will be the timestamp of creation of the default
    language's content in seconds.
    """

    default_locale: Optional[str] = None
    """The default locale of the help center.

    This field is only returned for multilingual help centers.
    """

    description: Optional[str] = None
    """The description of the article.

    For multilingual articles, this will be the description of the default
    language's content.
    """

    parent_id: Optional[int] = None
    """The id of the article's parent collection or section.

    An article without this field stands alone.
    """

    parent_ids: Optional[List[int]] = None
    """The ids of the article's parent collections or sections.

    An article without this field stands alone.
    """

    parent_type: Optional[str] = None
    """The type of parent, which can either be a `collection` or `section`."""

    state: Optional[Literal["published", "draft"]] = None
    """Whether the article is `published` or is a `draft`.

    For multilingual articles, this will be the state of the default language's
    content.
    """

    title: Optional[str] = None
    """The title of the article.

    For multilingual articles, this will be the title of the default language's
    content.
    """

    translated_content: Optional[ArticleTranslatedContent] = None
    """The Translated Content of an Article.

    The keys are the locale codes and the values are the translated content of the
    article.
    """

    type: Optional[Literal["article"]] = None
    """The type of object - `article`."""

    updated_at: Optional[int] = None
    """The time when the article was last updated.

    For multilingual articles, this will be the timestamp of last update of the
    default language's content in seconds.
    """

    url: Optional[str] = None
    """The URL of the article.

    For multilingual articles, this will be the URL of the default language's
    content.
    """

    workspace_id: Optional[str] = None
    """The id of the workspace which the article belongs to."""


class PagesNext(BaseModel):
    per_page: Optional[int] = None
    """The number of results to fetch per page."""

    starting_after: Optional[str] = None
    """The cursor to use in the next request to get the next page of results."""


class Pages(BaseModel):
    next: Optional[PagesNext] = None

    page: Optional[int] = None
    """The current page"""

    per_page: Optional[int] = None
    """Number of results per page"""

    total_pages: Optional[int] = None
    """Total number of pages"""

    type: Optional[Literal["pages"]] = None
    """the type of object `pages`."""


class ArticleList(BaseModel):
    data: Optional[List[Data]] = None
    """An array of Article objects"""

    pages: Optional[Pages] = None
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    total_count: Optional[int] = None
    """A count of the total number of articles."""

    type: Optional[Literal["list"]] = None
    """The type of the object - `list`."""
