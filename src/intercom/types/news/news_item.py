# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NewsItem", "NewsfeedAssignment"]


class NewsfeedAssignment(BaseModel):
    newsfeed_id: Optional[int] = None
    """The unique identifier for the newsfeed which is given by Intercom.

    Publish dates cannot be in the future, to schedule news items use the dedicated
    feature in app (see this article).
    """

    published_at: Optional[int] = None
    """
    Publish date of the news item on the newsfeed, use this field if you want to set
    a publish date in the past (e.g. when importing existing news items). On write,
    this field will be ignored if the news item state is "draft".
    """


class NewsItem(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the news item which is given by Intercom."""

    body: Optional[str] = None
    """The news item body, which may contain HTML."""

    cover_image_url: Optional[str] = None
    """URL of the image used as cover. Must have .jpg or .png extension."""

    created_at: Optional[int] = None
    """Timestamp for when the news item was created."""

    deliver_silently: Optional[bool] = None
    """
    When set to true, the news item will appear in the messenger newsfeed without
    showing a notification badge.
    """

    labels: Optional[List[Optional[str]]] = None
    """Label names displayed to users to categorize the news item."""

    newsfeed_assignments: Optional[List[NewsfeedAssignment]] = None
    """A list of newsfeed_assignments to assign to the specified newsfeed."""

    reactions: Optional[List[Optional[str]]] = None
    """Ordered list of emoji reactions to the news item.

    When empty, reactions are disabled.
    """

    sender_id: Optional[int] = None
    """The id of the sender of the news item. Must be a teammate on the workspace."""

    state: Optional[Literal["draft", "live"]] = None
    """
    News items will not be visible to your users in the assigned newsfeeds until
    they are set live.
    """

    title: Optional[str] = None
    """The title of the news item."""

    type: Optional[Literal["news-item"]] = None
    """The type of object."""

    updated_at: Optional[int] = None
    """Timestamp for when the news item was last updated."""

    workspace_id: Optional[str] = None
    """The id of the workspace which the news item belongs to."""
