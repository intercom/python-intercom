# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

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
