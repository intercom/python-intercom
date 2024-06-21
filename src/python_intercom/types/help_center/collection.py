# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.group_translated_content import GroupTranslatedContent

__all__ = ["Collection"]


class Collection(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the collection which is given by Intercom."""

    created_at: Optional[int] = None
    """The time when the article was created (seconds).

    For multilingual articles, this will be the timestamp of creation of the default
    language's content.
    """

    default_locale: Optional[str] = None
    """The default locale of the help center.

    This field is only returned for multilingual help centers.
    """

    description: Optional[str] = None
    """The description of the collection.

    For multilingual help centers, this will be the description of the collection
    for the default language.
    """

    help_center_id: Optional[int] = None
    """The id of the help center the collection is in."""

    icon: Optional[str] = None
    """The icon of the collection."""

    name: Optional[str] = None
    """The name of the collection.

    For multilingual collections, this will be the name of the default language's
    content.
    """

    order: Optional[int] = None
    """The order of the section in relation to others sections within a collection.

    Values go from `0` upwards. `0` is the default if there's no order.
    """

    parent_id: Optional[str] = None
    """The id of the parent collection.

    If `null` then it is the first level collection.
    """

    translated_content: Optional[GroupTranslatedContent] = None
    """The Translated Content of an Group.

    The keys are the locale codes and the values are the translated content of the
    Group.
    """

    updated_at: Optional[int] = None
    """The time when the article was last updated (seconds).

    For multilingual articles, this will be the timestamp of last update of the
    default language's content.
    """

    url: Optional[str] = None
    """The URL of the collection.

    For multilingual help centers, this will be the URL of the collection for the
    default language.
    """

    workspace_id: Optional[str] = None
    """The id of the workspace which the collection belongs to."""
