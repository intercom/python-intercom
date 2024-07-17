# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ...types import shared_params
from ..._utils import PropertyInfo

__all__ = ["ArticleTranslatedContent"]


class ArticleTranslatedContent(TypedDict, total=False):
    id: Optional[shared_params.ArticleContent]
    """The content of the article in Indonesian"""

    ar: Optional[shared_params.ArticleContent]
    """The content of the article in Arabic"""

    bg: Optional[shared_params.ArticleContent]
    """The content of the article in Bulgarian"""

    bs: Optional[shared_params.ArticleContent]
    """The content of the article in Bosnian"""

    ca: Optional[shared_params.ArticleContent]
    """The content of the article in Catalan"""

    cs: Optional[shared_params.ArticleContent]
    """The content of the article in Czech"""

    da: Optional[shared_params.ArticleContent]
    """The content of the article in Danish"""

    de: Optional[shared_params.ArticleContent]
    """The content of the article in German"""

    el: Optional[shared_params.ArticleContent]
    """The content of the article in Greek"""

    en: Optional[shared_params.ArticleContent]
    """The content of the article in English"""

    es: Optional[shared_params.ArticleContent]
    """The content of the article in Spanish"""

    et: Optional[shared_params.ArticleContent]
    """The content of the article in Estonian"""

    fi: Optional[shared_params.ArticleContent]
    """The content of the article in Finnish"""

    fr: Optional[shared_params.ArticleContent]
    """The content of the article in French"""

    he: Optional[shared_params.ArticleContent]
    """The content of the article in Hebrew"""

    hr: Optional[shared_params.ArticleContent]
    """The content of the article in Croatian"""

    hu: Optional[shared_params.ArticleContent]
    """The content of the article in Hungarian"""

    it: Optional[shared_params.ArticleContent]
    """The content of the article in Italian"""

    ja: Optional[shared_params.ArticleContent]
    """The content of the article in Japanese"""

    ko: Optional[shared_params.ArticleContent]
    """The content of the article in Korean"""

    lt: Optional[shared_params.ArticleContent]
    """The content of the article in Lithuanian"""

    lv: Optional[shared_params.ArticleContent]
    """The content of the article in Latvian"""

    mn: Optional[shared_params.ArticleContent]
    """The content of the article in Mongolian"""

    nb: Optional[shared_params.ArticleContent]
    """The content of the article in Norwegian"""

    nl: Optional[shared_params.ArticleContent]
    """The content of the article in Dutch"""

    pl: Optional[shared_params.ArticleContent]
    """The content of the article in Polish"""

    pt: Optional[shared_params.ArticleContent]
    """The content of the article in Portuguese (Portugal)"""

    pt_br: Annotated[Optional[shared_params.ArticleContent], PropertyInfo(alias="pt-BR")]
    """The content of the article in Portuguese (Brazil)"""

    ro: Optional[shared_params.ArticleContent]
    """The content of the article in Romanian"""

    ru: Optional[shared_params.ArticleContent]
    """The content of the article in Russian"""

    sl: Optional[shared_params.ArticleContent]
    """The content of the article in Slovenian"""

    sr: Optional[shared_params.ArticleContent]
    """The content of the article in Serbian"""

    sv: Optional[shared_params.ArticleContent]
    """The content of the article in Swedish"""

    tr: Optional[shared_params.ArticleContent]
    """The content of the article in Turkish"""

    type: Optional[Literal["article_translated_content"]]
    """The type of object - article_translated_content."""

    vi: Optional[shared_params.ArticleContent]
    """The content of the article in Vietnamese"""

    zh_cn: Annotated[Optional[shared_params.ArticleContent], PropertyInfo(alias="zh-CN")]
    """The content of the article in Chinese (China)"""

    zh_tw: Annotated[Optional[shared_params.ArticleContent], PropertyInfo(alias="zh-TW")]
    """The content of the article in Chinese (Taiwan)"""
