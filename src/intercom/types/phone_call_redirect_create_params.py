# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

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

    intercom_version: Annotated[
        Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ],
        PropertyInfo(alias="Intercom-Version"),
    ]
    """
    Intercom API version.By default, it's equal to the version set in the app
    package.
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
