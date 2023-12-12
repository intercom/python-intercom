# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ContactUpdateParams"]


class ContactUpdateParams(TypedDict, total=False):
    avatar: Optional[str]
    """An image URL containing the avatar of a contact"""

    custom_attributes: Optional[object]
    """The custom attributes which are set for the contact"""

    email: str
    """The contacts email"""

    external_id: str
    """A unique identifier for the contact which is given to Intercom"""

    last_seen_at: Optional[int]
    """
    The time when the contact was last seen (either where the Intercom Messenger was
    installed or when specified manually)
    """

    name: Optional[str]
    """The contacts name"""

    owner_id: Optional[int]
    """The id of an admin that has been assigned account ownership of the contact"""

    phone: Optional[str]
    """The contacts phone"""

    role: str
    """The role of the contact."""

    signed_up_at: Optional[int]
    """The time specified for when a contact signed up"""

    unsubscribed_from_emails: Optional[bool]
    """Whether the contact is unsubscribed from emails"""
