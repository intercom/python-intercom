# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ReplyCreateParams",
    "ContactReplyConversationRequest",
    "AdminReplyConversationRequest",
    "AdminReplyConversationRequestReplyOption",
]


class ContactReplyConversationRequest(TypedDict, total=False):
    body: Required[str]
    """The text body of the comment."""

    message_type: Required[Literal["comment"]]

    type: Required[Literal["user"]]

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 5 URLs.
    """

    created_at: int
    """The time the reply was created. If not provided, the current time will be used."""

    email: str
    """The email you have defined for the user."""

    intercom_user_id: str
    """The identifier for the contact as given by Intercom."""

    user_id: str
    """The external_id you have defined for the contact."""


class AdminReplyConversationRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is authoring the comment."""

    message_type: Required[Literal["comment", "note", "quick_reply"]]

    type: Required[Literal["admin"]]

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 5 URLs.
    """

    body: str
    """
    The text body of the reply.\nNotes accept some HTML formatting.\nMust be present
    for comment and note message types.
    """

    created_at: int
    """The time the reply was created. If not provided, the current time will be used."""

    reply_options: List[AdminReplyConversationRequestReplyOption]
    """
    The quick reply options to display.\nMust be present for quick_reply message
    types.
    """


class AdminReplyConversationRequestReplyOption(TypedDict, total=False):
    text: Required[str]
    """The text to display in this quick reply option."""

    uuid: Required[str]
    """A unique identifier for this quick reply option.

    This value will be available within the metadata of the comment conversation
    part that is created when a user clicks on this reply option.
    """


ReplyCreateParams = Union[ContactReplyConversationRequest, AdminReplyConversationRequest]
