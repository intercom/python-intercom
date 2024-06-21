# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.cursor_pages import CursorPages

__all__ = ["ActivityLogList", "ActivityLog", "ActivityLogMetadata", "ActivityLogPerformedBy"]


class ActivityLogMetadata(BaseModel):
    auto_changed: Optional[str] = None
    """Indicates if the status was changed automatically or manually."""

    away_mode: Optional[bool] = None
    """The away mode status which is set to true when away and false when returned."""

    away_status_reason: Optional[str] = None
    """The reason the Admin is away."""

    external_id: Optional[str] = None
    """The unique identifier for the contact which is provided by the Client."""

    reassign_conversations: Optional[bool] = None
    """Indicates if conversations should be reassigned while an Admin is away."""

    sign_in_method: Optional[str] = None
    """The way the admin signed in."""

    source: Optional[str] = None
    """The action that initiated the status change."""

    update_by: Optional[int] = None
    """The ID of the Admin who initiated the activity."""

    update_by_name: Optional[str] = None
    """The name of the Admin who initiated the activity."""


class ActivityLogPerformedBy(BaseModel):
    id: Optional[str] = None
    """The id representing the admin."""

    email: Optional[str] = None
    """The email of the admin."""

    ip: Optional[str] = None
    """The IP address of the admin."""

    type: Optional[str] = None
    """String representing the object's type. Always has the value `admin`."""


class ActivityLog(BaseModel):
    id: Optional[str] = None
    """The id representing the activity."""

    activity_description: Optional[str] = None
    """A sentence or two describing the activity."""

    activity_type: Optional[
        Literal[
            "admin_assignment_limit_change",
            "admin_away_mode_change",
            "admin_deletion",
            "admin_deprovisioned",
            "admin_impersonation_end",
            "admin_impersonation_start",
            "admin_invite_change",
            "admin_invite_creation",
            "admin_invite_deletion",
            "admin_login_failure",
            "admin_login_success",
            "admin_logout",
            "admin_password_reset_request",
            "admin_password_reset_success",
            "admin_permission_change",
            "admin_provisioned",
            "admin_two_factor_auth_change",
            "admin_unauthorized_sign_in_method",
            "app_admin_join",
            "app_authentication_method_change",
            "app_data_deletion",
            "app_data_export",
            "app_google_sso_domain_change",
            "app_identity_verification_change",
            "app_name_change",
            "app_outbound_address_change",
            "app_package_installation",
            "app_package_token_regeneration",
            "app_package_uninstallation",
            "app_team_creation",
            "app_team_deletion",
            "app_team_membership_modification",
            "app_timezone_change",
            "app_webhook_creation",
            "app_webhook_deletion",
            "articles_in_messenger_enabled_change",
            "bulk_delete",
            "bulk_export",
            "campaign_deletion",
            "campaign_state_change",
            "conversation_part_deletion",
            "conversation_topic_change",
            "conversation_topic_creation",
            "conversation_topic_deletion",
            "help_center_settings_change",
            "inbound_conversations_change",
            "inbox_access_change",
            "message_deletion",
            "message_state_change",
            "messenger_look_and_feel_change",
            "messenger_search_required_change",
            "messenger_spaces_change",
            "office_hours_change",
            "role_change",
            "role_creation",
            "role_deletion",
            "ruleset_activation_title_preview",
            "ruleset_creation",
            "ruleset_deletion",
            "search_browse_enabled_change",
            "search_browse_required_change",
            "seat_change",
            "seat_revoke",
            "security_settings_change",
            "temporary_expectation_change",
            "upfront_email_collection_change",
            "welcome_message_change",
        ]
    ] = None

    created_at: Optional[int] = None
    """The time the activity was created."""

    metadata: Optional[ActivityLogMetadata] = None
    """Additional data provided about Admin activity."""

    performed_by: Optional[ActivityLogPerformedBy] = None
    """Details about the Admin involved in the activity."""


class ActivityLogList(BaseModel):
    activity_logs: Optional[List[Optional[ActivityLog]]] = None
    """An array of activity logs"""

    pages: Optional[CursorPages] = None
    """
    Cursor-based pagination is a technique used in the Intercom API to navigate
    through large amounts of data. A "cursor" or pointer is used to keep track of
    the current position in the result set, allowing the API to return the data in
    small chunks or "pages" as needed.
    """

    type: Optional[str] = None
    """String representing the object's type.

    Always has the value `activity_log.list`.
    """
