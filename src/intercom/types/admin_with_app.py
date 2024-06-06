# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AdminWithApp", "App", "Avatar"]


class App(BaseModel):
    created_at: Optional[int] = None
    """When the app was created."""

    id_code: Optional[str] = None
    """The id of the app."""

    identity_verification: Optional[bool] = None
    """Whether or not the app uses identity verification."""

    name: Optional[str] = None
    """The name of the app."""

    region: Optional[str] = None
    """The Intercom region the app is located in."""

    timezone: Optional[str] = None
    """The timezone of the region where the app is located."""

    type: Optional[str] = None


class Avatar(BaseModel):
    image_url: Optional[str] = None
    """This object represents the avatar associated with the admin."""

    type: Optional[str] = None
    """This is a string that identifies the type of the object.

    It will always have the value `avatar`.
    """


class AdminWithApp(BaseModel):
    id: Optional[str] = None
    """The id representing the admin."""

    app: Optional[App] = None
    """App that the admin belongs to."""

    avatar: Optional[Avatar] = None
    """This object represents the avatar associated with the admin."""

    away_mode_enabled: Optional[bool] = None
    """Identifies if this admin is currently set in away mode."""

    away_mode_reassign: Optional[bool] = None
    """
    Identifies if this admin is set to automatically reassign new conversations to
    the apps default inbox.
    """

    email: Optional[str] = None
    """The email of the admin."""

    email_verified: Optional[bool] = None
    """Identifies if this admin's email is verified."""

    has_inbox_seat: Optional[bool] = None
    """
    Identifies if this admin has a paid inbox seat to restrict/allow features that
    require them.
    """

    job_title: Optional[str] = None
    """The job title of the admin."""

    name: Optional[str] = None
    """The name of the admin."""

    team_ids: Optional[List[int]] = None
    """This is a list of ids of the teams that this admin is part of."""

    type: Optional[str] = None
    """String representing the object's type. Always has the value `admin`."""
