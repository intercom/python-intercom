# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..contacts import SubscriptionType

__all__ = ["SubscriptionTypeList"]


class SubscriptionTypeList(BaseModel):
    data: Optional[List[SubscriptionType]] = None
    """A list of subscription type objects associated with the workspace ."""

    type: Optional[Literal["list"]] = None
    """The type of the object"""
