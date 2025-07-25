# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel
from ...types.customer_request import CustomerRequest


class AttachContactToConversationRequestCustomerUserId(UncheckedBaseModel):
    user_id: str = pydantic.Field()
    """
    The external_id you have defined for the contact who is being added as a participant.
    """

    customer: typing.Optional[CustomerRequest] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
