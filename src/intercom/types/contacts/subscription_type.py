# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubscriptionType", "DefaultTranslation", "Translation"]


class DefaultTranslation(BaseModel):
    description: Optional[str] = None
    """The localised description of the subscription type."""

    locale: Optional[str] = None
    """The two character identifier for the language of the translation object."""

    name: Optional[str] = None
    """The localised name of the subscription type."""


class Translation(BaseModel):
    description: Optional[str] = None
    """The localised description of the subscription type."""

    locale: Optional[str] = None
    """The two character identifier for the language of the translation object."""

    name: Optional[str] = None
    """The localised name of the subscription type."""


class SubscriptionType(BaseModel):
    id: Optional[str] = None
    """The unique identifier representing the subscription type."""

    consent_type: Optional[Literal["opt_out", "opt_in"]] = None
    """Describes the type of consent."""

    content_types: Optional[List[Literal["email", "sms_message"]]] = None
    """
    The message types that this subscription supports - can contain `email` or
    `sms_message`.
    """

    default_translation: Optional[DefaultTranslation] = None
    """A translation object contains the localised details of a subscription type."""

    state: Optional[Literal["live", "draft", "archived"]] = None
    """The state of the subscription type."""

    translations: Optional[List[Translation]] = None
    """
    An array of translations objects with the localised version of the subscription
    type in each available locale within your translation settings.
    """

    type: Optional[str] = None
    """The type of the object - subscription"""
