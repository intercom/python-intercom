# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["HelpCenter"]


class HelpCenter(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the Help Center which is given by Intercom."""

    created_at: Optional[int] = None
    """The time when the Help Center was created."""

    display_name: Optional[str] = None
    """The display name of the Help Center only seen by teammates."""

    identifier: Optional[str] = None
    """The identifier of the Help Center. This is used in the URL of the Help Center."""

    updated_at: Optional[int] = None
    """The time when the Help Center was last updated."""

    website_turned_on: Optional[bool] = None
    """Whether the Help Center is turned on or not.

    This is controlled in your Help Center settings.
    """

    workspace_id: Optional[str] = None
    """The id of the workspace which the Help Center belongs to."""
