# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import IntercomError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

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
    me: resources.MeResource
    admins: resources.AdminsResource
    articles: resources.ArticlesResource
    help_center: resources.HelpCenterResource
    companies: resources.CompaniesResource
    contacts: resources.ContactsResource
    conversations: resources.ConversationsResource
    data_attributes: resources.DataAttributesResource
    data_events: resources.DataEventsResource
    data_exports: resources.DataExportsResource
    export: resources.ExportResource
    download: resources.DownloadResource
    messages: resources.MessagesResource
    news: resources.NewsResource
    notes: resources.NotesResource
    segments: resources.SegmentsResource
    subscription_types: resources.SubscriptionTypesResource
    phone_call_redirects: resources.PhoneCallRedirectsResource
    tags: resources.TagsResource
    teams: resources.TeamsResource
    ticket_types: resources.TicketTypesResource
    tickets: resources.TicketsResource
    visitors: resources.VisitorsResource
    with_raw_response: IntercomWithRawResponse
    with_streaming_response: IntercomWithStreamedResponse

    # client options
    access_token: str

    _environment: Literal["production", "environment_1", "environment_2"] | NotGiven

    def __init__(
        self,
        *,
        access_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
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

        This automatically infers the `access_token` argument from the `INTERCOM_ACCESS_TOKEN` environment variable if it is not provided.
        """
        if access_token is None:
            access_token = os.environ.get("INTERCOM_ACCESS_TOKEN")
        if access_token is None:
            raise IntercomError(
                "The access_token client option must be set either by passing access_token to the client or by setting the INTERCOM_ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

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

        self.me = resources.MeResource(self)
        self.admins = resources.AdminsResource(self)
        self.articles = resources.ArticlesResource(self)
        self.help_center = resources.HelpCenterResource(self)
        self.companies = resources.CompaniesResource(self)
        self.contacts = resources.ContactsResource(self)
        self.conversations = resources.ConversationsResource(self)
        self.data_attributes = resources.DataAttributesResource(self)
        self.data_events = resources.DataEventsResource(self)
        self.data_exports = resources.DataExportsResource(self)
        self.export = resources.ExportResource(self)
        self.download = resources.DownloadResource(self)
        self.messages = resources.MessagesResource(self)
        self.news = resources.NewsResource(self)
        self.notes = resources.NotesResource(self)
        self.segments = resources.SegmentsResource(self)
        self.subscription_types = resources.SubscriptionTypesResource(self)
        self.phone_call_redirects = resources.PhoneCallRedirectsResource(self)
        self.tags = resources.TagsResource(self)
        self.teams = resources.TeamsResource(self)
        self.ticket_types = resources.TicketTypesResource(self)
        self.tickets = resources.TicketsResource(self)
        self.visitors = resources.VisitorsResource(self)
        self.with_raw_response = IntercomWithRawResponse(self)
        self.with_streaming_response = IntercomWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        return {"Authorization": f"Bearer {access_token}"}

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
        access_token: str | None = None,
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
            access_token=access_token or self.access_token,
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
    me: resources.AsyncMeResource
    admins: resources.AsyncAdminsResource
    articles: resources.AsyncArticlesResource
    help_center: resources.AsyncHelpCenterResource
    companies: resources.AsyncCompaniesResource
    contacts: resources.AsyncContactsResource
    conversations: resources.AsyncConversationsResource
    data_attributes: resources.AsyncDataAttributesResource
    data_events: resources.AsyncDataEventsResource
    data_exports: resources.AsyncDataExportsResource
    export: resources.AsyncExportResource
    download: resources.AsyncDownloadResource
    messages: resources.AsyncMessagesResource
    news: resources.AsyncNewsResource
    notes: resources.AsyncNotesResource
    segments: resources.AsyncSegmentsResource
    subscription_types: resources.AsyncSubscriptionTypesResource
    phone_call_redirects: resources.AsyncPhoneCallRedirectsResource
    tags: resources.AsyncTagsResource
    teams: resources.AsyncTeamsResource
    ticket_types: resources.AsyncTicketTypesResource
    tickets: resources.AsyncTicketsResource
    visitors: resources.AsyncVisitorsResource
    with_raw_response: AsyncIntercomWithRawResponse
    with_streaming_response: AsyncIntercomWithStreamedResponse

    # client options
    access_token: str

    _environment: Literal["production", "environment_1", "environment_2"] | NotGiven

    def __init__(
        self,
        *,
        access_token: str | None = None,
        environment: Literal["production", "environment_1", "environment_2"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
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

        This automatically infers the `access_token` argument from the `INTERCOM_ACCESS_TOKEN` environment variable if it is not provided.
        """
        if access_token is None:
            access_token = os.environ.get("INTERCOM_ACCESS_TOKEN")
        if access_token is None:
            raise IntercomError(
                "The access_token client option must be set either by passing access_token to the client or by setting the INTERCOM_ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

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

        self.me = resources.AsyncMeResource(self)
        self.admins = resources.AsyncAdminsResource(self)
        self.articles = resources.AsyncArticlesResource(self)
        self.help_center = resources.AsyncHelpCenterResource(self)
        self.companies = resources.AsyncCompaniesResource(self)
        self.contacts = resources.AsyncContactsResource(self)
        self.conversations = resources.AsyncConversationsResource(self)
        self.data_attributes = resources.AsyncDataAttributesResource(self)
        self.data_events = resources.AsyncDataEventsResource(self)
        self.data_exports = resources.AsyncDataExportsResource(self)
        self.export = resources.AsyncExportResource(self)
        self.download = resources.AsyncDownloadResource(self)
        self.messages = resources.AsyncMessagesResource(self)
        self.news = resources.AsyncNewsResource(self)
        self.notes = resources.AsyncNotesResource(self)
        self.segments = resources.AsyncSegmentsResource(self)
        self.subscription_types = resources.AsyncSubscriptionTypesResource(self)
        self.phone_call_redirects = resources.AsyncPhoneCallRedirectsResource(self)
        self.tags = resources.AsyncTagsResource(self)
        self.teams = resources.AsyncTeamsResource(self)
        self.ticket_types = resources.AsyncTicketTypesResource(self)
        self.tickets = resources.AsyncTicketsResource(self)
        self.visitors = resources.AsyncVisitorsResource(self)
        self.with_raw_response = AsyncIntercomWithRawResponse(self)
        self.with_streaming_response = AsyncIntercomWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        return {"Authorization": f"Bearer {access_token}"}

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
        access_token: str | None = None,
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
            access_token=access_token or self.access_token,
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
        self.me = resources.MeResourceWithRawResponse(client.me)
        self.admins = resources.AdminsResourceWithRawResponse(client.admins)
        self.articles = resources.ArticlesResourceWithRawResponse(client.articles)
        self.help_center = resources.HelpCenterResourceWithRawResponse(client.help_center)
        self.companies = resources.CompaniesResourceWithRawResponse(client.companies)
        self.contacts = resources.ContactsResourceWithRawResponse(client.contacts)
        self.conversations = resources.ConversationsResourceWithRawResponse(client.conversations)
        self.data_attributes = resources.DataAttributesResourceWithRawResponse(client.data_attributes)
        self.data_events = resources.DataEventsResourceWithRawResponse(client.data_events)
        self.data_exports = resources.DataExportsResourceWithRawResponse(client.data_exports)
        self.export = resources.ExportResourceWithRawResponse(client.export)
        self.download = resources.DownloadResourceWithRawResponse(client.download)
        self.messages = resources.MessagesResourceWithRawResponse(client.messages)
        self.news = resources.NewsResourceWithRawResponse(client.news)
        self.notes = resources.NotesResourceWithRawResponse(client.notes)
        self.segments = resources.SegmentsResourceWithRawResponse(client.segments)
        self.subscription_types = resources.SubscriptionTypesResourceWithRawResponse(client.subscription_types)
        self.phone_call_redirects = resources.PhoneCallRedirectsResourceWithRawResponse(client.phone_call_redirects)
        self.tags = resources.TagsResourceWithRawResponse(client.tags)
        self.teams = resources.TeamsResourceWithRawResponse(client.teams)
        self.ticket_types = resources.TicketTypesResourceWithRawResponse(client.ticket_types)
        self.tickets = resources.TicketsResourceWithRawResponse(client.tickets)
        self.visitors = resources.VisitorsResourceWithRawResponse(client.visitors)


class AsyncIntercomWithRawResponse:
    def __init__(self, client: AsyncIntercom) -> None:
        self.me = resources.AsyncMeResourceWithRawResponse(client.me)
        self.admins = resources.AsyncAdminsResourceWithRawResponse(client.admins)
        self.articles = resources.AsyncArticlesResourceWithRawResponse(client.articles)
        self.help_center = resources.AsyncHelpCenterResourceWithRawResponse(client.help_center)
        self.companies = resources.AsyncCompaniesResourceWithRawResponse(client.companies)
        self.contacts = resources.AsyncContactsResourceWithRawResponse(client.contacts)
        self.conversations = resources.AsyncConversationsResourceWithRawResponse(client.conversations)
        self.data_attributes = resources.AsyncDataAttributesResourceWithRawResponse(client.data_attributes)
        self.data_events = resources.AsyncDataEventsResourceWithRawResponse(client.data_events)
        self.data_exports = resources.AsyncDataExportsResourceWithRawResponse(client.data_exports)
        self.export = resources.AsyncExportResourceWithRawResponse(client.export)
        self.download = resources.AsyncDownloadResourceWithRawResponse(client.download)
        self.messages = resources.AsyncMessagesResourceWithRawResponse(client.messages)
        self.news = resources.AsyncNewsResourceWithRawResponse(client.news)
        self.notes = resources.AsyncNotesResourceWithRawResponse(client.notes)
        self.segments = resources.AsyncSegmentsResourceWithRawResponse(client.segments)
        self.subscription_types = resources.AsyncSubscriptionTypesResourceWithRawResponse(client.subscription_types)
        self.phone_call_redirects = resources.AsyncPhoneCallRedirectsResourceWithRawResponse(
            client.phone_call_redirects
        )
        self.tags = resources.AsyncTagsResourceWithRawResponse(client.tags)
        self.teams = resources.AsyncTeamsResourceWithRawResponse(client.teams)
        self.ticket_types = resources.AsyncTicketTypesResourceWithRawResponse(client.ticket_types)
        self.tickets = resources.AsyncTicketsResourceWithRawResponse(client.tickets)
        self.visitors = resources.AsyncVisitorsResourceWithRawResponse(client.visitors)


class IntercomWithStreamedResponse:
    def __init__(self, client: Intercom) -> None:
        self.me = resources.MeResourceWithStreamingResponse(client.me)
        self.admins = resources.AdminsResourceWithStreamingResponse(client.admins)
        self.articles = resources.ArticlesResourceWithStreamingResponse(client.articles)
        self.help_center = resources.HelpCenterResourceWithStreamingResponse(client.help_center)
        self.companies = resources.CompaniesResourceWithStreamingResponse(client.companies)
        self.contacts = resources.ContactsResourceWithStreamingResponse(client.contacts)
        self.conversations = resources.ConversationsResourceWithStreamingResponse(client.conversations)
        self.data_attributes = resources.DataAttributesResourceWithStreamingResponse(client.data_attributes)
        self.data_events = resources.DataEventsResourceWithStreamingResponse(client.data_events)
        self.data_exports = resources.DataExportsResourceWithStreamingResponse(client.data_exports)
        self.export = resources.ExportResourceWithStreamingResponse(client.export)
        self.download = resources.DownloadResourceWithStreamingResponse(client.download)
        self.messages = resources.MessagesResourceWithStreamingResponse(client.messages)
        self.news = resources.NewsResourceWithStreamingResponse(client.news)
        self.notes = resources.NotesResourceWithStreamingResponse(client.notes)
        self.segments = resources.SegmentsResourceWithStreamingResponse(client.segments)
        self.subscription_types = resources.SubscriptionTypesResourceWithStreamingResponse(client.subscription_types)
        self.phone_call_redirects = resources.PhoneCallRedirectsResourceWithStreamingResponse(
            client.phone_call_redirects
        )
        self.tags = resources.TagsResourceWithStreamingResponse(client.tags)
        self.teams = resources.TeamsResourceWithStreamingResponse(client.teams)
        self.ticket_types = resources.TicketTypesResourceWithStreamingResponse(client.ticket_types)
        self.tickets = resources.TicketsResourceWithStreamingResponse(client.tickets)
        self.visitors = resources.VisitorsResourceWithStreamingResponse(client.visitors)


class AsyncIntercomWithStreamedResponse:
    def __init__(self, client: AsyncIntercom) -> None:
        self.me = resources.AsyncMeResourceWithStreamingResponse(client.me)
        self.admins = resources.AsyncAdminsResourceWithStreamingResponse(client.admins)
        self.articles = resources.AsyncArticlesResourceWithStreamingResponse(client.articles)
        self.help_center = resources.AsyncHelpCenterResourceWithStreamingResponse(client.help_center)
        self.companies = resources.AsyncCompaniesResourceWithStreamingResponse(client.companies)
        self.contacts = resources.AsyncContactsResourceWithStreamingResponse(client.contacts)
        self.conversations = resources.AsyncConversationsResourceWithStreamingResponse(client.conversations)
        self.data_attributes = resources.AsyncDataAttributesResourceWithStreamingResponse(client.data_attributes)
        self.data_events = resources.AsyncDataEventsResourceWithStreamingResponse(client.data_events)
        self.data_exports = resources.AsyncDataExportsResourceWithStreamingResponse(client.data_exports)
        self.export = resources.AsyncExportResourceWithStreamingResponse(client.export)
        self.download = resources.AsyncDownloadResourceWithStreamingResponse(client.download)
        self.messages = resources.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.news = resources.AsyncNewsResourceWithStreamingResponse(client.news)
        self.notes = resources.AsyncNotesResourceWithStreamingResponse(client.notes)
        self.segments = resources.AsyncSegmentsResourceWithStreamingResponse(client.segments)
        self.subscription_types = resources.AsyncSubscriptionTypesResourceWithStreamingResponse(
            client.subscription_types
        )
        self.phone_call_redirects = resources.AsyncPhoneCallRedirectsResourceWithStreamingResponse(
            client.phone_call_redirects
        )
        self.tags = resources.AsyncTagsResourceWithStreamingResponse(client.tags)
        self.teams = resources.AsyncTeamsResourceWithStreamingResponse(client.teams)
        self.ticket_types = resources.AsyncTicketTypesResourceWithStreamingResponse(client.ticket_types)
        self.tickets = resources.AsyncTicketsResourceWithStreamingResponse(client.tickets)
        self.visitors = resources.AsyncVisitorsResourceWithStreamingResponse(client.visitors)


Client = Intercom

AsyncClient = AsyncIntercom
