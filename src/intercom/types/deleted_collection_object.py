# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class DeletedCollectionObject(UncheckedBaseModel):
    """
    Response returned when an object is deleted
    """

    id: str = pydantic.Field()
    """
    The unique identifier for the collection which you provided in the URL.
    """

    object: typing.Literal["collection"] = pydantic.Field(default="collection")
    """
    The type of object which was deleted. - `collection`
    """

    deleted: bool = pydantic.Field()
    """
    Whether the collection was deleted successfully or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
