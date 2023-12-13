# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypedDict

from .ticket_type import TicketType
from ..ticket_type import TicketType

__all__ = [
    "Ticket",
    "Contacts",
    "ContactsContact",
    "LinkedObjects",
    "LinkedObjectsData",
    "TicketAttributes",
    "TicketAttributesFileAttribute",
    "TicketParts",
    "TicketPartsTicketPart",
    "TicketPartsTicketPartAssignedTo",
    "TicketPartsTicketPartAttachment",
    "TicketPartsTicketPartAuthor",
]


class ContactsContact(TypedDict, total=False):
    id: str
    """The unique identifier for the contact which is given by Intercom."""

    external_id: Optional[str]
    """The unique identifier for the contact which is provided by the Client."""

    type: Literal["contact"]
    """always contact"""


class Contacts(TypedDict, total=False):
    contacts: List[ContactsContact]
    """The list of contacts affected by this ticket."""

    type: Literal["contact.list"]
    """always contact.list"""


class LinkedObjectsData(TypedDict, total=False):
    id: str
    """The ID of the linked object"""

    category: Optional[Literal["Customer", "Back-office", "Tracker"]]
    """Category of the Linked Ticket Object."""

    type: Literal["ticket", "conversation"]
    """ticket or conversation"""


class LinkedObjects(TypedDict, total=False):
    data: List[LinkedObjectsData]
    """An array containing the linked conversations and linked tickets."""

    has_more: bool
    """Whether or not there are more linked objects than returned."""

    total_count: int
    """The total number of linked objects."""

    type: Literal["list"]
    """Always list."""


class TicketAttributesFileAttribute(TypedDict, total=False):
    content_type: str
    """The type of file"""

    filesize: int
    """The size of the file in bytes"""

    height: int
    """The height of the file in pixels, if applicable"""

    name: str
    """The name of the file"""

    type: str

    url: str
    """The url of the file. This is a temporary URL and will expire after 30 minutes."""

    width: int
    """The width of the file in pixels, if applicable"""


TicketAttributes = Union[Optional[str], float, bool, List[object], TicketAttributesFileAttribute]


class TicketPartsTicketPartAssignedTo(TypedDict, total=False):
    id: Optional[str]

    type: str


class TicketPartsTicketPartAttachment(TypedDict, total=False):
    content_type: str
    """The content type of the attachment"""

    filesize: int
    """The size of the attachment"""

    height: int
    """The height of the attachment"""

    name: str
    """The name of the attachment"""

    type: str
    """The type of attachment"""

    url: str
    """The URL of the attachment"""

    width: int
    """The width of the attachment"""


class TicketPartsTicketPartAuthor(TypedDict, total=False):
    id: str
    """The id of the author"""

    email: str
    """The email of the author"""

    name: Optional[str]
    """The name of the author"""

    type: Literal["admin", "bot", "team", "user"]
    """The type of the author"""


class TicketPartsTicketPart(TypedDict, total=False):
    id: str
    """The id representing the ticket part."""

    assigned_to: Optional[TicketPartsTicketPartAssignedTo]
    """
    The id of the admin that was assigned the ticket by this ticket_part (null if
    there has been no change in assignment.)
    """

    attachments: List[TicketPartsTicketPartAttachment]
    """A list of attachments for the part."""

    author: TicketPartsTicketPartAuthor
    """The author that wrote or triggered the part. Can be a bot, admin, team or user."""

    body: Optional[str]
    """The message body, which may contain HTML."""

    created_at: int
    """The time the ticket part was created."""

    external_id: Optional[str]
    """The external id of the ticket part"""

    part_type: str
    """The type of ticket part."""

    previous_ticket_state: Literal["submitted", "in_progress", "waiting_on_customer", "resolved"]
    """The previous state of the ticket."""

    redacted: bool
    """Whether or not the ticket part has been redacted."""

    ticket_state: Literal["submitted", "in_progress", "waiting_on_customer", "resolved"]
    """The state of the ticket."""

    type: str
    """Always ticket_part"""

    updated_at: int
    """The last time the ticket part was updated."""


class TicketParts(TypedDict, total=False):
    ticket_parts: List[TicketPartsTicketPart]
    """A list of Ticket Part objects for each ticket. There is a limit of 500 parts."""

    total_count: int

    type: Literal["ticket_part.list"]


class Ticket(TypedDict, total=False):
    id: str
    """The unique identifier for the ticket which is given by Intercom."""

    admin_assignee_id: str
    """The id representing the admin assigned to the ticket."""

    category: Literal["Customer", "Back-office", "Tracker"]
    """Category of the Ticket."""

    contacts: Contacts
    """The list of contacts affected by a ticket."""

    created_at: int
    """The time the ticket was created as a UTC Unix timestamp."""

    is_shared: bool
    """Whether or not the ticket is shared with the customer."""

    linked_objects: LinkedObjects
    """An object containing metadata about linked conversations and linked tickets.

    Up to 1000 can be returned.
    """

    open: bool
    """Whether or not the ticket is open. If false, the ticket is closed."""

    snoozed_until: int
    """The time the ticket will be snoozed until as a UTC Unix timestamp.

    If null, the ticket is not currently snoozed.
    """

    team_assignee_id: str
    """The id representing the team assigned to the ticket."""

    ticket_attributes: Dict[str, TicketAttributes]
    """
    An object containing the different attributes associated to the ticket as
    key-value pairs. For the default title and description attributes, the keys are
    `_default_title_` and `_default_description_`.
    """

    ticket_id: str
    """The ID of the Ticket used in the Intercom Inbox and Messenger.

    Do not use ticket_id for API queries.
    """

    ticket_parts: TicketParts
    """A list of Ticket Part objects for each note and event in the ticket.

    There is a limit of 500 parts.
    """

    ticket_state: Literal["submitted", "in_progress", "waiting_on_customer", "on_hold", "resolved"]
    """The state the ticket is currenly in"""

    ticket_type: Optional[TicketType]
    """A ticket type, used to define the data fields to be captured in a ticket."""

    type: Literal["ticket"]
    """Always ticket"""

    updated_at: int
    """The last time the ticket was updated as a UTC Unix timestamp."""
