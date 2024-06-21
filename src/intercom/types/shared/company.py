# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .tag import Tag
from ..segment import Segment
from ..._models import BaseModel

__all__ = ["Company", "Plan", "Segments", "Tags"]


class Plan(BaseModel):
    id: Optional[str] = None
    """The id of the plan"""

    name: Optional[str] = None
    """The name of the plan"""

    type: Optional[str] = None
    """Value is always "plan" """


class Segments(BaseModel):
    segments: Optional[List[Segment]] = None

    type: Optional[Literal["segment.list"]] = None
    """The type of the object"""


class Tags(BaseModel):
    tags: Optional[List[Tag]] = None

    type: Optional[Literal["tag.list"]] = None
    """The type of the object"""


class Company(BaseModel):
    id: Optional[str] = None
    """The Intercom defined id representing the company."""

    app_id: Optional[str] = None
    """The Intercom defined code of the workspace the company is associated to."""

    company_id: Optional[str] = None
    """The company id you have defined for the company."""

    created_at: Optional[int] = None
    """The time the company was added in Intercom."""

    custom_attributes: Optional[Dict[str, str]] = None
    """The custom attributes you have set on the company."""

    industry: Optional[str] = None
    """The industry that the company operates in."""

    last_request_at: Optional[int] = None
    """The time the company last recorded making a request."""

    monthly_spend: Optional[int] = None
    """How much revenue the company generates for your business."""

    name: Optional[str] = None
    """The name of the company."""

    plan: Optional[Plan] = None

    remote_created_at: Optional[int] = None
    """The time the company was created by you."""

    segments: Optional[Segments] = None
    """The list of segments associated with the company"""

    session_count: Optional[int] = None
    """How many sessions the company has recorded."""

    size: Optional[int] = None
    """The number of employees in the company."""

    tags: Optional[Tags] = None
    """The list of tags associated with the company"""

    type: Optional[Literal["company"]] = None
    """Value is `company`"""

    updated_at: Optional[int] = None
    """The last time the company was updated."""

    user_count: Optional[int] = None
    """The number of users in the company."""

    website: Optional[str] = None
    """The URL for the company website."""
