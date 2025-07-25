# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel


class ActivityLogPerformedBy(UncheckedBaseModel):
    """
    Details about the Admin involved in the activity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    String representing the object's type. Always has the value `admin`.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id representing the admin.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email of the admin.
    """

    ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP address of the admin.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
