# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel
from ...types.team_priority_level import TeamPriorityLevel
from .admin_avatar import AdminAvatar


class Admin(UncheckedBaseModel):
    """
    Admins are teammate accounts that have access to a workspace.
    """

    type: typing.Optional[typing.Literal["admin"]] = pydantic.Field(default=None)
    """
    String representing the object's type. Always has the value `admin`.
    """

    id: str = pydantic.Field()
    """
    The id representing the admin.
    """

    name: str = pydantic.Field()
    """
    The name of the admin.
    """

    email: str = pydantic.Field()
    """
    The email of the admin.
    """

    job_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The job title of the admin.
    """

    away_mode_enabled: bool = pydantic.Field()
    """
    Identifies if this admin is currently set in away mode.
    """

    away_mode_reassign: bool = pydantic.Field()
    """
    Identifies if this admin is set to automatically reassign new conversations to the apps default inbox.
    """

    has_inbox_seat: bool = pydantic.Field()
    """
    Identifies if this admin has a paid inbox seat to restrict/allow features that require them.
    """

    team_ids: typing.List[int] = pydantic.Field()
    """
    This object represents the avatar associated with the admin.
    """

    avatar: typing.Optional[AdminAvatar] = pydantic.Field(default=None)
    """
    The avatar object associated with the admin
    """

    team_priority_level: typing.Optional[TeamPriorityLevel] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
