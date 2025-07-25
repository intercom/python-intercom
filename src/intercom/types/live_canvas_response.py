# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .content_object import ContentObject


class LiveCanvasResponse(UncheckedBaseModel):
    """
    The response object returned when responding to a Live Canvas request. This contains the components you want to show.
    """

    content: ContentObject = pydantic.Field()
    """
    The content object that defines the components to be shown.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
