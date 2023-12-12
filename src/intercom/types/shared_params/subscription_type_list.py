# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from ..contacts import SubscriptionType
from .subscription_type import SubscriptionType

__all__ = ["SubscriptionTypeList"]


class SubscriptionTypeList(TypedDict, total=False):
    data: List[SubscriptionType]
    """A list of subscription type objects associated with the workspace ."""

    type: Literal["list"]
    """The type of the object"""
