# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = [
    "CustomerCreateParams",
    "Customer",
    "CustomerUnionMember0",
    "CustomerUnionMember0Customer",
    "CustomerUnionMember0CustomerIntercomUserID",
    "CustomerUnionMember0CustomerUserID",
    "CustomerUnionMember0CustomerEmail",
    "CustomerUnionMember1",
    "CustomerUnionMember1Customer",
    "CustomerUnionMember1CustomerIntercomUserID",
    "CustomerUnionMember1CustomerUserID",
    "CustomerUnionMember1CustomerEmail",
    "CustomerUnionMember2",
    "CustomerUnionMember2Customer",
    "CustomerUnionMember2CustomerIntercomUserID",
    "CustomerUnionMember2CustomerUserID",
    "CustomerUnionMember2CustomerEmail",
]


class CustomerCreateParams(TypedDict, total=False):
    admin_id: str
    """The `id` of the admin who is adding the new participant."""

    customer: Customer


class CustomerUnionMember0CustomerIntercomUserID(TypedDict, total=False):
    intercom_user_id: Required[str]
    """The identifier for the contact as given by Intercom."""


class CustomerUnionMember0CustomerUserID(TypedDict, total=False):
    user_id: Required[str]
    """
    The external_id you have defined for the contact who is being added as a
    participant.
    """


class CustomerUnionMember0CustomerEmail(TypedDict, total=False):
    email: Required[str]
    """The email you have defined for the contact who is being added as a participant."""


CustomerUnionMember0Customer = Union[
    CustomerUnionMember0CustomerIntercomUserID, CustomerUnionMember0CustomerUserID, CustomerUnionMember0CustomerEmail
]


class CustomerUnionMember0(TypedDict, total=False):
    intercom_user_id: Required[str]
    """The identifier for the contact as given by Intercom."""

    customer: CustomerUnionMember0Customer


class CustomerUnionMember1CustomerIntercomUserID(TypedDict, total=False):
    intercom_user_id: Required[str]
    """The identifier for the contact as given by Intercom."""


class CustomerUnionMember1CustomerUserID(TypedDict, total=False):
    user_id: Required[str]
    """
    The external_id you have defined for the contact who is being added as a
    participant.
    """


class CustomerUnionMember1CustomerEmail(TypedDict, total=False):
    email: Required[str]
    """The email you have defined for the contact who is being added as a participant."""


CustomerUnionMember1Customer = Union[
    CustomerUnionMember1CustomerIntercomUserID, CustomerUnionMember1CustomerUserID, CustomerUnionMember1CustomerEmail
]


class CustomerUnionMember1(TypedDict, total=False):
    user_id: Required[str]
    """
    The external_id you have defined for the contact who is being added as a
    participant.
    """

    customer: CustomerUnionMember1Customer


class CustomerUnionMember2CustomerIntercomUserID(TypedDict, total=False):
    intercom_user_id: Required[str]
    """The identifier for the contact as given by Intercom."""


class CustomerUnionMember2CustomerUserID(TypedDict, total=False):
    user_id: Required[str]
    """
    The external_id you have defined for the contact who is being added as a
    participant.
    """


class CustomerUnionMember2CustomerEmail(TypedDict, total=False):
    email: Required[str]
    """The email you have defined for the contact who is being added as a participant."""


CustomerUnionMember2Customer = Union[
    CustomerUnionMember2CustomerIntercomUserID, CustomerUnionMember2CustomerUserID, CustomerUnionMember2CustomerEmail
]


class CustomerUnionMember2(TypedDict, total=False):
    email: Required[str]
    """The email you have defined for the contact who is being added as a participant."""

    customer: CustomerUnionMember2Customer


Customer = Union[CustomerUnionMember0, CustomerUnionMember1, CustomerUnionMember2]
