# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ArticleCreateParams",
    "TranslatedContent",
    "TranslatedContentID",
    "TranslatedContentAr",
    "TranslatedContentBg",
    "TranslatedContentBs",
    "TranslatedContentCa",
    "TranslatedContentCs",
    "TranslatedContentDa",
    "TranslatedContentDe",
    "TranslatedContentEl",
    "TranslatedContentEn",
    "TranslatedContentEs",
    "TranslatedContentEt",
    "TranslatedContentFi",
    "TranslatedContentFr",
    "TranslatedContentHe",
    "TranslatedContentHr",
    "TranslatedContentHu",
    "TranslatedContentIt",
    "TranslatedContentJa",
    "TranslatedContentKo",
    "TranslatedContentLt",
    "TranslatedContentLv",
    "TranslatedContentMn",
    "TranslatedContentNb",
    "TranslatedContentNl",
    "TranslatedContentPl",
    "TranslatedContentPt",
    "TranslatedContentPtBr",
    "TranslatedContentRo",
    "TranslatedContentRu",
    "TranslatedContentSl",
    "TranslatedContentSr",
    "TranslatedContentSv",
    "TranslatedContentTr",
    "TranslatedContentVi",
    "TranslatedContentZhCn",
    "TranslatedContentZhTw",
]


class ArticleCreateParams(TypedDict, total=False):
    author_id: Required[int]
    """The id of the author of the article.

    For multilingual articles, this will be the id of the author of the default
    language's content. Must be a teammate on the help center's workspace.
    """

    title: Required[str]
    """
    The title of the article.For multilingual articles, this will be the title of
    the default language's content.
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

    parent_id: int
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

    translated_content: Optional[TranslatedContent]
    """The Translated Content of an Article.

    The keys are the locale codes and the values are the translated content of the
    article.
    """


class TranslatedContentID(TypedDict, total=False):
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


class TranslatedContentAr(TypedDict, total=False):
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


class TranslatedContentBg(TypedDict, total=False):
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


class TranslatedContentBs(TypedDict, total=False):
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


class TranslatedContentCa(TypedDict, total=False):
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


class TranslatedContentCs(TypedDict, total=False):
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


class TranslatedContentDa(TypedDict, total=False):
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


class TranslatedContentDe(TypedDict, total=False):
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


class TranslatedContentEl(TypedDict, total=False):
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


class TranslatedContentEn(TypedDict, total=False):
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


class TranslatedContentEs(TypedDict, total=False):
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


class TranslatedContentEt(TypedDict, total=False):
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


class TranslatedContentFi(TypedDict, total=False):
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


class TranslatedContentFr(TypedDict, total=False):
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


class TranslatedContentHe(TypedDict, total=False):
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


class TranslatedContentHr(TypedDict, total=False):
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


class TranslatedContentHu(TypedDict, total=False):
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


class TranslatedContentIt(TypedDict, total=False):
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


class TranslatedContentJa(TypedDict, total=False):
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


class TranslatedContentKo(TypedDict, total=False):
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


class TranslatedContentLt(TypedDict, total=False):
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


class TranslatedContentLv(TypedDict, total=False):
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


class TranslatedContentMn(TypedDict, total=False):
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


class TranslatedContentNb(TypedDict, total=False):
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


class TranslatedContentNl(TypedDict, total=False):
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


class TranslatedContentPl(TypedDict, total=False):
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


class TranslatedContentPt(TypedDict, total=False):
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


class TranslatedContentPtBr(TypedDict, total=False):
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


class TranslatedContentRo(TypedDict, total=False):
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


class TranslatedContentRu(TypedDict, total=False):
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


class TranslatedContentSl(TypedDict, total=False):
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


class TranslatedContentSr(TypedDict, total=False):
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


class TranslatedContentSv(TypedDict, total=False):
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


class TranslatedContentTr(TypedDict, total=False):
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


class TranslatedContentVi(TypedDict, total=False):
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


class TranslatedContentZhCn(TypedDict, total=False):
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


class TranslatedContentZhTw(TypedDict, total=False):
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


class TranslatedContent(TypedDict, total=False):
    id: Optional[TranslatedContentID]
    """The content of the article in Indonesian"""

    ar: Optional[TranslatedContentAr]
    """The content of the article in Arabic"""

    bg: Optional[TranslatedContentBg]
    """The content of the article in Bulgarian"""

    bs: Optional[TranslatedContentBs]
    """The content of the article in Bosnian"""

    ca: Optional[TranslatedContentCa]
    """The content of the article in Catalan"""

    cs: Optional[TranslatedContentCs]
    """The content of the article in Czech"""

    da: Optional[TranslatedContentDa]
    """The content of the article in Danish"""

    de: Optional[TranslatedContentDe]
    """The content of the article in German"""

    el: Optional[TranslatedContentEl]
    """The content of the article in Greek"""

    en: Optional[TranslatedContentEn]
    """The content of the article in English"""

    es: Optional[TranslatedContentEs]
    """The content of the article in Spanish"""

    et: Optional[TranslatedContentEt]
    """The content of the article in Estonian"""

    fi: Optional[TranslatedContentFi]
    """The content of the article in Finnish"""

    fr: Optional[TranslatedContentFr]
    """The content of the article in French"""

    he: Optional[TranslatedContentHe]
    """The content of the article in Hebrew"""

    hr: Optional[TranslatedContentHr]
    """The content of the article in Croatian"""

    hu: Optional[TranslatedContentHu]
    """The content of the article in Hungarian"""

    it: Optional[TranslatedContentIt]
    """The content of the article in Italian"""

    ja: Optional[TranslatedContentJa]
    """The content of the article in Japanese"""

    ko: Optional[TranslatedContentKo]
    """The content of the article in Korean"""

    lt: Optional[TranslatedContentLt]
    """The content of the article in Lithuanian"""

    lv: Optional[TranslatedContentLv]
    """The content of the article in Latvian"""

    mn: Optional[TranslatedContentMn]
    """The content of the article in Mongolian"""

    nb: Optional[TranslatedContentNb]
    """The content of the article in Norwegian"""

    nl: Optional[TranslatedContentNl]
    """The content of the article in Dutch"""

    pl: Optional[TranslatedContentPl]
    """The content of the article in Polish"""

    pt: Optional[TranslatedContentPt]
    """The content of the article in Portuguese (Portugal)"""

    pt_br: Annotated[Optional[TranslatedContentPtBr], PropertyInfo(alias="pt-BR")]
    """The content of the article in Portuguese (Brazil)"""

    ro: Optional[TranslatedContentRo]
    """The content of the article in Romanian"""

    ru: Optional[TranslatedContentRu]
    """The content of the article in Russian"""

    sl: Optional[TranslatedContentSl]
    """The content of the article in Slovenian"""

    sr: Optional[TranslatedContentSr]
    """The content of the article in Serbian"""

    sv: Optional[TranslatedContentSv]
    """The content of the article in Swedish"""

    tr: Optional[TranslatedContentTr]
    """The content of the article in Turkish"""

    type: Optional[Literal["article_translated_content"]]
    """The type of object - article_translated_content."""

    vi: Optional[TranslatedContentVi]
    """The content of the article in Vietnamese"""

    zh_cn: Annotated[Optional[TranslatedContentZhCn], PropertyInfo(alias="zh-CN")]
    """The content of the article in Chinese (China)"""

    zh_tw: Annotated[Optional[TranslatedContentZhTw], PropertyInfo(alias="zh-TW")]
    """The content of the article in Chinese (Taiwan)"""
