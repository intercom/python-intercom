# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.team import Team
from .._base_client import (
    make_request_options,
)
from ..types.team_list import TeamList

__all__ = ["TeamsResource", "AsyncTeamsResource"]


class TeamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TeamsResourceWithRawResponse:
        return TeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamsResourceWithStreamingResponse:
        return TeamsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Team:
        """
        You can fetch the details of a single team, containing an array of admins that
        belong to this team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/teams/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamList:
        """This will return a list of team objects for the App."""
        return self._get(
            "/teams",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamList,
        )


class AsyncTeamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTeamsResourceWithRawResponse:
        return AsyncTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamsResourceWithStreamingResponse:
        return AsyncTeamsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Team:
        """
        You can fetch the details of a single team, containing an array of admins that
        belong to this team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/teams/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Team,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamList:
        """This will return a list of team objects for the App."""
        return await self._get(
            "/teams",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamList,
        )


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.retrieve = to_raw_response_wrapper(
            teams.retrieve,
        )
        self.list = to_raw_response_wrapper(
            teams.list,
        )


class AsyncTeamsResourceWithRawResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.retrieve = async_to_raw_response_wrapper(
            teams.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            teams.list,
        )


class TeamsResourceWithStreamingResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.retrieve = to_streamed_response_wrapper(
            teams.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            teams.list,
        )


class AsyncTeamsResourceWithStreamingResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.retrieve = async_to_streamed_response_wrapper(
            teams.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            teams.list,
        )
