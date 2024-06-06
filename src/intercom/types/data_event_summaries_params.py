# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DataEventSummariesParams", "EventSummaries"]


class DataEventSummariesParams(TypedDict, total=False):
    event_summaries: EventSummaries
    """A list of event summaries for the user.

    Each event summary should contain the event name, the time the event occurred,
    and the number of times the event occurred. The event name should be a past
    tense 'verb-noun' combination, to improve readability, for example
    `updated-plan`.
    """

    user_id: str
    """Your identifier for the user."""


class EventSummaries(TypedDict, total=False):
    count: int
    """The number of times the event occurred."""

    event_name: str
    """The name of the event that occurred.

    A good event name is typically a past tense 'verb-noun' combination, to improve
    readability, for example `updated-plan`.
    """

    first: int
    """The first time the event was sent"""

    last: int
    """The last time the event was sent"""
