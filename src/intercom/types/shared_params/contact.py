# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = [
    "Contact",
    "Avatar",
    "Companies",
    "Location",
    "Notes",
    "NotesData",
    "SocialProfiles",
    "SocialProfilesData",
    "Tags",
    "TagsData",
]


class Avatar(TypedDict, total=False):
    image_url: Optional[str]
    """An image URL containing the avatar of a contact."""

    type: str
    """The type of object"""


class Companies(TypedDict, total=False):
    has_more: bool
    """Whether there's more Addressable Objects to be viewed.

    If true, use the url to view all
    """

    total_count: int
    """Int representing the total number of companyies attached to this contact"""

    url: str
    """Url to get more company resources for this contact"""


class Location(TypedDict, total=False):
    city: Optional[str]
    """The city that the contact is located in"""

    country: Optional[str]
    """The country that the contact is located in"""

    region: Optional[str]
    """The overal region that the contact is located in"""

    type: Optional[str]
    """Always location"""


class NotesData(TypedDict, total=False):
    id: str
    """The id of the addressable object"""

    type: str
    """The addressable object type"""

    url: str
    """Url to get more company resources for this contact"""


class Notes(TypedDict, total=False):
    data: List[NotesData]
    """This object represents the notes attached to a contact."""

    has_more: bool
    """Whether there's more Addressable Objects to be viewed.

    If true, use the url to view all
    """

    total_count: int
    """Int representing the total number of companyies attached to this contact"""

    url: str
    """Url to get more company resources for this contact"""


class SocialProfilesData(TypedDict, total=False):
    name: str
    """The name of the Social media profile"""

    type: str
    """value is "social_profile" """

    url: str
    """The name of the Social media profile"""


class SocialProfiles(TypedDict, total=False):
    data: List[SocialProfilesData]
    """A list of social profiles objects associated with the contact."""


class TagsData(TypedDict, total=False):
    id: str
    """The id of the addressable object"""

    type: str
    """The addressable object type"""

    url: str
    """Url to get more company resources for this contact"""


class Tags(TypedDict, total=False):
    data: List[TagsData]
    """This object represents the tags attached to a contact."""

    has_more: bool
    """Whether there's more Addressable Objects to be viewed.

    If true, use the url to view all
    """

    total_count: int
    """Int representing the total number of tags attached to this contact"""

    url: str
    """url to get more tag resources for this contact"""


class Contact(TypedDict, total=False):
    id: str
    """The unique identifier for the contact which is given by Intercom."""

    android_app_name: Optional[str]
    """The name of the Android app which the contact is using."""

    android_app_version: Optional[str]
    """The version of the Android app which the contact is using."""

    android_device: Optional[str]
    """The Android device which the contact is using."""

    android_last_seen_at: Optional[int]
    """(UNIX timestamp) The time when the contact was last seen on an Android device."""

    android_os_version: Optional[str]
    """The version of the Android OS which the contact is using."""

    android_sdk_version: Optional[str]
    """The version of the Android SDK which the contact is using."""

    avatar: Optional[Avatar]

    browser: Optional[str]
    """The name of the browser which the contact is using."""

    browser_language: Optional[str]
    """The language set by the browser which the contact is using."""

    browser_version: Optional[str]
    """The version of the browser which the contact is using."""

    companies: Companies
    """
    An object containing companies meta data about the companies that a contact has.
    """

    created_at: int
    """(UNIX timestamp) The time when the contact was created."""

    custom_attributes: object
    """The custom attributes which are set for the contact."""

    email: str
    """The contacts email."""

    external_id: Optional[str]
    """The unique identifier for the contact which is provided by the Client."""

    formatted_phone: Optional[str]
    """The contacts phone number normalized to the E164 format"""

    has_hard_bounced: bool
    """Whether the contact has had an email sent to them hard bounce."""

    ios_app_name: Optional[str]
    """The name of the iOS app which the contact is using."""

    ios_app_version: Optional[str]
    """The version of the iOS app which the contact is using."""

    ios_device: Optional[str]
    """The iOS device which the contact is using."""

    ios_last_seen_at: Optional[int]
    """(UNIX timestamp) The last time the contact used the iOS app."""

    ios_os_version: Optional[str]
    """The version of iOS which the contact is using."""

    ios_sdk_version: Optional[str]
    """The version of the iOS SDK which the contact is using."""

    language_override: Optional[str]
    """
    A preferred language setting for the contact, used by the Intercom Messenger
    even if their browser settings change.
    """

    last_contacted_at: Optional[int]
    """(UNIX timestamp) The time when the contact was last messaged."""

    last_email_clicked_at: Optional[int]
    """(UNIX timestamp) The time when the contact last clicked a link in an email."""

    last_email_opened_at: Optional[int]
    """(UNIX timestamp) The time when the contact last opened an email."""

    last_replied_at: Optional[int]
    """(UNIX timestamp) The time when the contact last messaged in."""

    last_seen_at: Optional[int]
    """
    (UNIX timestamp) The time when the contact was last seen (either where the
    Intercom Messenger was installed or when specified manually).
    """

    location: Location
    """An object containing location meta data about a Intercom contact."""

    marked_email_as_spam: bool
    """Whether the contact has marked an email sent to them as spam."""

    name: Optional[str]
    """The contacts name."""

    notes: Notes
    """An object containing notes meta data about the notes that a contact has."""

    os: Optional[str]
    """The operating system which the contact is using."""

    owner_id: Optional[int]
    """The id of an admin that has been assigned account ownership of the contact."""

    phone: Optional[str]
    """The contacts phone."""

    role: str
    """The role of the contact."""

    signed_up_at: Optional[int]
    """(UNIX timestamp) The time specified for when a contact signed up."""

    social_profiles: SocialProfiles
    """An object containing social profiles that a contact has."""

    tags: Optional[Tags]
    """An object containing tags meta data about the tags that a contact has."""

    type: str
    """The type of object."""

    unsubscribed_from_emails: bool
    """Whether the contact is unsubscribed from emails."""

    updated_at: int
    """(UNIX timestamp) The time when the contact was last updated."""

    workspace_id: str
    """The id of the workspace which the contact belongs to."""
