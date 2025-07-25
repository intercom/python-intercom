# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class ActivityLogMetadata(UncheckedBaseModel):
    """
    Additional data provided about Admin activity.
    """

    sign_in_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    The way the admin signed in.
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the contact which is provided by the Client.
    """

    away_mode: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The away mode status which is set to true when away and false when returned.
    """

    away_status_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason the Admin is away.
    """

    reassign_conversations: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if conversations should be reassigned while an Admin is away.
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The action that initiated the status change.
    """

    auto_changed: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if the status was changed automatically or manually.
    """

    update_by: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the Admin who initiated the activity.
    """

    update_by_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the Admin who initiated the activity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
