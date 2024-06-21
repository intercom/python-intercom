# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import overload
from typing_extensions import Literal

import httpx

from ..types import data_event_list_params, data_event_create_params, data_event_summaries_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    required_args,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.data_event_summary import DataEventSummary

__all__ = ["DataEventsResource", "AsyncDataEventsResource"]


class DataEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataEventsResourceWithRawResponse:
        return DataEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataEventsResourceWithStreamingResponse:
        return DataEventsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        body: object,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """You will need an Access Token that has write permissions to send Events.

        Once
        you have a key you can submit events via POST to the Events resource, which is
        located at https://api.intercom.io/events, or you can send events using one of
        the client libraries. When working with the HTTP API directly a client should
        send the event with a `Content-Type` of `application/json`.

        When using the JavaScript API,
        [adding the code to your app](http://docs.intercom.io/configuring-Intercom/tracking-user-events-in-your-app)
        makes the Events API available. Once added, you can submit an event using the
        `trackEvent` method. This will associate the event with the Lead or currently
        logged-in user or logged-out visitor/lead and send it to Intercom. The final
        parameter is a map that can be used to send optional metadata about the event.

        With the Ruby client you pass a hash describing the event to
        `Intercom::Event.create`, or call the `track_user` method directly on the
        current user object (e.g. `user.track_event`).

        **NB: For the JSON object types, please note that we do not currently support
        nested JSON structure.**

        | Type            | Description                                                                                                                                                                                                     | Example                                                                           |
        | :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
        | String          | The value is a JSON String                                                                                                                                                                                      | `"source":"desktop"`                                                              |
        | Number          | The value is a JSON Number                                                                                                                                                                                      | `"load": 3.67`                                                                    |
        | Date            | The key ends with the String `_date` and the value is a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time), assumed to be in the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) timezone. | `"contact_date": 1392036272`                                                      |
        | Link            | The value is a HTTP or HTTPS URI.                                                                                                                                                                               | `"article": "https://example.org/ab1de.html"`                                     |
        | Rich Link       | The value is a JSON object that contains `url` and `value` keys.                                                                                                                                                | `"article": {"url": "https://example.org/ab1de.html", "value":"the dude abides"}` |
        | Monetary Amount | The value is a JSON object that contains `amount` and `currency` keys. The `amount` key is a positive integer representing the amount in cents. The price in the example to the right denotes €349.99.          | `"price": {"amount": 34999, "currency": "eur"}`                                   |

        **Lead Events**

        When submitting events for Leads, you will need to specify the Lead's `id`.

        **Metadata behaviour**

        - We currently limit the number of tracked metadata keys to 10 per event. Once
          the quota is reached, we ignore any further keys we receive. The first 10
          metadata keys are determined by the order in which they are sent in with the
          event.
        - It is not possible to change the metadata keys once the event has been sent. A
          new event will need to be created with the new keys and you can archive the
          old one.
        - There might be up to 24 hrs delay when you send a new metadata for an existing
          event.

        **Event de-duplication**

        The API may detect and ignore duplicate events. Each event is uniquely
        identified as a combination of the following data - the Workspace identifier,
        the Contact external identifier, the Data Event name and the Data Event created
        time. As a result, it is **strongly recommended** to send a second granularity
        Unix timestamp in the `created_at` field.

        Duplicated events are responded to using the normal `202 Accepted` code - an
        error is not thrown, however repeat requests will be counted against any rate
        limit that is in place.

        ### HTTP API Responses

        - Successful responses to submitted events return `202 Accepted` with an empty
          body.
        - Unauthorised access will be rejected with a `401 Unauthorized` or
          `403 Forbidden` response code.
        - Events sent about users that cannot be found will return a `404 Not Found`.
        - Event lists containing duplicate events will have those duplicates ignored.
        - Server errors will return a `500` response code and may contain an error
          message in the body.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        body: object,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """You will need an Access Token that has write permissions to send Events.

        Once
        you have a key you can submit events via POST to the Events resource, which is
        located at https://api.intercom.io/events, or you can send events using one of
        the client libraries. When working with the HTTP API directly a client should
        send the event with a `Content-Type` of `application/json`.

        When using the JavaScript API,
        [adding the code to your app](http://docs.intercom.io/configuring-Intercom/tracking-user-events-in-your-app)
        makes the Events API available. Once added, you can submit an event using the
        `trackEvent` method. This will associate the event with the Lead or currently
        logged-in user or logged-out visitor/lead and send it to Intercom. The final
        parameter is a map that can be used to send optional metadata about the event.

        With the Ruby client you pass a hash describing the event to
        `Intercom::Event.create`, or call the `track_user` method directly on the
        current user object (e.g. `user.track_event`).

        **NB: For the JSON object types, please note that we do not currently support
        nested JSON structure.**

        | Type            | Description                                                                                                                                                                                                     | Example                                                                           |
        | :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
        | String          | The value is a JSON String                                                                                                                                                                                      | `"source":"desktop"`                                                              |
        | Number          | The value is a JSON Number                                                                                                                                                                                      | `"load": 3.67`                                                                    |
        | Date            | The key ends with the String `_date` and the value is a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time), assumed to be in the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) timezone. | `"contact_date": 1392036272`                                                      |
        | Link            | The value is a HTTP or HTTPS URI.                                                                                                                                                                               | `"article": "https://example.org/ab1de.html"`                                     |
        | Rich Link       | The value is a JSON object that contains `url` and `value` keys.                                                                                                                                                | `"article": {"url": "https://example.org/ab1de.html", "value":"the dude abides"}` |
        | Monetary Amount | The value is a JSON object that contains `amount` and `currency` keys. The `amount` key is a positive integer representing the amount in cents. The price in the example to the right denotes €349.99.          | `"price": {"amount": 34999, "currency": "eur"}`                                   |

        **Lead Events**

        When submitting events for Leads, you will need to specify the Lead's `id`.

        **Metadata behaviour**

        - We currently limit the number of tracked metadata keys to 10 per event. Once
          the quota is reached, we ignore any further keys we receive. The first 10
          metadata keys are determined by the order in which they are sent in with the
          event.
        - It is not possible to change the metadata keys once the event has been sent. A
          new event will need to be created with the new keys and you can archive the
          old one.
        - There might be up to 24 hrs delay when you send a new metadata for an existing
          event.

        **Event de-duplication**

        The API may detect and ignore duplicate events. Each event is uniquely
        identified as a combination of the following data - the Workspace identifier,
        the Contact external identifier, the Data Event name and the Data Event created
        time. As a result, it is **strongly recommended** to send a second granularity
        Unix timestamp in the `created_at` field.

        Duplicated events are responded to using the normal `202 Accepted` code - an
        error is not thrown, however repeat requests will be counted against any rate
        limit that is in place.

        ### HTTP API Responses

        - Successful responses to submitted events return `202 Accepted` with an empty
          body.
        - Unauthorised access will be rejected with a `401 Unauthorized` or
          `403 Forbidden` response code.
        - Events sent about users that cannot be found will return a `404 Not Found`.
        - Event lists containing duplicate events will have those duplicates ignored.
        - Server errors will return a `500` response code and may contain an error
          message in the body.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        body: object,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """You will need an Access Token that has write permissions to send Events.

        Once
        you have a key you can submit events via POST to the Events resource, which is
        located at https://api.intercom.io/events, or you can send events using one of
        the client libraries. When working with the HTTP API directly a client should
        send the event with a `Content-Type` of `application/json`.

        When using the JavaScript API,
        [adding the code to your app](http://docs.intercom.io/configuring-Intercom/tracking-user-events-in-your-app)
        makes the Events API available. Once added, you can submit an event using the
        `trackEvent` method. This will associate the event with the Lead or currently
        logged-in user or logged-out visitor/lead and send it to Intercom. The final
        parameter is a map that can be used to send optional metadata about the event.

        With the Ruby client you pass a hash describing the event to
        `Intercom::Event.create`, or call the `track_user` method directly on the
        current user object (e.g. `user.track_event`).

        **NB: For the JSON object types, please note that we do not currently support
        nested JSON structure.**

        | Type            | Description                                                                                                                                                                                                     | Example                                                                           |
        | :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
        | String          | The value is a JSON String                                                                                                                                                                                      | `"source":"desktop"`                                                              |
        | Number          | The value is a JSON Number                                                                                                                                                                                      | `"load": 3.67`                                                                    |
        | Date            | The key ends with the String `_date` and the value is a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time), assumed to be in the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) timezone. | `"contact_date": 1392036272`                                                      |
        | Link            | The value is a HTTP or HTTPS URI.                                                                                                                                                                               | `"article": "https://example.org/ab1de.html"`                                     |
        | Rich Link       | The value is a JSON object that contains `url` and `value` keys.                                                                                                                                                | `"article": {"url": "https://example.org/ab1de.html", "value":"the dude abides"}` |
        | Monetary Amount | The value is a JSON object that contains `amount` and `currency` keys. The `amount` key is a positive integer representing the amount in cents. The price in the example to the right denotes €349.99.          | `"price": {"amount": 34999, "currency": "eur"}`                                   |

        **Lead Events**

        When submitting events for Leads, you will need to specify the Lead's `id`.

        **Metadata behaviour**

        - We currently limit the number of tracked metadata keys to 10 per event. Once
          the quota is reached, we ignore any further keys we receive. The first 10
          metadata keys are determined by the order in which they are sent in with the
          event.
        - It is not possible to change the metadata keys once the event has been sent. A
          new event will need to be created with the new keys and you can archive the
          old one.
        - There might be up to 24 hrs delay when you send a new metadata for an existing
          event.

        **Event de-duplication**

        The API may detect and ignore duplicate events. Each event is uniquely
        identified as a combination of the following data - the Workspace identifier,
        the Contact external identifier, the Data Event name and the Data Event created
        time. As a result, it is **strongly recommended** to send a second granularity
        Unix timestamp in the `created_at` field.

        Duplicated events are responded to using the normal `202 Accepted` code - an
        error is not thrown, however repeat requests will be counted against any rate
        limit that is in place.

        ### HTTP API Responses

        - Successful responses to submitted events return `202 Accepted` with an empty
          body.
        - Unauthorised access will be rejected with a `401 Unauthorized` or
          `403 Forbidden` response code.
        - Events sent about users that cannot be found will return a `404 Not Found`.
        - Event lists containing duplicate events will have those duplicates ignored.
        - Server errors will return a `500` response code and may contain an error
          message in the body.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body"])
    def create(
        self,
        *,
        body: object,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._post(
            "/events",
            body=maybe_transform(body, data_event_create_params.DataEventCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        filter: data_event_list_params.Filter,
        type: str,
        summary: bool | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataEventSummary:
        """
        > 🚧
        >
        > Please note that you can only 'list' events that are less than 90 days old.
        > Event counts and summaries will still include your events older than 90 days
        > but you cannot 'list' these events individually if they are older than 90 days

        The events belonging to a customer can be listed by sending a GET request to
        `https://api.intercom.io/events` with a user or lead identifier along with a
        `type` parameter. The identifier parameter can be one of `user_id`, `email` or
        `intercom_user_id`. The `type` parameter value must be `user`.

        - `https://api.intercom.io/events?type=user&user_id={user_id}`
        - `https://api.intercom.io/events?type=user&email={email}`
        - `https://api.intercom.io/events?type=user&intercom_user_id={id}` (this call
          can be used to list leads)

        The `email` parameter value should be
        [url encoded](http://en.wikipedia.org/wiki/Percent-encoding) when sending.

        You can optionally define the result page size as well with the `per_page`
        parameter.

        Args:
          type: The value must be user

          summary: summary flag

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._get(
            "/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "type": type,
                        "summary": summary,
                    },
                    data_event_list_params.DataEventListParams,
                ),
            ),
            cast_to=DataEventSummary,
        )

    def summaries(
        self,
        *,
        event_summaries: data_event_summaries_params.EventSummaries | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Create event summaries for a user.

        Event summaries are used to track the number
        of times an event has occurred, the first time it occurred and the last time it
        occurred.

        Args:
          event_summaries: A list of event summaries for the user. Each event summary should contain the
              event name, the time the event occurred, and the number of times the event
              occurred. The event name should be a past tense 'verb-noun' combination, to
              improve readability, for example `updated-plan`.

          user_id: Your identifier for the user.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return self._post(
            "/events/summaries",
            body=maybe_transform(
                {
                    "event_summaries": event_summaries,
                    "user_id": user_id,
                },
                data_event_summaries_params.DataEventSummariesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDataEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataEventsResourceWithRawResponse:
        return AsyncDataEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataEventsResourceWithStreamingResponse:
        return AsyncDataEventsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        body: object,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """You will need an Access Token that has write permissions to send Events.

        Once
        you have a key you can submit events via POST to the Events resource, which is
        located at https://api.intercom.io/events, or you can send events using one of
        the client libraries. When working with the HTTP API directly a client should
        send the event with a `Content-Type` of `application/json`.

        When using the JavaScript API,
        [adding the code to your app](http://docs.intercom.io/configuring-Intercom/tracking-user-events-in-your-app)
        makes the Events API available. Once added, you can submit an event using the
        `trackEvent` method. This will associate the event with the Lead or currently
        logged-in user or logged-out visitor/lead and send it to Intercom. The final
        parameter is a map that can be used to send optional metadata about the event.

        With the Ruby client you pass a hash describing the event to
        `Intercom::Event.create`, or call the `track_user` method directly on the
        current user object (e.g. `user.track_event`).

        **NB: For the JSON object types, please note that we do not currently support
        nested JSON structure.**

        | Type            | Description                                                                                                                                                                                                     | Example                                                                           |
        | :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
        | String          | The value is a JSON String                                                                                                                                                                                      | `"source":"desktop"`                                                              |
        | Number          | The value is a JSON Number                                                                                                                                                                                      | `"load": 3.67`                                                                    |
        | Date            | The key ends with the String `_date` and the value is a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time), assumed to be in the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) timezone. | `"contact_date": 1392036272`                                                      |
        | Link            | The value is a HTTP or HTTPS URI.                                                                                                                                                                               | `"article": "https://example.org/ab1de.html"`                                     |
        | Rich Link       | The value is a JSON object that contains `url` and `value` keys.                                                                                                                                                | `"article": {"url": "https://example.org/ab1de.html", "value":"the dude abides"}` |
        | Monetary Amount | The value is a JSON object that contains `amount` and `currency` keys. The `amount` key is a positive integer representing the amount in cents. The price in the example to the right denotes €349.99.          | `"price": {"amount": 34999, "currency": "eur"}`                                   |

        **Lead Events**

        When submitting events for Leads, you will need to specify the Lead's `id`.

        **Metadata behaviour**

        - We currently limit the number of tracked metadata keys to 10 per event. Once
          the quota is reached, we ignore any further keys we receive. The first 10
          metadata keys are determined by the order in which they are sent in with the
          event.
        - It is not possible to change the metadata keys once the event has been sent. A
          new event will need to be created with the new keys and you can archive the
          old one.
        - There might be up to 24 hrs delay when you send a new metadata for an existing
          event.

        **Event de-duplication**

        The API may detect and ignore duplicate events. Each event is uniquely
        identified as a combination of the following data - the Workspace identifier,
        the Contact external identifier, the Data Event name and the Data Event created
        time. As a result, it is **strongly recommended** to send a second granularity
        Unix timestamp in the `created_at` field.

        Duplicated events are responded to using the normal `202 Accepted` code - an
        error is not thrown, however repeat requests will be counted against any rate
        limit that is in place.

        ### HTTP API Responses

        - Successful responses to submitted events return `202 Accepted` with an empty
          body.
        - Unauthorised access will be rejected with a `401 Unauthorized` or
          `403 Forbidden` response code.
        - Events sent about users that cannot be found will return a `404 Not Found`.
        - Event lists containing duplicate events will have those duplicates ignored.
        - Server errors will return a `500` response code and may contain an error
          message in the body.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        body: object,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """You will need an Access Token that has write permissions to send Events.

        Once
        you have a key you can submit events via POST to the Events resource, which is
        located at https://api.intercom.io/events, or you can send events using one of
        the client libraries. When working with the HTTP API directly a client should
        send the event with a `Content-Type` of `application/json`.

        When using the JavaScript API,
        [adding the code to your app](http://docs.intercom.io/configuring-Intercom/tracking-user-events-in-your-app)
        makes the Events API available. Once added, you can submit an event using the
        `trackEvent` method. This will associate the event with the Lead or currently
        logged-in user or logged-out visitor/lead and send it to Intercom. The final
        parameter is a map that can be used to send optional metadata about the event.

        With the Ruby client you pass a hash describing the event to
        `Intercom::Event.create`, or call the `track_user` method directly on the
        current user object (e.g. `user.track_event`).

        **NB: For the JSON object types, please note that we do not currently support
        nested JSON structure.**

        | Type            | Description                                                                                                                                                                                                     | Example                                                                           |
        | :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
        | String          | The value is a JSON String                                                                                                                                                                                      | `"source":"desktop"`                                                              |
        | Number          | The value is a JSON Number                                                                                                                                                                                      | `"load": 3.67`                                                                    |
        | Date            | The key ends with the String `_date` and the value is a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time), assumed to be in the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) timezone. | `"contact_date": 1392036272`                                                      |
        | Link            | The value is a HTTP or HTTPS URI.                                                                                                                                                                               | `"article": "https://example.org/ab1de.html"`                                     |
        | Rich Link       | The value is a JSON object that contains `url` and `value` keys.                                                                                                                                                | `"article": {"url": "https://example.org/ab1de.html", "value":"the dude abides"}` |
        | Monetary Amount | The value is a JSON object that contains `amount` and `currency` keys. The `amount` key is a positive integer representing the amount in cents. The price in the example to the right denotes €349.99.          | `"price": {"amount": 34999, "currency": "eur"}`                                   |

        **Lead Events**

        When submitting events for Leads, you will need to specify the Lead's `id`.

        **Metadata behaviour**

        - We currently limit the number of tracked metadata keys to 10 per event. Once
          the quota is reached, we ignore any further keys we receive. The first 10
          metadata keys are determined by the order in which they are sent in with the
          event.
        - It is not possible to change the metadata keys once the event has been sent. A
          new event will need to be created with the new keys and you can archive the
          old one.
        - There might be up to 24 hrs delay when you send a new metadata for an existing
          event.

        **Event de-duplication**

        The API may detect and ignore duplicate events. Each event is uniquely
        identified as a combination of the following data - the Workspace identifier,
        the Contact external identifier, the Data Event name and the Data Event created
        time. As a result, it is **strongly recommended** to send a second granularity
        Unix timestamp in the `created_at` field.

        Duplicated events are responded to using the normal `202 Accepted` code - an
        error is not thrown, however repeat requests will be counted against any rate
        limit that is in place.

        ### HTTP API Responses

        - Successful responses to submitted events return `202 Accepted` with an empty
          body.
        - Unauthorised access will be rejected with a `401 Unauthorized` or
          `403 Forbidden` response code.
        - Events sent about users that cannot be found will return a `404 Not Found`.
        - Event lists containing duplicate events will have those duplicates ignored.
        - Server errors will return a `500` response code and may contain an error
          message in the body.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        body: object,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """You will need an Access Token that has write permissions to send Events.

        Once
        you have a key you can submit events via POST to the Events resource, which is
        located at https://api.intercom.io/events, or you can send events using one of
        the client libraries. When working with the HTTP API directly a client should
        send the event with a `Content-Type` of `application/json`.

        When using the JavaScript API,
        [adding the code to your app](http://docs.intercom.io/configuring-Intercom/tracking-user-events-in-your-app)
        makes the Events API available. Once added, you can submit an event using the
        `trackEvent` method. This will associate the event with the Lead or currently
        logged-in user or logged-out visitor/lead and send it to Intercom. The final
        parameter is a map that can be used to send optional metadata about the event.

        With the Ruby client you pass a hash describing the event to
        `Intercom::Event.create`, or call the `track_user` method directly on the
        current user object (e.g. `user.track_event`).

        **NB: For the JSON object types, please note that we do not currently support
        nested JSON structure.**

        | Type            | Description                                                                                                                                                                                                     | Example                                                                           |
        | :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
        | String          | The value is a JSON String                                                                                                                                                                                      | `"source":"desktop"`                                                              |
        | Number          | The value is a JSON Number                                                                                                                                                                                      | `"load": 3.67`                                                                    |
        | Date            | The key ends with the String `_date` and the value is a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time), assumed to be in the [UTC](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) timezone. | `"contact_date": 1392036272`                                                      |
        | Link            | The value is a HTTP or HTTPS URI.                                                                                                                                                                               | `"article": "https://example.org/ab1de.html"`                                     |
        | Rich Link       | The value is a JSON object that contains `url` and `value` keys.                                                                                                                                                | `"article": {"url": "https://example.org/ab1de.html", "value":"the dude abides"}` |
        | Monetary Amount | The value is a JSON object that contains `amount` and `currency` keys. The `amount` key is a positive integer representing the amount in cents. The price in the example to the right denotes €349.99.          | `"price": {"amount": 34999, "currency": "eur"}`                                   |

        **Lead Events**

        When submitting events for Leads, you will need to specify the Lead's `id`.

        **Metadata behaviour**

        - We currently limit the number of tracked metadata keys to 10 per event. Once
          the quota is reached, we ignore any further keys we receive. The first 10
          metadata keys are determined by the order in which they are sent in with the
          event.
        - It is not possible to change the metadata keys once the event has been sent. A
          new event will need to be created with the new keys and you can archive the
          old one.
        - There might be up to 24 hrs delay when you send a new metadata for an existing
          event.

        **Event de-duplication**

        The API may detect and ignore duplicate events. Each event is uniquely
        identified as a combination of the following data - the Workspace identifier,
        the Contact external identifier, the Data Event name and the Data Event created
        time. As a result, it is **strongly recommended** to send a second granularity
        Unix timestamp in the `created_at` field.

        Duplicated events are responded to using the normal `202 Accepted` code - an
        error is not thrown, however repeat requests will be counted against any rate
        limit that is in place.

        ### HTTP API Responses

        - Successful responses to submitted events return `202 Accepted` with an empty
          body.
        - Unauthorised access will be rejected with a `401 Unauthorized` or
          `403 Forbidden` response code.
        - Events sent about users that cannot be found will return a `404 Not Found`.
        - Event lists containing duplicate events will have those duplicates ignored.
        - Server errors will return a `500` response code and may contain an error
          message in the body.

        Args:
          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["body"])
    async def create(
        self,
        *,
        body: object,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._post(
            "/events",
            body=await async_maybe_transform(body, data_event_create_params.DataEventCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        filter: data_event_list_params.Filter,
        type: str,
        summary: bool | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataEventSummary:
        """
        > 🚧
        >
        > Please note that you can only 'list' events that are less than 90 days old.
        > Event counts and summaries will still include your events older than 90 days
        > but you cannot 'list' these events individually if they are older than 90 days

        The events belonging to a customer can be listed by sending a GET request to
        `https://api.intercom.io/events` with a user or lead identifier along with a
        `type` parameter. The identifier parameter can be one of `user_id`, `email` or
        `intercom_user_id`. The `type` parameter value must be `user`.

        - `https://api.intercom.io/events?type=user&user_id={user_id}`
        - `https://api.intercom.io/events?type=user&email={email}`
        - `https://api.intercom.io/events?type=user&intercom_user_id={id}` (this call
          can be used to list leads)

        The `email` parameter value should be
        [url encoded](http://en.wikipedia.org/wiki/Percent-encoding) when sending.

        You can optionally define the result page size as well with the `per_page`
        parameter.

        Args:
          type: The value must be user

          summary: summary flag

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._get(
            "/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "type": type,
                        "summary": summary,
                    },
                    data_event_list_params.DataEventListParams,
                ),
            ),
            cast_to=DataEventSummary,
        )

    async def summaries(
        self,
        *,
        event_summaries: data_event_summaries_params.EventSummaries | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        intercom_version: Literal[
            "1.0",
            "1.1",
            "1.2",
            "1.3",
            "1.4",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "2.11",
            "Unstable",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Create event summaries for a user.

        Event summaries are used to track the number
        of times an event has occurred, the first time it occurred and the last time it
        occurred.

        Args:
          event_summaries: A list of event summaries for the user. Each event summary should contain the
              event name, the time the event occurred, and the number of times the event
              occurred. The event name should be a past tense 'verb-noun' combination, to
              improve readability, for example `updated-plan`.

          user_id: Your identifier for the user.

          intercom_version: Intercom API version.By default, it's equal to the version set in the app
              package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Intercom-Version": str(intercom_version)}), **(extra_headers or {})}
        return await self._post(
            "/events/summaries",
            body=await async_maybe_transform(
                {
                    "event_summaries": event_summaries,
                    "user_id": user_id,
                },
                data_event_summaries_params.DataEventSummariesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DataEventsResourceWithRawResponse:
    def __init__(self, data_events: DataEventsResource) -> None:
        self._data_events = data_events

        self.create = to_raw_response_wrapper(
            data_events.create,
        )
        self.list = to_raw_response_wrapper(
            data_events.list,
        )
        self.summaries = to_raw_response_wrapper(
            data_events.summaries,
        )


class AsyncDataEventsResourceWithRawResponse:
    def __init__(self, data_events: AsyncDataEventsResource) -> None:
        self._data_events = data_events

        self.create = async_to_raw_response_wrapper(
            data_events.create,
        )
        self.list = async_to_raw_response_wrapper(
            data_events.list,
        )
        self.summaries = async_to_raw_response_wrapper(
            data_events.summaries,
        )


class DataEventsResourceWithStreamingResponse:
    def __init__(self, data_events: DataEventsResource) -> None:
        self._data_events = data_events

        self.create = to_streamed_response_wrapper(
            data_events.create,
        )
        self.list = to_streamed_response_wrapper(
            data_events.list,
        )
        self.summaries = to_streamed_response_wrapper(
            data_events.summaries,
        )


class AsyncDataEventsResourceWithStreamingResponse:
    def __init__(self, data_events: AsyncDataEventsResource) -> None:
        self._data_events = data_events

        self.create = async_to_streamed_response_wrapper(
            data_events.create,
        )
        self.list = async_to_streamed_response_wrapper(
            data_events.list,
        )
        self.summaries = async_to_streamed_response_wrapper(
            data_events.summaries,
        )
