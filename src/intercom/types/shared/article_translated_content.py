# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .article_content import ArticleContent

__all__ = ["ArticleTranslatedContent"]


class ArticleTranslatedContent(BaseModel):
    id: Optional[ArticleContent] = None
    """The content of the article in Indonesian"""

    ar: Optional[ArticleContent] = None
    """The content of the article in Arabic"""

    bg: Optional[ArticleContent] = None
    """The content of the article in Bulgarian"""

    bs: Optional[ArticleContent] = None
    """The content of the article in Bosnian"""

    ca: Optional[ArticleContent] = None
    """The content of the article in Catalan"""

    cs: Optional[ArticleContent] = None
    """The content of the article in Czech"""

    da: Optional[ArticleContent] = None
    """The content of the article in Danish"""

    de: Optional[ArticleContent] = None
    """The content of the article in German"""

    el: Optional[ArticleContent] = None
    """The content of the article in Greek"""

    en: Optional[ArticleContent] = None
    """The content of the article in English"""

    es: Optional[ArticleContent] = None
    """The content of the article in Spanish"""

    et: Optional[ArticleContent] = None
    """The content of the article in Estonian"""

    fi: Optional[ArticleContent] = None
    """The content of the article in Finnish"""

    fr: Optional[ArticleContent] = None
    """The content of the article in French"""

    he: Optional[ArticleContent] = None
    """The content of the article in Hebrew"""

    hr: Optional[ArticleContent] = None
    """The content of the article in Croatian"""

    hu: Optional[ArticleContent] = None
    """The content of the article in Hungarian"""

    it: Optional[ArticleContent] = None
    """The content of the article in Italian"""

    ja: Optional[ArticleContent] = None
    """The content of the article in Japanese"""

    ko: Optional[ArticleContent] = None
    """The content of the article in Korean"""

    lt: Optional[ArticleContent] = None
    """The content of the article in Lithuanian"""

    lv: Optional[ArticleContent] = None
    """The content of the article in Latvian"""

    mn: Optional[ArticleContent] = None
    """The content of the article in Mongolian"""

    nb: Optional[ArticleContent] = None
    """The content of the article in Norwegian"""

    nl: Optional[ArticleContent] = None
    """The content of the article in Dutch"""

    pl: Optional[ArticleContent] = None
    """The content of the article in Polish"""

    pt: Optional[ArticleContent] = None
    """The content of the article in Portuguese (Portugal)"""

    pt_br: Optional[ArticleContent] = FieldInfo(alias="pt-BR", default=None)
    """The content of the article in Portuguese (Brazil)"""

    ro: Optional[ArticleContent] = None
    """The content of the article in Romanian"""

    ru: Optional[ArticleContent] = None
    """The content of the article in Russian"""

    sl: Optional[ArticleContent] = None
    """The content of the article in Slovenian"""

    sr: Optional[ArticleContent] = None
    """The content of the article in Serbian"""

    sv: Optional[ArticleContent] = None
    """The content of the article in Swedish"""

    tr: Optional[ArticleContent] = None
    """The content of the article in Turkish"""

    type: Optional[Literal["article_translated_content"]] = None
    """The type of object - article_translated_content."""

    vi: Optional[ArticleContent] = None
    """The content of the article in Vietnamese"""

    zh_cn: Optional[ArticleContent] = FieldInfo(alias="zh-CN", default=None)
    """The content of the article in Chinese (China)"""

    zh_tw: Optional[ArticleContent] = FieldInfo(alias="zh-TW", default=None)
    """The content of the article in Chinese (Taiwan)"""
