# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

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


class Avatar(BaseModel):
    image_url: Optional[str] = None
    """An image URL containing the avatar of a contact."""

    type: Optional[str] = None
    """The type of object"""


class Companies(BaseModel):
    has_more: Optional[bool] = None
    """Whether there's more Addressable Objects to be viewed.

    If true, use the url to view all
    """

    total_count: Optional[int] = None
    """Int representing the total number of companyies attached to this contact"""

    url: Optional[str] = None
    """Url to get more company resources for this contact"""


class Location(BaseModel):
    city: Optional[str] = None
    """The city that the contact is located in"""

    country: Optional[str] = None
    """The country that the contact is located in"""

    region: Optional[str] = None
    """The overal region that the contact is located in"""

    type: Optional[str] = None
    """Always location"""


class NotesData(BaseModel):
    id: Optional[str] = None
    """The id of the addressable object"""

    type: Optional[str] = None
    """The addressable object type"""

    url: Optional[str] = None
    """Url to get more company resources for this contact"""


class Notes(BaseModel):
    data: Optional[List[NotesData]] = None
    """This object represents the notes attached to a contact."""

    has_more: Optional[bool] = None
    """Whether there's more Addressable Objects to be viewed.

    If true, use the url to view all
    """

    total_count: Optional[int] = None
    """Int representing the total number of companyies attached to this contact"""

    url: Optional[str] = None
    """Url to get more company resources for this contact"""


class SocialProfilesData(BaseModel):
    name: Optional[str] = None
    """The name of the Social media profile"""

    type: Optional[str] = None
    """value is "social_profile" """

    url: Optional[str] = None
    """The name of the Social media profile"""


class SocialProfiles(BaseModel):
    data: Optional[List[SocialProfilesData]] = None
    """A list of social profiles objects associated with the contact."""


class TagsData(BaseModel):
    id: Optional[str] = None
    """The id of the addressable object"""

    type: Optional[str] = None
    """The addressable object type"""

    url: Optional[str] = None
    """Url to get more company resources for this contact"""


class Tags(BaseModel):
    data: Optional[List[TagsData]] = None
    """This object represents the tags attached to a contact."""

    has_more: Optional[bool] = None
    """Whether there's more Addressable Objects to be viewed.

    If true, use the url to view all
    """

    total_count: Optional[int] = None
    """Int representing the total number of tags attached to this contact"""

    url: Optional[str] = None
    """url to get more tag resources for this contact"""


class Contact(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the contact which is given by Intercom."""

    android_app_name: Optional[str] = None
    """The name of the Android app which the contact is using."""

    android_app_version: Optional[str] = None
    """The version of the Android app which the contact is using."""

    android_device: Optional[str] = None
    """The Android device which the contact is using."""

    android_last_seen_at: Optional[int] = None
    """(UNIX timestamp) The time when the contact was last seen on an Android device."""

    android_os_version: Optional[str] = None
    """The version of the Android OS which the contact is using."""

    android_sdk_version: Optional[str] = None
    """The version of the Android SDK which the contact is using."""

    avatar: Optional[Avatar] = None

    browser: Optional[str] = None
    """The name of the browser which the contact is using."""

    browser_language: Optional[str] = None
    """The language set by the browser which the contact is using."""

    browser_version: Optional[str] = None
    """The version of the browser which the contact is using."""

    companies: Optional[Companies] = None
    """
    An object containing companies meta data about the companies that a contact has.
    """

    created_at: Optional[int] = None
    """(UNIX timestamp) The time when the contact was created."""

    custom_attributes: Optional[object] = None
    """The custom attributes which are set for the contact."""

    email: Optional[str] = None
    """The contacts email."""

    external_id: Optional[str] = None
    """The unique identifier for the contact which is provided by the Client."""

    formatted_phone: Optional[str] = None
    """The contacts phone number normalized to the E164 format"""

    has_hard_bounced: Optional[bool] = None
    """Whether the contact has had an email sent to them hard bounce."""

    ios_app_name: Optional[str] = None
    """The name of the iOS app which the contact is using."""

    ios_app_version: Optional[str] = None
    """The version of the iOS app which the contact is using."""

    ios_device: Optional[str] = None
    """The iOS device which the contact is using."""

    ios_last_seen_at: Optional[int] = None
    """(UNIX timestamp) The last time the contact used the iOS app."""

    ios_os_version: Optional[str] = None
    """The version of iOS which the contact is using."""

    ios_sdk_version: Optional[str] = None
    """The version of the iOS SDK which the contact is using."""

    language_override: Optional[str] = None
    """
    A preferred language setting for the contact, used by the Intercom Messenger
    even if their browser settings change.
    """

    last_contacted_at: Optional[int] = None
    """(UNIX timestamp) The time when the contact was last messaged."""

    last_email_clicked_at: Optional[int] = None
    """(UNIX timestamp) The time when the contact last clicked a link in an email."""

    last_email_opened_at: Optional[int] = None
    """(UNIX timestamp) The time when the contact last opened an email."""

    last_replied_at: Optional[int] = None
    """(UNIX timestamp) The time when the contact last messaged in."""

    last_seen_at: Optional[int] = None
    """
    (UNIX timestamp) The time when the contact was last seen (either where the
    Intercom Messenger was installed or when specified manually).
    """

    location: Optional[Location] = None
    """An object containing location meta data about a Intercom contact."""

    marked_email_as_spam: Optional[bool] = None
    """Whether the contact has marked an email sent to them as spam."""

    name: Optional[str] = None
    """The contacts name."""

    notes: Optional[Notes] = None
    """An object containing notes meta data about the notes that a contact has."""

    os: Optional[str] = None
    """The operating system which the contact is using."""

    owner_id: Optional[int] = None
    """The id of an admin that has been assigned account ownership of the contact."""

    phone: Optional[str] = None
    """The contacts phone."""

    role: Optional[str] = None
    """The role of the contact."""

    signed_up_at: Optional[int] = None
    """(UNIX timestamp) The time specified for when a contact signed up."""

    social_profiles: Optional[SocialProfiles] = None
    """An object containing social profiles that a contact has."""

    tags: Optional[Tags] = None
    """An object containing tags meta data about the tags that a contact has."""

    type: Optional[str] = None
    """The type of object."""

    unsubscribed_from_emails: Optional[bool] = None
    """Whether the contact is unsubscribed from emails."""

    updated_at: Optional[int] = None
    """(UNIX timestamp) The time when the contact was last updated."""

    workspace_id: Optional[str] = None
    """The id of the workspace which the contact belongs to."""
