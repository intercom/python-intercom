# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, TypedDict

from .segment import Segment
from ..segment import Segment

__all__ = ["Company", "Plan", "Segments", "Tags"]


class Plan(TypedDict, total=False):
    id: str
    """The id of the plan"""

    name: str
    """The name of the plan"""

    type: str
    """Value is always "plan" """


class Segments(TypedDict, total=False):
    segments: List[Segment]

    type: Literal["segment.list"]
    """The type of the object"""


class Tags(TypedDict, total=False):
    tags: List[object]

    type: Literal["tag.list"]
    """The type of the object"""


class Company(TypedDict, total=False):
    id: str
    """The Intercom defined id representing the company."""

    app_id: str
    """The Intercom defined code of the workspace the company is associated to."""

    company_id: str
    """The company id you have defined for the company."""

    created_at: int
    """The time the company was added in Intercom."""

    custom_attributes: Dict[str, str]
    """The custom attributes you have set on the company."""

    industry: str
    """The industry that the company operates in."""

    last_request_at: int
    """The time the company last recorded making a request."""

    monthly_spend: int
    """How much revenue the company generates for your business."""

    name: str
    """The name of the company."""

    plan: Plan

    remote_created_at: int
    """The time the company was created by you."""

    segments: Segments
    """The list of segments associated with the company"""

    session_count: int
    """How many sessions the company has recorded."""

    size: int
    """The number of employees in the company."""

    tags: Tags
    """The list of tags associated with the company"""

    type: Literal["company"]
    """Value is `company`"""

    updated_at: int
    """The last time the company was updated."""

    user_count: int
    """The number of users in the company."""

    website: str
    """The URL for the company website."""
