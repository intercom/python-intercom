# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ...types.ai import (
    ExternalPage,
    ExternalPagesList,
    external_page_create_params,
    external_page_update_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["ExternalPages", "AsyncExternalPages"]


class ExternalPages(SyncAPIResource):
    with_raw_response: ExternalPagesWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = ExternalPagesWithRawResponse(self)

    def create(
        self,
        *,
        html: str,
        locale: Literal["en"],
        source_id: int,
        title: str,
        url: str,
        external_id: str | NotGiven = NOT_GIVEN,
        fin_availability: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPage:
        """
        You can create a new external page by sending a POST request to this endpoint.
        If an external page already exists with the specified source_id and external_id,
        it will be updated instead.

        Args:
          html: The body of the external page in HTML.

          locale: Always en

          source_id: The unique identifier for the source of the external page which was given by
              Intercom. Every external page must be associated with a Content Import Source
              which represents the place it comes from and from which it inherits a default
              audience (configured in the UI). For a new source, make a POST request to the
              Content Import Source endpoint and an ID for the source will be returned in the
              response.

          title: The title of the external page.

          url: The URL of the external page. This will be used by Fin to link end users to the
              page it based its answer on.

          external_id: The identifier for the external page which was given by the source. Must be
              unique for the source.

          fin_availability: Whether the external page should be used to answer questions by Fin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/external_pages",
            body=maybe_transform(
                {
                    "html": html,
                    "locale": locale,
                    "source_id": source_id,
                    "title": title,
                    "url": url,
                    "external_id": external_id,
                    "fin_availability": fin_availability,
                },
                external_page_create_params.ExternalPageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPage,
        )

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
    ) -> ExternalPage:
        """
        You can retrieve an external page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/ai/external_pages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPage,
        )

    def update(
        self,
        id: str,
        *,
        html: str,
        locale: Literal["en"],
        source_id: int,
        title: str,
        url: str,
        external_id: str | NotGiven = NOT_GIVEN,
        fin_availability: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPage:
        """
        You can update an existing external page (if it was created via the API).

        Args:
          html: The body of the external page in HTML.

          locale: Always en

          source_id: The unique identifier for the source of the external page which was given by
              Intercom. Every external page must be associated with a Content Import Source
              which represents the place it comes from and from which it inherits a default
              audience (configured in the UI). For a new source, make a POST request to the
              Content Import Source endpoint and an ID for the source will be returned in the
              response.

          title: The title of the external page.

          url: The URL of the external page. This will be used by Fin to link end users to the
              page it based its answer on.

          external_id: The identifier for the external page which was given by the source. Must be
              unique for the source.

          fin_availability: Whether the external page should be used to answer questions by Fin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/ai/external_pages/{id}",
            body=maybe_transform(
                {
                    "html": html,
                    "locale": locale,
                    "source_id": source_id,
                    "title": title,
                    "url": url,
                    "external_id": external_id,
                    "fin_availability": fin_availability,
                },
                external_page_update_params.ExternalPageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPage,
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
    ) -> ExternalPagesList:
        """You can retrieve a list of all external pages for a workspace."""
        return self._get(
            "/ai/external_pages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPagesList,
        )

    def remove_all(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPage:
        """
        Sending a DELETE request for an external page will remove it from the content
        library UI and from being used for AI answers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/ai/external_pages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPage,
        )


class AsyncExternalPages(AsyncAPIResource):
    with_raw_response: AsyncExternalPagesWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncExternalPagesWithRawResponse(self)

    async def create(
        self,
        *,
        html: str,
        locale: Literal["en"],
        source_id: int,
        title: str,
        url: str,
        external_id: str | NotGiven = NOT_GIVEN,
        fin_availability: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPage:
        """
        You can create a new external page by sending a POST request to this endpoint.
        If an external page already exists with the specified source_id and external_id,
        it will be updated instead.

        Args:
          html: The body of the external page in HTML.

          locale: Always en

          source_id: The unique identifier for the source of the external page which was given by
              Intercom. Every external page must be associated with a Content Import Source
              which represents the place it comes from and from which it inherits a default
              audience (configured in the UI). For a new source, make a POST request to the
              Content Import Source endpoint and an ID for the source will be returned in the
              response.

          title: The title of the external page.

          url: The URL of the external page. This will be used by Fin to link end users to the
              page it based its answer on.

          external_id: The identifier for the external page which was given by the source. Must be
              unique for the source.

          fin_availability: Whether the external page should be used to answer questions by Fin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/external_pages",
            body=maybe_transform(
                {
                    "html": html,
                    "locale": locale,
                    "source_id": source_id,
                    "title": title,
                    "url": url,
                    "external_id": external_id,
                    "fin_availability": fin_availability,
                },
                external_page_create_params.ExternalPageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPage,
        )

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
    ) -> ExternalPage:
        """
        You can retrieve an external page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/ai/external_pages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPage,
        )

    async def update(
        self,
        id: str,
        *,
        html: str,
        locale: Literal["en"],
        source_id: int,
        title: str,
        url: str,
        external_id: str | NotGiven = NOT_GIVEN,
        fin_availability: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPage:
        """
        You can update an existing external page (if it was created via the API).

        Args:
          html: The body of the external page in HTML.

          locale: Always en

          source_id: The unique identifier for the source of the external page which was given by
              Intercom. Every external page must be associated with a Content Import Source
              which represents the place it comes from and from which it inherits a default
              audience (configured in the UI). For a new source, make a POST request to the
              Content Import Source endpoint and an ID for the source will be returned in the
              response.

          title: The title of the external page.

          url: The URL of the external page. This will be used by Fin to link end users to the
              page it based its answer on.

          external_id: The identifier for the external page which was given by the source. Must be
              unique for the source.

          fin_availability: Whether the external page should be used to answer questions by Fin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/ai/external_pages/{id}",
            body=maybe_transform(
                {
                    "html": html,
                    "locale": locale,
                    "source_id": source_id,
                    "title": title,
                    "url": url,
                    "external_id": external_id,
                    "fin_availability": fin_availability,
                },
                external_page_update_params.ExternalPageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPage,
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
    ) -> ExternalPagesList:
        """You can retrieve a list of all external pages for a workspace."""
        return await self._get(
            "/ai/external_pages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPagesList,
        )

    async def remove_all(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPage:
        """
        Sending a DELETE request for an external page will remove it from the content
        library UI and from being used for AI answers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/ai/external_pages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPage,
        )


class ExternalPagesWithRawResponse:
    def __init__(self, external_pages: ExternalPages) -> None:
        self.create = to_raw_response_wrapper(
            external_pages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            external_pages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            external_pages.update,
        )
        self.list = to_raw_response_wrapper(
            external_pages.list,
        )
        self.remove_all = to_raw_response_wrapper(
            external_pages.remove_all,
        )


class AsyncExternalPagesWithRawResponse:
    def __init__(self, external_pages: AsyncExternalPages) -> None:
        self.create = async_to_raw_response_wrapper(
            external_pages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            external_pages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            external_pages.update,
        )
        self.list = async_to_raw_response_wrapper(
            external_pages.list,
        )
        self.remove_all = async_to_raw_response_wrapper(
            external_pages.remove_all,
        )
