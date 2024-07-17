# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TicketCreateParams", "Contact", "ContactID", "ContactExternalID", "ContactEmail"]


class TicketCreateParams(TypedDict, total=False):
    contacts: Required[Iterable[Contact]]
    """The list of contacts (users or leads) affected by this ticket.

    Currently only one is allowed
    """

    ticket_type_id: Required[str]
    """The ID of the type of ticket you want to create"""

    company_id: str
    """The ID of the company that the ticket is associated with.

    The ID that you set upon company creation.
    """

    created_at: int
    """The time the ticket was created.

    If not provided, the current time will be used.
    """

    ticket_attributes: Dict[str, Union[Optional[str], float, bool, Iterable[object]]]
    """The attributes set on the ticket.

    When setting the default title and description attributes, the attribute keys
    that should be used are `_default_title_` and `_default_description_`. When
    setting ticket type attributes of the list attribute type, the key should be the
    attribute name and the value of the attribute should be the list item id,
    obtainable by [listing the ticket type](ref:get_ticket-types). For example, if
    the ticket type has an attribute called `priority` of type `list`, the key
    should be `priority` and the value of the attribute should be the guid of the
    list item (e.g. `de1825a0-0164-4070-8ca6-13e22462fa7e`).
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


class ContactID(TypedDict, total=False):
    id: Required[str]
    """The identifier for the contact as given by Intercom."""


class ContactExternalID(TypedDict, total=False):
    external_id: Required[str]
    """
    The external_id you have defined for the contact who is being added as a
    participant.
    """


class ContactEmail(TypedDict, total=False):
    email: Required[str]
    """The email you have defined for the contact who is being added as a participant.

    If a contact with this email does not exist, one will be created.
    """


Contact = Union[ContactID, ContactExternalID, ContactEmail]
