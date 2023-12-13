# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReplyCreateParams", "ContactReplyConversationRequest", "AdminReplyConversationRequest"]


class ContactReplyConversationRequest(TypedDict, total=False):
    body: Required[str]
    """The text body of the comment."""

    message_type: Required[Literal["comment"]]

    type: Required[Literal["user"]]

    attachment_urls: List[str]
    """A list of image URLs that will be added as attachments.

    You can include up to 5 URLs.
    """

    email: str
    """The email you have defined for the user."""

    intercom_user_id: str
    """The identifier for the contact as given by Intercom."""

    user_id: str
    """The external_id you have defined for the contact."""


class AdminReplyConversationRequest(TypedDict, total=False):
    admin_id: Required[str]
    """The id of the admin who is authoring the comment."""

    message_type: Required[Literal["comment", "note"]]

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


ReplyCreateParams = Union[ContactReplyConversationRequest, AdminReplyConversationRequest]
