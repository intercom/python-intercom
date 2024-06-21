# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

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
