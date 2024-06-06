# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypedDict

__all__ = [
    "CustomerCreateParams",
    "Customer",
    "CustomerIntercomUserID",
    "CustomerIntercomUserIDCustomer",
    "CustomerIntercomUserIDCustomerIntercomUserID",
    "CustomerIntercomUserIDCustomerUserID",
    "CustomerIntercomUserIDCustomerEmail",
    "CustomerUserID",
    "CustomerUserIDCustomer",
    "CustomerUserIDCustomerIntercomUserID",
    "CustomerUserIDCustomerUserID",
    "CustomerUserIDCustomerEmail",
    "CustomerEmail",
    "CustomerEmailCustomer",
    "CustomerEmailCustomerIntercomUserID",
    "CustomerEmailCustomerUserID",
    "CustomerEmailCustomerEmail",
]


class CustomerCreateParams(TypedDict, total=False):
    admin_id: str
    """The `id` of the admin who is adding the new participant."""

    customer: Customer


class CustomerIntercomUserIDCustomerIntercomUserID(TypedDict, total=False):
    intercom_user_id: Required[str]
    """The identifier for the contact as given by Intercom."""


class CustomerIntercomUserIDCustomerUserID(TypedDict, total=False):
    user_id: Required[str]
    """
    The external_id you have defined for the contact who is being added as a
    participant.
    """


class CustomerIntercomUserIDCustomerEmail(TypedDict, total=False):
    email: Required[str]
    """The email you have defined for the contact who is being added as a participant."""


CustomerIntercomUserIDCustomer = Union[
    CustomerIntercomUserIDCustomerIntercomUserID,
    CustomerIntercomUserIDCustomerUserID,
    CustomerIntercomUserIDCustomerEmail,
]


class CustomerIntercomUserID(TypedDict, total=False):
    intercom_user_id: Required[str]
    """The identifier for the contact as given by Intercom."""

    customer: Optional[CustomerIntercomUserIDCustomer]


class CustomerUserIDCustomerIntercomUserID(TypedDict, total=False):
    intercom_user_id: Required[str]
    """The identifier for the contact as given by Intercom."""


class CustomerUserIDCustomerUserID(TypedDict, total=False):
    user_id: Required[str]
    """
    The external_id you have defined for the contact who is being added as a
    participant.
    """


class CustomerUserIDCustomerEmail(TypedDict, total=False):
    email: Required[str]
    """The email you have defined for the contact who is being added as a participant."""


CustomerUserIDCustomer = Union[
    CustomerUserIDCustomerIntercomUserID, CustomerUserIDCustomerUserID, CustomerUserIDCustomerEmail
]


class CustomerUserID(TypedDict, total=False):
    user_id: Required[str]
    """
    The external_id you have defined for the contact who is being added as a
    participant.
    """

    customer: Optional[CustomerUserIDCustomer]


class CustomerEmailCustomerIntercomUserID(TypedDict, total=False):
    intercom_user_id: Required[str]
    """The identifier for the contact as given by Intercom."""


class CustomerEmailCustomerUserID(TypedDict, total=False):
    user_id: Required[str]
    """
    The external_id you have defined for the contact who is being added as a
    participant.
    """


class CustomerEmailCustomerEmail(TypedDict, total=False):
    email: Required[str]
    """The email you have defined for the contact who is being added as a participant."""


CustomerEmailCustomer = Union[
    CustomerEmailCustomerIntercomUserID, CustomerEmailCustomerUserID, CustomerEmailCustomerEmail
]


class CustomerEmail(TypedDict, total=False):
    email: Required[str]
    """The email you have defined for the contact who is being added as a participant."""

    customer: Optional[CustomerEmailCustomer]


Customer = Union[CustomerIntercomUserID, CustomerUserID, CustomerEmail]
