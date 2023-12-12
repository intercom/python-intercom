# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypedDict

from .tag import Tag
from ..shared import Tag

__all__ = [
    "Conversation",
    "Contacts",
    "ContactsContact",
    "ConversationParts",
    "ConversationPartsConversationPart",
    "ConversationPartsConversationPartAssignedTo",
    "ConversationPartsConversationPartAttachment",
    "ConversationPartsConversationPartAuthor",
    "ConversationRating",
    "ConversationRatingContact",
    "ConversationRatingTeammate",
    "CustomAttributes",
    "CustomAttributesCustomObjectInstance",
    "FirstContactReply",
    "LinkedObjects",
    "LinkedObjectsData",
    "SlaApplied",
    "Source",
    "SourceAttachment",
    "SourceAuthor",
    "Statistics",
    "Tags",
    "Teammates",
    "TeammatesTeammate",
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
    """The list of contacts (users or leads) involved in this conversation.

    This will only contain one customer unless more were added via the group
    conversation feature.
    """

    type: Literal["contact.list"]


class ConversationPartsConversationPartAssignedTo(TypedDict, total=False):
    id: Optional[str]

    type: str


class ConversationPartsConversationPartAttachment(TypedDict, total=False):
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


class ConversationPartsConversationPartAuthor(TypedDict, total=False):
    id: str
    """The id of the author"""

    email: str
    """The email of the author"""

    name: str
    """The name of the author"""

    type: str
    """The type of the author"""


class ConversationPartsConversationPart(TypedDict, total=False):
    id: str
    """The id representing the conversation part."""

    assigned_to: Optional[ConversationPartsConversationPartAssignedTo]
    """
    The id of the admin that was assigned the conversation by this conversation_part
    (null if there has been no change in assignment.)
    """

    attachments: List[ConversationPartsConversationPartAttachment]
    """A list of attachments for the part."""

    author: ConversationPartsConversationPartAuthor
    """The object who initiated the conversation, which can be a Contact, Admin or
    Team.

    Bots and campaigns send messages on behalf of Admins or Teams. For Twitter, this
    will be blank.
    """

    body: Optional[str]
    """The message body, which may contain HTML.

    For Twitter, this will show a generic message regarding why the body is
    obscured.
    """

    created_at: int
    """The time the conversation part was created."""

    external_id: Optional[str]
    """The external id of the conversation part"""

    notified_at: int
    """The time the user was notified with the conversation part."""

    part_type: str
    """The type of conversation part."""

    redacted: bool
    """Whether or not the conversation part has been redacted."""

    type: str
    """Always conversation_part"""

    updated_at: int
    """The last time the conversation part was updated."""


class ConversationParts(TypedDict, total=False):
    conversation_parts: List[ConversationPartsConversationPart]
    """A list of Conversation Part objects for each part message in the conversation.

    This is only returned when Retrieving a Conversation, and ignored when Listing
    all Conversations. There is a limit of 500 parts.
    """

    total_count: int

    type: Literal["conversation_part.list"]


class ConversationRatingContact(TypedDict, total=False):
    id: str
    """The unique identifier for the contact which is given by Intercom."""

    external_id: Optional[str]
    """The unique identifier for the contact which is provided by the Client."""

    type: Literal["contact"]
    """always contact"""


class ConversationRatingTeammate(TypedDict, total=False):
    id: Optional[str]

    type: str


class ConversationRating(TypedDict, total=False):
    contact: ConversationRatingContact
    """reference to contact object"""

    created_at: int
    """The time the rating was requested in the conversation being rated."""

    rating: int
    """The rating, between 1 and 5, for the conversation."""

    remark: str
    """An optional field to add a remark to correspond to the number rating"""

    teammate: ConversationRatingTeammate
    """reference to another object"""


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


class FirstContactReply(TypedDict, total=False):
    created_at: int

    type: str

    url: Optional[str]


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


class SlaApplied(TypedDict, total=False):
    sla_name: str
    """The name of the SLA as given by the teammate when it was created."""

    sla_status: Literal["hit", "missed", "cancelled", "active"]
    """
    SLA statuses: - `hit`: If there’s at least one hit event in the underlying
    sla_events table, and no “missed” or “canceled” events for the conversation. -
    `missed`: If there are any missed sla_events for the conversation and no
    canceled events. If there’s even a single missed sla event, the status will
    always be missed. A missed status is not applied when the SLA expires, only the
    next time a teammate replies. - `active`: An SLA has been applied to a
    conversation, but has not yet been fulfilled. SLA status is active only if there
    are no “hit, “missed”, or “canceled” events.
    """

    type: str
    """object type"""


class SourceAttachment(TypedDict, total=False):
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


class SourceAuthor(TypedDict, total=False):
    id: str
    """The id of the author"""

    email: str
    """The email of the author"""

    name: str
    """The name of the author"""

    type: str
    """The type of the author"""


class Source(TypedDict, total=False):
    id: str
    """The id representing the message."""

    attachments: List[SourceAttachment]
    """A list of attachments for the part."""

    author: SourceAuthor
    """The object who initiated the conversation, which can be a Contact, Admin or
    Team.

    Bots and campaigns send messages on behalf of Admins or Teams. For Twitter, this
    will be blank.
    """

    body: str
    """The message body, which may contain HTML.

    For Twitter, this will show a generic message regarding why the body is
    obscured.
    """

    delivered_as: str
    """The conversation's initiation type.

    Possible values are customer_initiated, campaigns_initiated (legacy campaigns),
    operator_initiated (Custom bot), automated (Series and other outbounds with
    dynamic audience message) and admin_initiated (fixed audience message, ticket
    initiated by an admin, group email).
    """

    redacted: bool
    """Whether or not the source message has been redacted.

    Only applicable for contact initiated messages.
    """

    subject: str
    """Optional.

    The message subject. For Twitter, this will show a generic message regarding why
    the subject is obscured.
    """

    type: str
    """This includes conversation, push, facebook, twitter and email."""

    url: Optional[str]
    """The URL where the conversation was started.

    For Twitter, Email, and Bots, this will be blank.
    """


class Statistics(TypedDict, total=False):
    count_assignments: int
    """Number of assignments after first_contact_reply_at."""

    count_conversation_parts: int
    """Total number of conversation parts."""

    count_reopens: int
    """Number of reopens after first_contact_reply_at."""

    first_admin_reply_at: int
    """Time of first admin reply after first_contact_reply_at."""

    first_assignment_at: int
    """Time of first assignment after first_contact_reply_at."""

    first_close_at: int
    """Time of first close after first_contact_reply_at."""

    first_contact_reply_at: int
    """Time of first text conversation part from a contact."""

    last_admin_reply_at: int
    """Time of the last conversation part from an admin."""

    last_assignment_admin_reply_at: int
    """Time of first admin reply since most recent assignment."""

    last_assignment_at: int
    """Time of last assignment after first_contact_reply_at."""

    last_close_at: int
    """Time of the last conversation close."""

    last_closed_by_id: str
    """The last admin who closed the conversation.

    Returns a reference to an Admin object.
    """

    last_contact_reply_at: int
    """Time of the last conversation part from a contact."""

    median_time_to_reply: int
    """Median based on all admin replies after a contact reply.

    Subtracts out of business hours. In seconds.
    """

    time_to_admin_reply: int
    """Duration until first admin reply. Subtracts out of business hours. In seconds."""

    time_to_assignment: int
    """Duration until last assignment before first admin reply. In seconds."""

    time_to_first_close: int
    """Duration until conversation was closed first time.

    Subtracts out of business hours. In seconds.
    """

    time_to_last_close: int
    """Duration until conversation was closed last time.

    Subtracts out of business hours. In seconds.
    """

    type: str


class Tags(TypedDict, total=False):
    tags: List[Tag]
    """A list of tags objects associated with the conversation."""

    type: Literal["tag.list"]
    """The type of the object"""


class TeammatesTeammate(TypedDict, total=False):
    id: Optional[str]

    type: str


class Teammates(TypedDict, total=False):
    teammates: List[TeammatesTeammate]
    """
    The list of teammates who participated in the conversation (wrote at least one
    conversation part).
    """

    type: str
    """The type of the object - `admin.list`."""


class Conversation(TypedDict, total=False):
    id: str
    """The id representing the conversation."""

    admin_assignee_id: Optional[int]
    """The id of the admin assigned to the conversation.

    If it's not assigned to an admin it will return null.
    """

    contacts: Contacts
    """The list of contacts (users or leads) involved in this conversation.

    This will only contain one customer unless more were added via the group
    conversation feature.
    """

    conversation_parts: ConversationParts
    """A list of Conversation Part objects for each part message in the conversation.

    This is only returned when Retrieving a Conversation, and ignored when Listing
    all Conversations. There is a limit of 500 parts.
    """

    conversation_rating: Optional[ConversationRating]
    """
    The Conversation Rating object which contains information on the rating and/or
    remark added by a Contact and the Admin assigned to the conversation.
    """

    created_at: int
    """The time the conversation was created."""

    custom_attributes: Dict[str, CustomAttributes]
    """
    An object containing the different custom attributes associated to the
    conversation as key-value pairs. For relationship attributes the value will be a
    list of custom object instance models.
    """

    first_contact_reply: Optional[FirstContactReply]
    """An object containing information on the first users message.

    For a contact initiated message this will represent the users original message.
    """

    linked_objects: LinkedObjects
    """An object containing metadata about linked conversations and linked tickets.

    Up to 1000 can be returned.
    """

    open: bool
    """Indicates whether a conversation is open (true) or closed (false)."""

    priority: Literal["priority", "not_priority"]
    """If marked as priority, it will return priority or else not_priority."""

    read: bool
    """Indicates whether a conversation has been read."""

    sla_applied: Optional[SlaApplied]
    """
    The SLA Applied object contains the details for which SLA has been applied to
    this conversation. Important: if there are any canceled sla_events for the
    conversation - meaning an SLA has been manually removed from a conversation, the
    sla_status will always be returned as null.
    """

    snoozed_until: Optional[int]
    """
    If set this is the time in the future when this conversation will be marked as
    open. i.e. it will be in a snoozed state until this time. i.e. it will be in a
    snoozed state until this time.
    """

    source: Source
    """
    The Conversation Part that originated this conversation, which can be Contact,
    Admin, Campaign, Automated or Operator initiated.
    """

    state: Literal["open", "closed", "snoozed"]
    """Can be set to "open", "closed" or "snoozed"."""

    statistics: Optional[Statistics]
    """
    A Statistics object containing all information required for reporting, with
    timestamps and calculated metrics.
    """

    tags: Tags
    """A list of tags objects associated with a conversation"""

    team_assignee_id: Optional[str]
    """The id of the team assigned to the conversation.

    If it's not assigned to a team it will return null.
    """

    teammates: Optional[Teammates]
    """
    The list of teammates who participated in the conversation (wrote at least one
    conversation part).
    """

    title: Optional[str]
    """The title given to the conversation."""

    type: str
    """Always conversation."""

    updated_at: int
    """The last time the conversation was updated."""

    waiting_since: Optional[int]
    """The last time a Contact responded to an Admin.

    In other words, the time a customer started waiting for a response. Set to null
    if last reply is from an Admin.
    """
