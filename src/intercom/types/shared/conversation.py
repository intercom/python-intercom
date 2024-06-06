# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .tag import Tag
from ..._models import BaseModel

__all__ = [
    "Conversation",
    "AIAgent",
    "AIAgentContentSources",
    "AIAgentContentSourcesContentSource",
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


class AIAgentContentSourcesContentSource(BaseModel):
    content_type: Optional[
        Literal["file", "article", "external_content", "content_snippet", "workflow_connector_action"]
    ] = None
    """The type of the content source."""

    locale: Optional[str] = None
    """The ISO 639 language code of the content source."""

    title: Optional[str] = None
    """The title of the content source."""

    url: Optional[str] = None
    """The internal URL linking to the content source for teammates."""


class AIAgentContentSources(BaseModel):
    content_sources: Optional[List[AIAgentContentSourcesContentSource]] = None
    """The content sources used by AI Agent in the conversation."""

    total_count: Optional[int] = None
    """The total number of content sources used by AI Agent in the conversation."""

    type: Optional[Literal["content_source.list"]] = None


class AIAgent(BaseModel):
    content_sources: Optional[AIAgentContentSources] = None

    last_answer_type: Optional[Literal["ai_answer", "custom_answer"]] = None
    """The type of the last answer delviered by AI Agent.

    If no answer was delivered then this will return null
    """

    rating: Optional[int] = None
    """The customer satisfaction rating given to AI Agent, from 1-5."""

    rating_remark: Optional[str] = None
    """The customer satisfaction rating remark given to AI Agent."""

    resolution_state: Optional[
        Literal["assumed_resolution", "confirmed_resolution", "routed_to_team", "abandoned"]
    ] = None
    """The resolution state of AI Agent.

    If no AI or custom answer has been delivered then this will return `abandoned`.
    """

    source_title: Optional[str] = None
    """The title of the source that triggered AI Agent involvement in the conversation.

    If this is `essentials_plan_setup` then it will return null.
    """

    source_type: Optional[
        Literal["essentials_plan_setup", "profile", "workflow", "workflow_preview", "fin_preview"]
    ] = None
    """The type of the source that triggered AI Agent involvement in the conversation."""


class ContactsContact(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the contact which is given by Intercom."""

    external_id: Optional[str] = None
    """The unique identifier for the contact which is provided by the Client."""

    type: Optional[Literal["contact"]] = None
    """always contact"""


class Contacts(BaseModel):
    contacts: Optional[List[ContactsContact]] = None
    """The list of contacts (users or leads) involved in this conversation.

    This will only contain one customer unless more were added via the group
    conversation feature.
    """

    type: Optional[Literal["contact.list"]] = None


class ConversationPartsConversationPartAssignedTo(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class ConversationPartsConversationPartAttachment(BaseModel):
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


class ConversationPartsConversationPartAuthor(BaseModel):
    id: Optional[str] = None
    """The id of the author"""

    email: Optional[str] = None
    """The email of the author"""

    name: Optional[str] = None
    """The name of the author"""

    type: Optional[str] = None
    """The type of the author"""


class ConversationPartsConversationPart(BaseModel):
    id: Optional[str] = None
    """The id representing the conversation part."""

    assigned_to: Optional[ConversationPartsConversationPartAssignedTo] = None
    """
    The id of the admin that was assigned the conversation by this conversation_part
    (null if there has been no change in assignment.)
    """

    attachments: Optional[List[ConversationPartsConversationPartAttachment]] = None
    """A list of attachments for the part."""

    author: Optional[ConversationPartsConversationPartAuthor] = None
    """The object who initiated the conversation, which can be a Contact, Admin or
    Team.

    Bots and campaigns send messages on behalf of Admins or Teams. For Twitter, this
    will be blank.
    """

    body: Optional[str] = None
    """The message body, which may contain HTML.

    For Twitter, this will show a generic message regarding why the body is
    obscured.
    """

    created_at: Optional[int] = None
    """The time the conversation part was created."""

    external_id: Optional[str] = None
    """The external id of the conversation part"""

    notified_at: Optional[int] = None
    """The time the user was notified with the conversation part."""

    part_type: Optional[str] = None
    """The type of conversation part."""

    redacted: Optional[bool] = None
    """Whether or not the conversation part has been redacted."""

    type: Optional[str] = None
    """Always conversation_part"""

    updated_at: Optional[int] = None
    """The last time the conversation part was updated."""


class ConversationParts(BaseModel):
    conversation_parts: Optional[List[ConversationPartsConversationPart]] = None
    """A list of Conversation Part objects for each part message in the conversation.

    This is only returned when Retrieving a Conversation, and ignored when Listing
    all Conversations. There is a limit of 500 parts.
    """

    total_count: Optional[int] = None

    type: Optional[Literal["conversation_part.list"]] = None


class ConversationRatingContact(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the contact which is given by Intercom."""

    external_id: Optional[str] = None
    """The unique identifier for the contact which is provided by the Client."""

    type: Optional[Literal["contact"]] = None
    """always contact"""


class ConversationRatingTeammate(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class ConversationRating(BaseModel):
    contact: Optional[ConversationRatingContact] = None
    """reference to contact object"""

    created_at: Optional[int] = None
    """The time the rating was requested in the conversation being rated."""

    rating: Optional[int] = None
    """The rating, between 1 and 5, for the conversation."""

    remark: Optional[str] = None
    """An optional field to add a remark to correspond to the number rating"""

    teammate: Optional[ConversationRatingTeammate] = None
    """reference to another object"""


class CustomAttributesCustomObjectInstance(BaseModel):
    id: Optional[str] = None
    """The Intercom defined id representing the custom object instance."""

    custom_attributes: Optional[Dict[str, str]] = None
    """The custom attributes you have set on the custom object instance."""

    external_id: Optional[str] = None
    """The id you have defined for the custom object instance."""

    type: Optional[str] = None
    """
    The identifier of the custom object type that defines the structure of the
    custom object instance.
    """


CustomAttributes = Union[str, Optional[CustomAttributesCustomObjectInstance]]


class FirstContactReply(BaseModel):
    created_at: Optional[int] = None

    type: Optional[str] = None

    url: Optional[str] = None


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


class SlaApplied(BaseModel):
    sla_name: Optional[str] = None
    """The name of the SLA as given by the teammate when it was created."""

    sla_status: Optional[Literal["hit", "missed", "cancelled", "active"]] = None
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

    type: Optional[str] = None
    """object type"""


class SourceAttachment(BaseModel):
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


class SourceAuthor(BaseModel):
    id: Optional[str] = None
    """The id of the author"""

    email: Optional[str] = None
    """The email of the author"""

    name: Optional[str] = None
    """The name of the author"""

    type: Optional[str] = None
    """The type of the author"""


class Source(BaseModel):
    id: Optional[str] = None
    """The id representing the message."""

    attachments: Optional[List[SourceAttachment]] = None
    """A list of attachments for the part."""

    author: Optional[SourceAuthor] = None
    """The object who initiated the conversation, which can be a Contact, Admin or
    Team.

    Bots and campaigns send messages on behalf of Admins or Teams. For Twitter, this
    will be blank.
    """

    body: Optional[str] = None
    """The message body, which may contain HTML.

    For Twitter, this will show a generic message regarding why the body is
    obscured.
    """

    delivered_as: Optional[str] = None
    """The conversation's initiation type.

    Possible values are customer_initiated, campaigns_initiated (legacy campaigns),
    operator_initiated (Custom bot), automated (Series and other outbounds with
    dynamic audience message) and admin_initiated (fixed audience message, ticket
    initiated by an admin, group email).
    """

    redacted: Optional[bool] = None
    """Whether or not the source message has been redacted.

    Only applicable for contact initiated messages.
    """

    subject: Optional[str] = None
    """Optional.

    The message subject. For Twitter, this will show a generic message regarding why
    the subject is obscured.
    """

    type: Optional[str] = None
    """
    This includes conversation, email, facebook, instagram, phone_call,
    phone_switch, push, sms, twitter and whatsapp.
    """

    url: Optional[str] = None
    """The URL where the conversation was started.

    For Twitter, Email, and Bots, this will be blank.
    """


class Statistics(BaseModel):
    count_assignments: Optional[int] = None
    """Number of assignments after first_contact_reply_at."""

    count_conversation_parts: Optional[int] = None
    """Total number of conversation parts."""

    count_reopens: Optional[int] = None
    """Number of reopens after first_contact_reply_at."""

    first_admin_reply_at: Optional[int] = None
    """Time of first admin reply after first_contact_reply_at."""

    first_assignment_at: Optional[int] = None
    """Time of first assignment after first_contact_reply_at."""

    first_close_at: Optional[int] = None
    """Time of first close after first_contact_reply_at."""

    first_contact_reply_at: Optional[int] = None
    """Time of first text conversation part from a contact."""

    last_admin_reply_at: Optional[int] = None
    """Time of the last conversation part from an admin."""

    last_assignment_admin_reply_at: Optional[int] = None
    """Time of first admin reply since most recent assignment."""

    last_assignment_at: Optional[int] = None
    """Time of last assignment after first_contact_reply_at."""

    last_close_at: Optional[int] = None
    """Time of the last conversation close."""

    last_closed_by_id: Optional[str] = None
    """The last admin who closed the conversation.

    Returns a reference to an Admin object.
    """

    last_contact_reply_at: Optional[int] = None
    """Time of the last conversation part from a contact."""

    median_time_to_reply: Optional[int] = None
    """Median based on all admin replies after a contact reply.

    Subtracts out of business hours. In seconds.
    """

    time_to_admin_reply: Optional[int] = None
    """Duration until first admin reply. Subtracts out of business hours. In seconds."""

    time_to_assignment: Optional[int] = None
    """Duration until last assignment before first admin reply. In seconds."""

    time_to_first_close: Optional[int] = None
    """Duration until conversation was closed first time.

    Subtracts out of business hours. In seconds.
    """

    time_to_last_close: Optional[int] = None
    """Duration until conversation was closed last time.

    Subtracts out of business hours. In seconds.
    """

    type: Optional[str] = None


class Tags(BaseModel):
    tags: Optional[List[Tag]] = None
    """A list of tags objects associated with the conversation."""

    type: Optional[Literal["tag.list"]] = None
    """The type of the object"""


class TeammatesTeammate(BaseModel):
    id: Optional[str] = None

    type: Optional[str] = None


class Teammates(BaseModel):
    teammates: Optional[List[TeammatesTeammate]] = None
    """
    The list of teammates who participated in the conversation (wrote at least one
    conversation part).
    """

    type: Optional[str] = None
    """The type of the object - `admin.list`."""


class Conversation(BaseModel):
    id: Optional[str] = None
    """The id representing the conversation."""

    admin_assignee_id: Optional[int] = None
    """The id of the admin assigned to the conversation.

    If it's not assigned to an admin it will return null.
    """

    ai_agent: Optional[AIAgent] = None
    """Data related to AI Agent involvement in the conversation."""

    ai_agent_participated: Optional[bool] = None
    """Indicates whether the AI Agent participated in the conversation."""

    contacts: Optional[Contacts] = None
    """The list of contacts (users or leads) involved in this conversation.

    This will only contain one customer unless more were added via the group
    conversation feature.
    """

    conversation_parts: Optional[ConversationParts] = None
    """A list of Conversation Part objects for each part message in the conversation.

    This is only returned when Retrieving a Conversation, and ignored when Listing
    all Conversations. There is a limit of 500 parts.
    """

    conversation_rating: Optional[ConversationRating] = None
    """
    The Conversation Rating object which contains information on the rating and/or
    remark added by a Contact and the Admin assigned to the conversation.
    """

    created_at: Optional[int] = None
    """The time the conversation was created."""

    custom_attributes: Optional[Dict[str, CustomAttributes]] = None
    """
    An object containing the different custom attributes associated to the
    conversation as key-value pairs. For relationship attributes the value will be a
    list of custom object instance models.
    """

    first_contact_reply: Optional[FirstContactReply] = None
    """An object containing information on the first users message.

    For a contact initiated message this will represent the users original message.
    """

    linked_objects: Optional[LinkedObjects] = None
    """An object containing metadata about linked conversations and linked tickets.

    Up to 1000 can be returned.
    """

    open: Optional[bool] = None
    """Indicates whether a conversation is open (true) or closed (false)."""

    priority: Optional[Literal["priority", "not_priority"]] = None
    """If marked as priority, it will return priority or else not_priority."""

    read: Optional[bool] = None
    """Indicates whether a conversation has been read."""

    sla_applied: Optional[SlaApplied] = None
    """
    The SLA Applied object contains the details for which SLA has been applied to
    this conversation. Important: if there are any canceled sla_events for the
    conversation - meaning an SLA has been manually removed from a conversation, the
    sla_status will always be returned as null.
    """

    snoozed_until: Optional[int] = None
    """
    If set this is the time in the future when this conversation will be marked as
    open. i.e. it will be in a snoozed state until this time. i.e. it will be in a
    snoozed state until this time.
    """

    source: Optional[Source] = None
    """
    The Conversation Part that originated this conversation, which can be Contact,
    Admin, Campaign, Automated or Operator initiated.
    """

    state: Optional[Literal["open", "closed", "snoozed"]] = None
    """Can be set to "open", "closed" or "snoozed"."""

    statistics: Optional[Statistics] = None
    """
    A Statistics object containing all information required for reporting, with
    timestamps and calculated metrics.
    """

    tags: Optional[Tags] = None
    """A list of tags objects associated with a conversation"""

    team_assignee_id: Optional[str] = None
    """The id of the team assigned to the conversation.

    If it's not assigned to a team it will return null.
    """

    teammates: Optional[Teammates] = None
    """
    The list of teammates who participated in the conversation (wrote at least one
    conversation part).
    """

    title: Optional[str] = None
    """The title given to the conversation."""

    type: Optional[str] = None
    """Always conversation."""

    updated_at: Optional[int] = None
    """The last time the conversation was updated."""

    waiting_since: Optional[int] = None
    """The last time a Contact responded to an Admin.

    In other words, the time a customer started waiting for a response. Set to null
    if last reply is from an Admin.
    """
