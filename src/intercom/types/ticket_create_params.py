# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TicketCreateParams", "Contact", "ContactID", "ContactExternalID", "ContactEmail"]


class TicketCreateParams(TypedDict, total=False):
    contacts: Required[List[Contact]]
    """The list of contacts (users or leads) affected by this ticket.

    Currently only one is allowed
    """

    ticket_type_id: Required[str]
    """The ID of the type of ticket you want to create"""

    ticket_attributes: Dict[str, Union[Optional[str], float, bool, List[object]]]
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
