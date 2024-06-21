# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .group_content import GroupContent

__all__ = ["GroupTranslatedContent"]


class GroupTranslatedContent(BaseModel):
    id: Optional[GroupContent] = None
    """The content of the group in Indonesian"""

    ar: Optional[GroupContent] = None
    """The content of the group in Arabic"""

    bg: Optional[GroupContent] = None
    """The content of the group in Bulgarian"""

    bs: Optional[GroupContent] = None
    """The content of the group in Bosnian"""

    ca: Optional[GroupContent] = None
    """The content of the group in Catalan"""

    cs: Optional[GroupContent] = None
    """The content of the group in Czech"""

    da: Optional[GroupContent] = None
    """The content of the group in Danish"""

    de: Optional[GroupContent] = None
    """The content of the group in German"""

    el: Optional[GroupContent] = None
    """The content of the group in Greek"""

    en: Optional[GroupContent] = None
    """The content of the group in English"""

    es: Optional[GroupContent] = None
    """The content of the group in Spanish"""

    et: Optional[GroupContent] = None
    """The content of the group in Estonian"""

    fi: Optional[GroupContent] = None
    """The content of the group in Finnish"""

    fr: Optional[GroupContent] = None
    """The content of the group in French"""

    he: Optional[GroupContent] = None
    """The content of the group in Hebrew"""

    hr: Optional[GroupContent] = None
    """The content of the group in Croatian"""

    hu: Optional[GroupContent] = None
    """The content of the group in Hungarian"""

    it: Optional[GroupContent] = None
    """The content of the group in Italian"""

    ja: Optional[GroupContent] = None
    """The content of the group in Japanese"""

    ko: Optional[GroupContent] = None
    """The content of the group in Korean"""

    lt: Optional[GroupContent] = None
    """The content of the group in Lithuanian"""

    lv: Optional[GroupContent] = None
    """The content of the group in Latvian"""

    mn: Optional[GroupContent] = None
    """The content of the group in Mongolian"""

    nb: Optional[GroupContent] = None
    """The content of the group in Norwegian"""

    nl: Optional[GroupContent] = None
    """The content of the group in Dutch"""

    pl: Optional[GroupContent] = None
    """The content of the group in Polish"""

    pt: Optional[GroupContent] = None
    """The content of the group in Portuguese (Portugal)"""

    pt_br: Optional[GroupContent] = FieldInfo(alias="pt-BR", default=None)
    """The content of the group in Portuguese (Brazil)"""

    ro: Optional[GroupContent] = None
    """The content of the group in Romanian"""

    ru: Optional[GroupContent] = None
    """The content of the group in Russian"""

    sl: Optional[GroupContent] = None
    """The content of the group in Slovenian"""

    sr: Optional[GroupContent] = None
    """The content of the group in Serbian"""

    sv: Optional[GroupContent] = None
    """The content of the group in Swedish"""

    tr: Optional[GroupContent] = None
    """The content of the group in Turkish"""

    type: Optional[Literal["group_translated_content"]] = None
    """The type of object - group_translated_content."""

    vi: Optional[GroupContent] = None
    """The content of the group in Vietnamese"""

    zh_cn: Optional[GroupContent] = FieldInfo(alias="zh-CN", default=None)
    """The content of the group in Chinese (China)"""

    zh_tw: Optional[GroupContent] = FieldInfo(alias="zh-TW", default=None)
    """The content of the group in Chinese (Taiwan)"""
