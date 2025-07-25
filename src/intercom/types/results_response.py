# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class ResultsResponse(UncheckedBaseModel):
    """
    The results object should be sent when you want to end configuration of the app and trigger the [Initialize request](https://developers.intercom.com/docs/canvas-kit/#initialize) to be sent. You provide the key-value pairs of data you want access to and we will send these in the Initialize request within a [card_creation_options object](https://developers.intercom.com/docs/references/canvas-kit/requestobjects/card-creation-options/#card-creation-options).
    """

    results: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    Key-value pairs of data you want access to in the Initialize request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
