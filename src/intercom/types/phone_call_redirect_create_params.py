# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PhoneCallRedirectCreateParams", "CustomAttributes", "CustomAttributesCustomObjectInstance"]


class PhoneCallRedirectCreateParams(TypedDict, total=False):
    phone: Required[str]
    """
    Phone number in E.164 format, that will receive the SMS to continue the
    conversation in the Messenger.
    """

    custom_attributes: Dict[str, CustomAttributes]
    """
    An object containing the different custom attributes associated to the
    conversation as key-value pairs. For relationship attributes the value will be a
    list of custom object instance models.
    """


class CustomAttributesCustomObjectInstance(TypedDict, total=False):
    id: str
    """The Intercom defined id representing the custom object instance."""

    custom_attributes: Dict[str, str]
    """The custom attributes you have set on the custom object instance."""

    external_id: str
    """The id you have defined for the custom object instance."""

    type: str
    """
    The identifier of the custom object type that defines the structure of the
    custom object instance.
    """


CustomAttributes = Union[str, Optional[CustomAttributesCustomObjectInstance]]

CustomAttributes = Dict[str, CustomAttributes]
