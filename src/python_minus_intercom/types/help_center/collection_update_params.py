# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ...types import shared_params
from ..._utils import PropertyInfo

__all__ = ["CollectionUpdateParams"]


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

    translated_content: Optional[shared_params.GroupTranslatedContent]
    """The Translated Content of an Group.

    The keys are the locale codes and the values are the translated content of the
    Group.
    """

    intercom_version: Annotated[
        Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ],
        PropertyInfo(alias="Intercom-Version"),
    ]
    """
    Intercom API version.By default, it's equal to the version set in the app
    package.
    """
