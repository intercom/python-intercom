# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .shared import Company
from .._models import BaseModel

__all__ = ["Visitor", "Avatar", "Companies", "LocationData", "Segments", "SocialProfiles", "Tags", "TagsTag"]


class Avatar(BaseModel):
    image_url: Optional[str] = None
    """This object represents the avatar associated with the visitor."""

    type: Optional[str] = None


class Companies(BaseModel):
    companies: Optional[List[Company]] = None

    type: Optional[Literal["company.list"]] = None
    """The type of the object"""


class LocationData(BaseModel):
    city_name: Optional[str] = None
    """The city name of the visitor."""

    continent_code: Optional[str] = None
    """The continent code of the visitor."""

    country_code: Optional[str] = None
    """The country code of the visitor."""

    country_name: Optional[str] = None
    """The country name of the visitor."""

    postal_code: Optional[str] = None
    """The postal code of the visitor."""

    region_name: Optional[str] = None
    """The region name of the visitor."""

    timezone: Optional[str] = None
    """The timezone of the visitor."""

    type: Optional[str] = None


class Segments(BaseModel):
    segments: Optional[List[str]] = None

    type: Optional[Literal["segment.list"]] = None
    """The type of the object"""


class SocialProfiles(BaseModel):
    social_profiles: Optional[List[str]] = None

    type: Optional[Literal["social_profile.list"]] = None
    """The type of the object"""


class TagsTag(BaseModel):
    id: Optional[str] = None
    """The id of the tag."""

    name: Optional[str] = None
    """The name of the tag."""

    type: Optional[Literal["tag"]] = None
    """The type of the object"""


class Tags(BaseModel):
    tags: Optional[List[TagsTag]] = None

    type: Optional[Literal["tag.list"]] = None
    """The type of the object"""


class Visitor(BaseModel):
    id: Optional[str] = None
    """The Intercom defined id representing the Visitor."""

    anonymous: Optional[bool] = None
    """Identifies if this visitor is anonymous."""

    app_id: Optional[str] = None
    """The id of the app the visitor is associated with."""

    avatar: Optional[Avatar] = None

    companies: Optional[Companies] = None

    created_at: Optional[int] = None
    """The time the Visitor was added to Intercom."""

    custom_attributes: Optional[Dict[str, str]] = None
    """The custom attributes you have set on the Visitor."""

    do_not_track: Optional[bool] = None
    """Identifies if this visitor has do not track enabled."""

    email: Optional[str] = None
    """The email of the visitor."""

    has_hard_bounced: Optional[bool] = None
    """Identifies if this visitor has had a hard bounce."""

    las_request_at: Optional[int] = None
    """The time the Lead last recorded making a request."""

    location_data: Optional[LocationData] = None

    marked_email_as_spam: Optional[bool] = None
    """Identifies if this visitor has marked an email as spam."""

    name: Optional[str] = None
    """The name of the visitor."""

    owner_id: Optional[str] = None
    """The id of the admin that owns the Visitor."""

    phone: Optional[str] = None
    """The phone number of the visitor."""

    pseudonym: Optional[str] = None
    """The pseudonym of the visitor."""

    referrer: Optional[str] = None
    """The referer of the visitor."""

    remote_created_at: Optional[int] = None
    """The time the Visitor was added to Intercom."""

    segments: Optional[Segments] = None

    session_count: Optional[int] = None
    """The number of sessions the Visitor has had."""

    signed_up_at: Optional[int] = None
    """The time the Visitor signed up for your product."""

    social_profiles: Optional[SocialProfiles] = None

    tags: Optional[Tags] = None

    type: Optional[str] = None
    """Value is 'visitor'"""

    unsubscribed_from_emails: Optional[bool] = None
    """Whether the Visitor is unsubscribed from emails."""

    updated_at: Optional[int] = None
    """The last time the Visitor was updated."""

    user_id: Optional[str] = None
    """Automatically generated identifier for the Visitor."""

    utm_campaign: Optional[str] = None
    """The utm_campaign of the visitor."""

    utm_content: Optional[str] = None
    """The utm_content of the visitor."""

    utm_medium: Optional[str] = None
    """The utm_medium of the visitor."""

    utm_source: Optional[str] = None
    """The utm_source of the visitor."""

    utm_term: Optional[str] = None
    """The utm_term of the visitor."""
