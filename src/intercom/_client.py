# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from ._streaming import Stream as Stream
from ._streaming import AsyncStream as AsyncStream
from ._exceptions import IntercomError, APIStatusError
from ._base_client import DEFAULT_MAX_RETRIES, SyncAPIClient, AsyncAPIClient

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Intercom",
    "AsyncIntercom",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.intercom.io",
    "environment_1": "https://api.eu.intercom.io",
    "environment_2": "https://api.au.intercom.io",
}


class Intercom(SyncAPIClient):
    me: resources.Me
    admins: resources.Admins
    articles: resources.Articles
    help_center: resources.HelpCenter
    companies: resources.Companies
    contacts: resources.Contacts
    conversations: resources.Conversations
    data_attributes: resources.DataAttributes
    data_events: resources.DataEvents
    data_exports: resources.DataExports
    export: resources.Export
    download: resources.Download
    messages: resources.Messages
    news: resources.News
    notes: resources.Notes
    segments: resources.Segments
    subscription_types: resources.SubscriptionTypes
    phone_call_redirects: resources.PhoneCallRedirects
    tags: resources.Tags
    teams: resources.Teams
    ticket_types: resources.TicketTypes
    tickets: resources.Tickets
    visitors: resources.Visitors
    with_raw_response: IntercomWithRawResponse

    # client options
    bearer_token: str

    _environment: Literal["production", "environment_1", "environment_2"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous intercom client instance.

        This automatically infers the `bearer_token` argument from the `INTERCOM_TEST_1_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("INTERCOM_TEST_1_BEARER_TOKEN")
        if bearer_token is None:
            raise IntercomError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the INTERCOM_TEST_1_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("INTERCOM_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `INTERCOM_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.me = resources.Me(self)
        self.admins = resources.Admins(self)
        self.articles = resources.Articles(self)
        self.help_center = resources.HelpCenter(self)
        self.companies = resources.Companies(self)
        self.contacts = resources.Contacts(self)
        self.conversations = resources.Conversations(self)
        self.data_attributes = resources.DataAttributes(self)
        self.data_events = resources.DataEvents(self)
        self.data_exports = resources.DataExports(self)
        self.export = resources.Export(self)
        self.download = resources.Download(self)
        self.messages = resources.Messages(self)
        self.news = resources.News(self)
        self.notes = resources.Notes(self)
        self.segments = resources.Segments(self)
        self.subscription_types = resources.SubscriptionTypes(self)
        self.phone_call_redirects = resources.PhoneCallRedirects(self)
        self.tags = resources.Tags(self)
        self.teams = resources.Teams(self)
        self.ticket_types = resources.TicketTypes(self)
        self.tickets = resources.Tickets(self)
        self.visitors = resources.Visitors(self)
        self.with_raw_response = IntercomWithRawResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncIntercom(AsyncAPIClient):
    me: resources.AsyncMe
    admins: resources.AsyncAdmins
    articles: resources.AsyncArticles
    help_center: resources.AsyncHelpCenter
    companies: resources.AsyncCompanies
    contacts: resources.AsyncContacts
    conversations: resources.AsyncConversations
    data_attributes: resources.AsyncDataAttributes
    data_events: resources.AsyncDataEvents
    data_exports: resources.AsyncDataExports
    export: resources.AsyncExport
    download: resources.AsyncDownload
    messages: resources.AsyncMessages
    news: resources.AsyncNews
    notes: resources.AsyncNotes
    segments: resources.AsyncSegments
    subscription_types: resources.AsyncSubscriptionTypes
    phone_call_redirects: resources.AsyncPhoneCallRedirects
    tags: resources.AsyncTags
    teams: resources.AsyncTeams
    ticket_types: resources.AsyncTicketTypes
    tickets: resources.AsyncTickets
    visitors: resources.AsyncVisitors
    with_raw_response: AsyncIntercomWithRawResponse

    # client options
    bearer_token: str

    _environment: Literal["production", "environment_1", "environment_2"] | NotGiven

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async intercom client instance.

        This automatically infers the `bearer_token` argument from the `INTERCOM_TEST_1_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("INTERCOM_TEST_1_BEARER_TOKEN")
        if bearer_token is None:
            raise IntercomError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the INTERCOM_TEST_1_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("INTERCOM_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `INTERCOM_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.me = resources.AsyncMe(self)
        self.admins = resources.AsyncAdmins(self)
        self.articles = resources.AsyncArticles(self)
        self.help_center = resources.AsyncHelpCenter(self)
        self.companies = resources.AsyncCompanies(self)
        self.contacts = resources.AsyncContacts(self)
        self.conversations = resources.AsyncConversations(self)
        self.data_attributes = resources.AsyncDataAttributes(self)
        self.data_events = resources.AsyncDataEvents(self)
        self.data_exports = resources.AsyncDataExports(self)
        self.export = resources.AsyncExport(self)
        self.download = resources.AsyncDownload(self)
        self.messages = resources.AsyncMessages(self)
        self.news = resources.AsyncNews(self)
        self.notes = resources.AsyncNotes(self)
        self.segments = resources.AsyncSegments(self)
        self.subscription_types = resources.AsyncSubscriptionTypes(self)
        self.phone_call_redirects = resources.AsyncPhoneCallRedirects(self)
        self.tags = resources.AsyncTags(self)
        self.teams = resources.AsyncTeams(self)
        self.ticket_types = resources.AsyncTicketTypes(self)
        self.tickets = resources.AsyncTickets(self)
        self.visitors = resources.AsyncVisitors(self)
        self.with_raw_response = AsyncIntercomWithRawResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class IntercomWithRawResponse:
    def __init__(self, client: Intercom) -> None:
        self.me = resources.MeWithRawResponse(client.me)
        self.admins = resources.AdminsWithRawResponse(client.admins)
        self.articles = resources.ArticlesWithRawResponse(client.articles)
        self.help_center = resources.HelpCenterWithRawResponse(client.help_center)
        self.companies = resources.CompaniesWithRawResponse(client.companies)
        self.contacts = resources.ContactsWithRawResponse(client.contacts)
        self.conversations = resources.ConversationsWithRawResponse(client.conversations)
        self.data_attributes = resources.DataAttributesWithRawResponse(client.data_attributes)
        self.data_events = resources.DataEventsWithRawResponse(client.data_events)
        self.data_exports = resources.DataExportsWithRawResponse(client.data_exports)
        self.export = resources.ExportWithRawResponse(client.export)
        self.download = resources.DownloadWithRawResponse(client.download)
        self.messages = resources.MessagesWithRawResponse(client.messages)
        self.news = resources.NewsWithRawResponse(client.news)
        self.notes = resources.NotesWithRawResponse(client.notes)
        self.segments = resources.SegmentsWithRawResponse(client.segments)
        self.subscription_types = resources.SubscriptionTypesWithRawResponse(client.subscription_types)
        self.phone_call_redirects = resources.PhoneCallRedirectsWithRawResponse(client.phone_call_redirects)
        self.tags = resources.TagsWithRawResponse(client.tags)
        self.teams = resources.TeamsWithRawResponse(client.teams)
        self.ticket_types = resources.TicketTypesWithRawResponse(client.ticket_types)
        self.tickets = resources.TicketsWithRawResponse(client.tickets)
        self.visitors = resources.VisitorsWithRawResponse(client.visitors)


class AsyncIntercomWithRawResponse:
    def __init__(self, client: AsyncIntercom) -> None:
        self.me = resources.AsyncMeWithRawResponse(client.me)
        self.admins = resources.AsyncAdminsWithRawResponse(client.admins)
        self.articles = resources.AsyncArticlesWithRawResponse(client.articles)
        self.help_center = resources.AsyncHelpCenterWithRawResponse(client.help_center)
        self.companies = resources.AsyncCompaniesWithRawResponse(client.companies)
        self.contacts = resources.AsyncContactsWithRawResponse(client.contacts)
        self.conversations = resources.AsyncConversationsWithRawResponse(client.conversations)
        self.data_attributes = resources.AsyncDataAttributesWithRawResponse(client.data_attributes)
        self.data_events = resources.AsyncDataEventsWithRawResponse(client.data_events)
        self.data_exports = resources.AsyncDataExportsWithRawResponse(client.data_exports)
        self.export = resources.AsyncExportWithRawResponse(client.export)
        self.download = resources.AsyncDownloadWithRawResponse(client.download)
        self.messages = resources.AsyncMessagesWithRawResponse(client.messages)
        self.news = resources.AsyncNewsWithRawResponse(client.news)
        self.notes = resources.AsyncNotesWithRawResponse(client.notes)
        self.segments = resources.AsyncSegmentsWithRawResponse(client.segments)
        self.subscription_types = resources.AsyncSubscriptionTypesWithRawResponse(client.subscription_types)
        self.phone_call_redirects = resources.AsyncPhoneCallRedirectsWithRawResponse(client.phone_call_redirects)
        self.tags = resources.AsyncTagsWithRawResponse(client.tags)
        self.teams = resources.AsyncTeamsWithRawResponse(client.teams)
        self.ticket_types = resources.AsyncTicketTypesWithRawResponse(client.ticket_types)
        self.tickets = resources.AsyncTicketsWithRawResponse(client.tickets)
        self.visitors = resources.AsyncVisitorsWithRawResponse(client.visitors)


Client = Intercom

AsyncClient = AsyncIntercom
