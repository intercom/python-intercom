# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...types import shared_params

__all__ = ["CollectionCreateParams"]


class CollectionCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the collection.

    For multilingual collections, this will be the name of the default language's
    content.
    """

    description: str
    """The description of the collection.

    For multilingual collections, this will be the description of the default
    language's content.
    """

    help_center_id: Optional[int]
    """The id of the help center where the collection will be created.

    If `null` then it will be created in the default help center.
    """

    parent_id: Optional[str]
    """The id of the parent collection.

    If `null` then it will be created as the first level collection.
    """

    translated_content: Optional[shared_params.GroupTranslatedContent]
    """The Translated Content of an Group.

    The keys are the locale codes and the values are the translated content of the
    Group.
    """
