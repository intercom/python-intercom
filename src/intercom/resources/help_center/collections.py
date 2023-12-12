# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.help_center import (
    Collection,
    CollectionList,
    DeletedCollectionObject,
    collection_create_params,
    collection_update_params,
)

if TYPE_CHECKING:
    from ..._client import Intercom, AsyncIntercom

__all__ = ["Collections", "AsyncCollections"]


class Collections(SyncAPIResource):
    with_raw_response: CollectionsWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = CollectionsWithRawResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        help_center_id: Optional[int] | NotGiven = NOT_GIVEN,
        parent_id: Optional[str] | NotGiven = NOT_GIVEN,
        translated_content: Optional[collection_create_params.TranslatedContent] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        You can create a new collection by making a POST request to
        `https://api.intercom.io/help_center/collections.`

        Args:
          name: The name of the collection. For multilingual collections, this will be the name
              of the default language's content.

          description: The description of the collection. For multilingual collections, this will be
              the description of the default language's content.

          help_center_id: The id of the help center where the collection will be created. If `null` then
              it will be created in the default help center.

          parent_id: The id of the parent collection. If `null` then it will be created as the first
              level collection.

          translated_content: The Translated Content of an Group. The keys are the locale codes and the values
              are the translated content of the Group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/help_center/collections",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "help_center_id": help_center_id,
                    "parent_id": parent_id,
                    "translated_content": translated_content,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
        )

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        You can fetch the details of a single collection by making a GET request to
        `https://api.intercom.io/help_center/collections/<id>`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/help_center/collections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
        )

    def update(
        self,
        id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: Optional[str] | NotGiven = NOT_GIVEN,
        translated_content: Optional[collection_update_params.TranslatedContent] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        You can update the details of a single collection by making a PUT request to
        `https://api.intercom.io/collections/<id>`.

        Args:
          description: The description of the collection. For multilingual collections, this will be
              the description of the default language's content.

          name: The name of the collection. For multilingual collections, this will be the name
              of the default language's content.

          parent_id: The id of the parent collection. If `null` then it will be updated as the first
              level collection.

          translated_content: The Translated Content of an Group. The keys are the locale codes and the values
              are the translated content of the Group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/help_center/collections/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "parent_id": parent_id,
                    "translated_content": translated_content,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
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
    ) -> CollectionList:
        """
        You can fetch a list of all collections by making a GET request to
        `https://api.intercom.io/help_center/collections`.

        > 📘 How are the collections sorted and ordered?
        >
        > Collections will be returned in descending order on the `updated_at`
        > attribute. This means if you need to iterate through results then we'll show
        > the most recently updated collections first.
        """
        return self._get(
            "/help_center/collections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionList,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedCollectionObject:
        """
        You can delete a single collection by making a DELETE request to
        `https://api.intercom.io/collections/<id>`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/help_center/collections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedCollectionObject,
        )


class AsyncCollections(AsyncAPIResource):
    with_raw_response: AsyncCollectionsWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCollectionsWithRawResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        help_center_id: Optional[int] | NotGiven = NOT_GIVEN,
        parent_id: Optional[str] | NotGiven = NOT_GIVEN,
        translated_content: Optional[collection_create_params.TranslatedContent] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        You can create a new collection by making a POST request to
        `https://api.intercom.io/help_center/collections.`

        Args:
          name: The name of the collection. For multilingual collections, this will be the name
              of the default language's content.

          description: The description of the collection. For multilingual collections, this will be
              the description of the default language's content.

          help_center_id: The id of the help center where the collection will be created. If `null` then
              it will be created in the default help center.

          parent_id: The id of the parent collection. If `null` then it will be created as the first
              level collection.

          translated_content: The Translated Content of an Group. The keys are the locale codes and the values
              are the translated content of the Group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/help_center/collections",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "help_center_id": help_center_id,
                    "parent_id": parent_id,
                    "translated_content": translated_content,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
        )

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        You can fetch the details of a single collection by making a GET request to
        `https://api.intercom.io/help_center/collections/<id>`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/help_center/collections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
        )

    async def update(
        self,
        id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parent_id: Optional[str] | NotGiven = NOT_GIVEN,
        translated_content: Optional[collection_update_params.TranslatedContent] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        You can update the details of a single collection by making a PUT request to
        `https://api.intercom.io/collections/<id>`.

        Args:
          description: The description of the collection. For multilingual collections, this will be
              the description of the default language's content.

          name: The name of the collection. For multilingual collections, this will be the name
              of the default language's content.

          parent_id: The id of the parent collection. If `null` then it will be updated as the first
              level collection.

          translated_content: The Translated Content of an Group. The keys are the locale codes and the values
              are the translated content of the Group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/help_center/collections/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "parent_id": parent_id,
                    "translated_content": translated_content,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
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
    ) -> CollectionList:
        """
        You can fetch a list of all collections by making a GET request to
        `https://api.intercom.io/help_center/collections`.

        > 📘 How are the collections sorted and ordered?
        >
        > Collections will be returned in descending order on the `updated_at`
        > attribute. This means if you need to iterate through results then we'll show
        > the most recently updated collections first.
        """
        return await self._get(
            "/help_center/collections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionList,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedCollectionObject:
        """
        You can delete a single collection by making a DELETE request to
        `https://api.intercom.io/collections/<id>`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/help_center/collections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedCollectionObject,
        )


class CollectionsWithRawResponse:
    def __init__(self, collections: Collections) -> None:
        self.create = to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            collections.update,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.delete = to_raw_response_wrapper(
            collections.delete,
        )


class AsyncCollectionsWithRawResponse:
    def __init__(self, collections: AsyncCollections) -> None:
        self.create = async_to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            collections.delete,
        )
