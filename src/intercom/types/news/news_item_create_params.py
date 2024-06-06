# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["NewsItemCreateParams", "NewsfeedAssignment"]


class NewsItemCreateParams(TypedDict, total=False):
    sender_id: Required[int]
    """The id of the sender of the news item. Must be a teammate on the workspace."""

    title: Required[str]
    """The title of the news item."""

    body: str
    """The news item body, which may contain HTML."""

    deliver_silently: bool
    """
    When set to `true`, the news item will appear in the messenger newsfeed without
    showing a notification badge.
    """

    labels: List[str]
    """Label names displayed to users to categorize the news item."""

    newsfeed_assignments: Iterable[NewsfeedAssignment]
    """A list of newsfeed_assignments to assign to the specified newsfeed."""

    reactions: List[Optional[str]]
    """Ordered list of emoji reactions to the news item.

    When empty, reactions are disabled.
    """

    state: Literal["draft", "live"]
    """
    News items will not be visible to your users in the assigned newsfeeds until
    they are set live.
    """


class NewsfeedAssignment(TypedDict, total=False):
    newsfeed_id: int
    """The unique identifier for the newsfeed which is given by Intercom.

    Publish dates cannot be in the future, to schedule news items use the dedicated
    feature in app (see this article).
    """

    published_at: int
    """
    Publish date of the news item on the newsfeed, use this field if you want to set
    a publish date in the past (e.g. when importing existing news items). On write,
    this field will be ignored if the news item state is "draft".
    """
