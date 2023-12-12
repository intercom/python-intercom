# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel
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


class ContactsContact(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the contact which is given by Intercom."""

    external_id: Optional[str] = None
    """The unique identifier for the contact which is provided by the Client."""

    type: Optional[Literal["contact"]] = None
    """always contact"""


class Contacts(BaseModel):
    contacts: Optional[List[ContactsContact]] = None
    """The list of contacts affected by this ticket."""

    type: Optional[Literal["contact.list"]] = None
    """always contact.list"""


class LinkedObjectsData(BaseModel):
    id: Optional[str] = None
    """The ID of the linked object"""

    category: Optional[Literal["Customer", "Back-office", "Tracker"]] = None
    """Category of the Linked Ticket Object."""

    type: Optional[Literal["ticket", "conversation"]] = None
    """ticket or conversation"""


class LinkedObjects(BaseModel):
    data: Optional[List[LinkedObjectsData]] = None
    """An array containing the linked conversations and linked tickets."""

    has_more: Optional[bool] = None
    """Whether or not there are more linked objects than returned."""

    total_count: Optional[int] = None
    """The total number of linked objects."""

    type: Optional[Literal["list"]] = None
    """Always list."""


class TicketAttributesFileAttribute(BaseModel):
    content_type: Optional[str] = None
    """The type of file"""

    filesize: Optional[int] = None
    """The size of the file in bytes"""

    height: Optional[int] = None
    """The height of the file in pixels, if applicable"""

    name: Optional[str] = None
    """The name of the file"""

    type: Optional[str] = None

    url: Optional[str] = None
    """The url of the file. This is a temporary URL and will expire after 30 minutes."""

    width: Optional[int] = None
    """The width of the file in pixels, if applicable"""


TicketAttributes = Union[Optional[str], float, bool, List[object], TicketAttributesFileAttribute]


class TicketPartsTicketPartAssignedTo(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class TicketPartsTicketPartAttachment(BaseModel):
    content_type: Optional[str] = None
    """The content type of the attachment"""

    filesize: Optional[int] = None
    """The size of the attachment"""

    height: Optional[int] = None
    """The height of the attachment"""

    name: Optional[str] = None
    """The name of the attachment"""

    type: Optional[str] = None
    """The type of attachment"""

    url: Optional[str] = None
    """The URL of the attachment"""

    width: Optional[int] = None
    """The width of the attachment"""


class TicketPartsTicketPartAuthor(BaseModel):
    id: Optional[str] = None
    """The id of the author"""

    email: Optional[str] = None
    """The email of the author"""

    name: Optional[str] = None
    """The name of the author"""

    type: Optional[Literal["admin", "bot", "team", "user"]] = None
    """The type of the author"""


class TicketPartsTicketPart(BaseModel):
    id: Optional[str] = None
    """The id representing the ticket part."""

    assigned_to: Optional[TicketPartsTicketPartAssignedTo] = None
    """
    The id of the admin that was assigned the ticket by this ticket_part (null if
    there has been no change in assignment.)
    """

    attachments: Optional[List[TicketPartsTicketPartAttachment]] = None
    """A list of attachments for the part."""

    author: Optional[TicketPartsTicketPartAuthor] = None
    """The author that wrote or triggered the part. Can be a bot, admin, team or user."""

    body: Optional[str] = None
    """The message body, which may contain HTML."""

    created_at: Optional[int] = None
    """The time the ticket part was created."""

    external_id: Optional[str] = None
    """The external id of the ticket part"""

    part_type: Optional[str] = None
    """The type of ticket part."""

    previous_ticket_state: Optional[Literal["submitted", "in_progress", "waiting_on_customer", "resolved"]] = None
    """The previous state of the ticket."""

    redacted: Optional[bool] = None
    """Whether or not the ticket part has been redacted."""

    ticket_state: Optional[Literal["submitted", "in_progress", "waiting_on_customer", "resolved"]] = None
    """The state of the ticket."""

    type: Optional[str] = None
    """Always ticket_part"""

    updated_at: Optional[int] = None
    """The last time the ticket part was updated."""


class TicketParts(BaseModel):
    ticket_parts: Optional[List[TicketPartsTicketPart]] = None
    """A list of Ticket Part objects for each ticket. There is a limit of 500 parts."""

    total_count: Optional[int] = None

    type: Optional[Literal["ticket_part.list"]] = None


class Ticket(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the ticket which is given by Intercom."""

    admin_assignee_id: Optional[str] = None
    """The id representing the admin assigned to the ticket."""

    category: Optional[Literal["Customer", "Back-office", "Tracker"]] = None
    """Category of the Ticket."""

    contacts: Optional[Contacts] = None
    """The list of contacts affected by a ticket."""

    created_at: Optional[int] = None
    """The time the ticket was created as a UTC Unix timestamp."""

    is_shared: Optional[bool] = None
    """Whether or not the ticket is shared with the customer."""

    linked_objects: Optional[LinkedObjects] = None
    """An object containing metadata about linked conversations and linked tickets.

    Up to 1000 can be returned.
    """

    open: Optional[bool] = None
    """Whether or not the ticket is open. If false, the ticket is closed."""

    snoozed_until: Optional[int] = None
    """The time the ticket will be snoozed until as a UTC Unix timestamp.

    If null, the ticket is not currently snoozed.
    """

    team_assignee_id: Optional[str] = None
    """The id representing the team assigned to the ticket."""

    ticket_attributes: Optional[Dict[str, TicketAttributes]] = None
    """
    An object containing the different attributes associated to the ticket as
    key-value pairs. For the default title and description attributes, the keys are
    `_default_title_` and `_default_description_`.
    """

    ticket_id: Optional[str] = None
    """The ID of the Ticket used in the Intercom Inbox and Messenger.

    Do not use ticket_id for API queries.
    """

    ticket_parts: Optional[TicketParts] = None
    """A list of Ticket Part objects for each note and event in the ticket.

    There is a limit of 500 parts.
    """

    ticket_state: Optional[Literal["submitted", "in_progress", "waiting_on_customer", "resolved", "closed"]] = None
    """The state the ticket is currenly in"""

    ticket_type: Optional[TicketType] = None
    """A ticket type, used to define the data fields to be captured in a ticket."""

    type: Optional[Literal["ticket"]] = None
    """Always ticket"""

    updated_at: Optional[int] = None
    """The last time the ticket was updated as a UTC Unix timestamp."""
