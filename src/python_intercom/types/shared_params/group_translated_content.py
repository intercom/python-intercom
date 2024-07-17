# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ...types import shared_params
from ..._utils import PropertyInfo

__all__ = ["GroupTranslatedContent"]


class GroupTranslatedContent(TypedDict, total=False):
    id: Optional[shared_params.GroupContent]
    """The content of the group in Indonesian"""

    ar: Optional[shared_params.GroupContent]
    """The content of the group in Arabic"""

    bg: Optional[shared_params.GroupContent]
    """The content of the group in Bulgarian"""

    bs: Optional[shared_params.GroupContent]
    """The content of the group in Bosnian"""

    ca: Optional[shared_params.GroupContent]
    """The content of the group in Catalan"""

    cs: Optional[shared_params.GroupContent]
    """The content of the group in Czech"""

    da: Optional[shared_params.GroupContent]
    """The content of the group in Danish"""

    de: Optional[shared_params.GroupContent]
    """The content of the group in German"""

    el: Optional[shared_params.GroupContent]
    """The content of the group in Greek"""

    en: Optional[shared_params.GroupContent]
    """The content of the group in English"""

    es: Optional[shared_params.GroupContent]
    """The content of the group in Spanish"""

    et: Optional[shared_params.GroupContent]
    """The content of the group in Estonian"""

    fi: Optional[shared_params.GroupContent]
    """The content of the group in Finnish"""

    fr: Optional[shared_params.GroupContent]
    """The content of the group in French"""

    he: Optional[shared_params.GroupContent]
    """The content of the group in Hebrew"""

    hr: Optional[shared_params.GroupContent]
    """The content of the group in Croatian"""

    hu: Optional[shared_params.GroupContent]
    """The content of the group in Hungarian"""

    it: Optional[shared_params.GroupContent]
    """The content of the group in Italian"""

    ja: Optional[shared_params.GroupContent]
    """The content of the group in Japanese"""

    ko: Optional[shared_params.GroupContent]
    """The content of the group in Korean"""

    lt: Optional[shared_params.GroupContent]
    """The content of the group in Lithuanian"""

    lv: Optional[shared_params.GroupContent]
    """The content of the group in Latvian"""

    mn: Optional[shared_params.GroupContent]
    """The content of the group in Mongolian"""

    nb: Optional[shared_params.GroupContent]
    """The content of the group in Norwegian"""

    nl: Optional[shared_params.GroupContent]
    """The content of the group in Dutch"""

    pl: Optional[shared_params.GroupContent]
    """The content of the group in Polish"""

    pt: Optional[shared_params.GroupContent]
    """The content of the group in Portuguese (Portugal)"""

    pt_br: Annotated[Optional[shared_params.GroupContent], PropertyInfo(alias="pt-BR")]
    """The content of the group in Portuguese (Brazil)"""

    ro: Optional[shared_params.GroupContent]
    """The content of the group in Romanian"""

    ru: Optional[shared_params.GroupContent]
    """The content of the group in Russian"""

    sl: Optional[shared_params.GroupContent]
    """The content of the group in Slovenian"""

    sr: Optional[shared_params.GroupContent]
    """The content of the group in Serbian"""

    sv: Optional[shared_params.GroupContent]
    """The content of the group in Swedish"""

    tr: Optional[shared_params.GroupContent]
    """The content of the group in Turkish"""

    type: Optional[Literal["group_translated_content"]]
    """The type of object - group_translated_content."""

    vi: Optional[shared_params.GroupContent]
    """The content of the group in Vietnamese"""

    zh_cn: Annotated[Optional[shared_params.GroupContent], PropertyInfo(alias="zh-CN")]
    """The content of the group in Chinese (China)"""

    zh_tw: Annotated[Optional[shared_params.GroupContent], PropertyInfo(alias="zh-TW")]
    """The content of the group in Chinese (Taiwan)"""
