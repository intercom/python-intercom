# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Article",
    "Statistics",
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


class Statistics(BaseModel):
    conversions: Optional[int] = None
    """The number of conversations started from the article."""

    happy_reaction_percentage: Optional[float] = None
    """
    The percentage of happy reactions the article has received against other types
    of reaction.
    """

    neutral_reaction_percentage: Optional[float] = None
    """
    The percentage of neutral reactions the article has received against other types
    of reaction.
    """

    reactions: Optional[int] = None
    """The number of total reactions the article has received."""

    sad_reaction_percentage: Optional[float] = None
    """
    The percentage of sad reactions the article has received against other types of
    reaction.
    """

    type: Optional[Literal["article_statistics"]] = None
    """The type of object - `article_statistics`."""

    views: Optional[int] = None
    """The number of total views the article has received."""


class TranslatedContentID(BaseModel):
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


class TranslatedContentAr(BaseModel):
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


class TranslatedContentBg(BaseModel):
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


class TranslatedContentBs(BaseModel):
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


class TranslatedContentCa(BaseModel):
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


class TranslatedContentCs(BaseModel):
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


class TranslatedContentDa(BaseModel):
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


class TranslatedContentDe(BaseModel):
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


class TranslatedContentEl(BaseModel):
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


class TranslatedContentEn(BaseModel):
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


class TranslatedContentEs(BaseModel):
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


class TranslatedContentEt(BaseModel):
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


class TranslatedContentFi(BaseModel):
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


class TranslatedContentFr(BaseModel):
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


class TranslatedContentHe(BaseModel):
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


class TranslatedContentHr(BaseModel):
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


class TranslatedContentHu(BaseModel):
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


class TranslatedContentIt(BaseModel):
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


class TranslatedContentJa(BaseModel):
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


class TranslatedContentKo(BaseModel):
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


class TranslatedContentLt(BaseModel):
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


class TranslatedContentLv(BaseModel):
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


class TranslatedContentMn(BaseModel):
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


class TranslatedContentNb(BaseModel):
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


class TranslatedContentNl(BaseModel):
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


class TranslatedContentPl(BaseModel):
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


class TranslatedContentPt(BaseModel):
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


class TranslatedContentPtBr(BaseModel):
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


class TranslatedContentRo(BaseModel):
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


class TranslatedContentRu(BaseModel):
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


class TranslatedContentSl(BaseModel):
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


class TranslatedContentSr(BaseModel):
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


class TranslatedContentSv(BaseModel):
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


class TranslatedContentTr(BaseModel):
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


class TranslatedContentVi(BaseModel):
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


class TranslatedContentZhCn(BaseModel):
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


class TranslatedContentZhTw(BaseModel):
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


class TranslatedContent(BaseModel):
    id: Optional[TranslatedContentID] = None
    """The content of the article in Indonesian"""

    ar: Optional[TranslatedContentAr] = None
    """The content of the article in Arabic"""

    bg: Optional[TranslatedContentBg] = None
    """The content of the article in Bulgarian"""

    bs: Optional[TranslatedContentBs] = None
    """The content of the article in Bosnian"""

    ca: Optional[TranslatedContentCa] = None
    """The content of the article in Catalan"""

    cs: Optional[TranslatedContentCs] = None
    """The content of the article in Czech"""

    da: Optional[TranslatedContentDa] = None
    """The content of the article in Danish"""

    de: Optional[TranslatedContentDe] = None
    """The content of the article in German"""

    el: Optional[TranslatedContentEl] = None
    """The content of the article in Greek"""

    en: Optional[TranslatedContentEn] = None
    """The content of the article in English"""

    es: Optional[TranslatedContentEs] = None
    """The content of the article in Spanish"""

    et: Optional[TranslatedContentEt] = None
    """The content of the article in Estonian"""

    fi: Optional[TranslatedContentFi] = None
    """The content of the article in Finnish"""

    fr: Optional[TranslatedContentFr] = None
    """The content of the article in French"""

    he: Optional[TranslatedContentHe] = None
    """The content of the article in Hebrew"""

    hr: Optional[TranslatedContentHr] = None
    """The content of the article in Croatian"""

    hu: Optional[TranslatedContentHu] = None
    """The content of the article in Hungarian"""

    it: Optional[TranslatedContentIt] = None
    """The content of the article in Italian"""

    ja: Optional[TranslatedContentJa] = None
    """The content of the article in Japanese"""

    ko: Optional[TranslatedContentKo] = None
    """The content of the article in Korean"""

    lt: Optional[TranslatedContentLt] = None
    """The content of the article in Lithuanian"""

    lv: Optional[TranslatedContentLv] = None
    """The content of the article in Latvian"""

    mn: Optional[TranslatedContentMn] = None
    """The content of the article in Mongolian"""

    nb: Optional[TranslatedContentNb] = None
    """The content of the article in Norwegian"""

    nl: Optional[TranslatedContentNl] = None
    """The content of the article in Dutch"""

    pl: Optional[TranslatedContentPl] = None
    """The content of the article in Polish"""

    pt: Optional[TranslatedContentPt] = None
    """The content of the article in Portuguese (Portugal)"""

    pt_br: Optional[TranslatedContentPtBr] = FieldInfo(alias="pt-BR", default=None)
    """The content of the article in Portuguese (Brazil)"""

    ro: Optional[TranslatedContentRo] = None
    """The content of the article in Romanian"""

    ru: Optional[TranslatedContentRu] = None
    """The content of the article in Russian"""

    sl: Optional[TranslatedContentSl] = None
    """The content of the article in Slovenian"""

    sr: Optional[TranslatedContentSr] = None
    """The content of the article in Serbian"""

    sv: Optional[TranslatedContentSv] = None
    """The content of the article in Swedish"""

    tr: Optional[TranslatedContentTr] = None
    """The content of the article in Turkish"""

    type: Optional[Literal["article_translated_content"]] = None
    """The type of object - article_translated_content."""

    vi: Optional[TranslatedContentVi] = None
    """The content of the article in Vietnamese"""

    zh_cn: Optional[TranslatedContentZhCn] = FieldInfo(alias="zh-CN", default=None)
    """The content of the article in Chinese (China)"""

    zh_tw: Optional[TranslatedContentZhTw] = FieldInfo(alias="zh-TW", default=None)
    """The content of the article in Chinese (Taiwan)"""


class Article(BaseModel):
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
    language's content.
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

    statistics: Optional[Statistics] = None
    """The statistics of an article."""

    title: Optional[str] = None
    """The title of the article.

    For multilingual articles, this will be the title of the default language's
    content.
    """

    translated_content: Optional[TranslatedContent] = None
    """The Translated Content of an Article.

    The keys are the locale codes and the values are the translated content of the
    article.
    """

    type: Optional[Literal["article"]] = None
    """The type of object - `article`."""

    updated_at: Optional[int] = None
    """The time when the article was last updated.

    For multilingual articles, this will be the timestamp of last update of the
    default language's content.
    """

    url: Optional[str] = None
    """The URL of the article.

    For multilingual articles, this will be the URL of the default language's
    content.
    """

    workspace_id: Optional[str] = None
    """The id of the workspace which the article belongs to."""
