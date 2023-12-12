# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CollectionUpdateParams",
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


class CollectionUpdateParams(TypedDict, total=False):
    description: str
    """The description of the collection.

    For multilingual collections, this will be the description of the default
    language's content.
    """

    name: str
    """The name of the collection.

    For multilingual collections, this will be the name of the default language's
    content.
    """

    parent_id: Optional[str]
    """The id of the parent collection.

    If `null` then it will be updated as the first level collection.
    """

    translated_content: Optional[TranslatedContent]
    """The Translated Content of an Group.

    The keys are the locale codes and the values are the translated content of the
    Group.
    """


class TranslatedContentID(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentAr(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentBg(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentBs(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentCa(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentCs(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentDa(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentDe(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentEl(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentEn(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentEs(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentEt(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentFi(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentFr(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentHe(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentHr(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentHu(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentIt(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentJa(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentKo(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentLt(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentLv(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentMn(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentNb(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentNl(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentPl(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentPt(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentPtBr(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentRo(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentRu(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentSl(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentSr(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentSv(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentTr(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentVi(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentZhCn(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContentZhTw(TypedDict, total=False):
    description: str
    """The description of the collection. Only available for collections."""

    name: str
    """The name of the collection or section."""

    type: Optional[Literal["group_content"]]
    """The type of object - `group_content` ."""


class TranslatedContent(TypedDict, total=False):
    id: Optional[TranslatedContentID]
    """The content of the group in Indonesian"""

    ar: Optional[TranslatedContentAr]
    """The content of the group in Arabic"""

    bg: Optional[TranslatedContentBg]
    """The content of the group in Bulgarian"""

    bs: Optional[TranslatedContentBs]
    """The content of the group in Bosnian"""

    ca: Optional[TranslatedContentCa]
    """The content of the group in Catalan"""

    cs: Optional[TranslatedContentCs]
    """The content of the group in Czech"""

    da: Optional[TranslatedContentDa]
    """The content of the group in Danish"""

    de: Optional[TranslatedContentDe]
    """The content of the group in German"""

    el: Optional[TranslatedContentEl]
    """The content of the group in Greek"""

    en: Optional[TranslatedContentEn]
    """The content of the group in English"""

    es: Optional[TranslatedContentEs]
    """The content of the group in Spanish"""

    et: Optional[TranslatedContentEt]
    """The content of the group in Estonian"""

    fi: Optional[TranslatedContentFi]
    """The content of the group in Finnish"""

    fr: Optional[TranslatedContentFr]
    """The content of the group in French"""

    he: Optional[TranslatedContentHe]
    """The content of the group in Hebrew"""

    hr: Optional[TranslatedContentHr]
    """The content of the group in Croatian"""

    hu: Optional[TranslatedContentHu]
    """The content of the group in Hungarian"""

    it: Optional[TranslatedContentIt]
    """The content of the group in Italian"""

    ja: Optional[TranslatedContentJa]
    """The content of the group in Japanese"""

    ko: Optional[TranslatedContentKo]
    """The content of the group in Korean"""

    lt: Optional[TranslatedContentLt]
    """The content of the group in Lithuanian"""

    lv: Optional[TranslatedContentLv]
    """The content of the group in Latvian"""

    mn: Optional[TranslatedContentMn]
    """The content of the group in Mongolian"""

    nb: Optional[TranslatedContentNb]
    """The content of the group in Norwegian"""

    nl: Optional[TranslatedContentNl]
    """The content of the group in Dutch"""

    pl: Optional[TranslatedContentPl]
    """The content of the group in Polish"""

    pt: Optional[TranslatedContentPt]
    """The content of the group in Portuguese (Portugal)"""

    pt_br: Annotated[Optional[TranslatedContentPtBr], PropertyInfo(alias="pt-BR")]
    """The content of the group in Portuguese (Brazil)"""

    ro: Optional[TranslatedContentRo]
    """The content of the group in Romanian"""

    ru: Optional[TranslatedContentRu]
    """The content of the group in Russian"""

    sl: Optional[TranslatedContentSl]
    """The content of the group in Slovenian"""

    sr: Optional[TranslatedContentSr]
    """The content of the group in Serbian"""

    sv: Optional[TranslatedContentSv]
    """The content of the group in Swedish"""

    tr: Optional[TranslatedContentTr]
    """The content of the group in Turkish"""

    type: Optional[Literal["group_translated_content"]]
    """The type of object - group_translated_content."""

    vi: Optional[TranslatedContentVi]
    """The content of the group in Vietnamese"""

    zh_cn: Annotated[Optional[TranslatedContentZhCn], PropertyInfo(alias="zh-CN")]
    """The content of the group in Chinese (China)"""

    zh_tw: Annotated[Optional[TranslatedContentZhTw], PropertyInfo(alias="zh-TW")]
    """The content of the group in Chinese (Taiwan)"""
