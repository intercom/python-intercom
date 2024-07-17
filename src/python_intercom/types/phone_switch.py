# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneSwitch"]


class PhoneSwitch(BaseModel):
    phone: Optional[str] = None
    """
    Phone number in E.164 format, that has received the SMS to continue the
    conversation in the Messenger.
    """

    type: Optional[Literal["phone_call_redirect"]] = None
