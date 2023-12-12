# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    Article,
    ArticleList,
    DeletedArticleObject,
    ArticleSearchResponse,
    article_create_params,
    article_search_params,
    article_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Intercom, AsyncIntercom

__all__ = ["Articles", "AsyncArticles"]


class Articles(SyncAPIResource):
    with_raw_response: ArticlesWithRawResponse

    def __init__(self, client: Intercom) -> None:
        super().__init__(client)
        self.with_raw_response = ArticlesWithRawResponse(self)

    def create(
        self,
        *,
        author_id: int,
        title: str,
        body: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        parent_id: int | NotGiven = NOT_GIVEN,
        parent_type: str | NotGiven = NOT_GIVEN,
        state: Literal["published", "draft"] | NotGiven = NOT_GIVEN,
        translated_content: Optional[article_create_params.TranslatedContent] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Article:
        """
        You can create a new article by making a POST request to
        `https://api.intercom.io/articles`.

        Args:
          author_id: The id of the author of the article. For multilingual articles, this will be the
              id of the author of the default language's content. Must be a teammate on the
              help center's workspace.

          title: The title of the article.For multilingual articles, this will be the title of
              the default language's content.

          body: The content of the article. For multilingual articles, this will be the body of
              the default language's content.

          description: The description of the article. For multilingual articles, this will be the
              description of the default language's content.

          parent_id: The id of the article's parent collection or section. An article without this
              field stands alone.

          parent_type: The type of parent, which can either be a `collection` or `section`.

          state: Whether the article will be `published` or will be a `draft`. Defaults to draft.
              For multilingual articles, this will be the state of the default language's
              content.

          translated_content: The Translated Content of an Article. The keys are the locale codes and the
              values are the translated content of the article.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/articles",
            body=maybe_transform(
                {
                    "author_id": author_id,
                    "title": title,
                    "body": body,
                    "description": description,
                    "parent_id": parent_id,
                    "parent_type": parent_type,
                    "state": state,
                    "translated_content": translated_content,
                },
                article_create_params.ArticleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Article,
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
    ) -> Article:
        """
        You can fetch the details of a single article by making a GET request to
        `https://api.intercom.io/articles/<id>`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/articles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Article,
        )

    def update(
        self,
        id: int,
        *,
        author_id: int | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        parent_type: str | NotGiven = NOT_GIVEN,
        state: Literal["published", "draft"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        translated_content: Optional[article_update_params.TranslatedContent] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Article:
        """
        You can update the details of a single article by making a PUT request to
        `https://api.intercom.io/articles/<id>`.

        Args:
          author_id: The id of the author of the article. For multilingual articles, this will be the
              id of the author of the default language's content. Must be a teammate on the
              help center's workspace.

          body: The content of the article. For multilingual articles, this will be the body of
              the default language's content.

          description: The description of the article. For multilingual articles, this will be the
              description of the default language's content.

          parent_id: The id of the article's parent collection or section. An article without this
              field stands alone.

          parent_type: The type of parent, which can either be a `collection` or `section`.

          state: Whether the article will be `published` or will be a `draft`. Defaults to draft.
              For multilingual articles, this will be the state of the default language's
              content.

          title: The title of the article.For multilingual articles, this will be the title of
              the default language's content.

          translated_content: The Translated Content of an Article. The keys are the locale codes and the
              values are the translated content of the article.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/articles/{id}",
            body=maybe_transform(
                {
                    "author_id": author_id,
                    "body": body,
                    "description": description,
                    "parent_id": parent_id,
                    "parent_type": parent_type,
                    "state": state,
                    "title": title,
                    "translated_content": translated_content,
                },
                article_update_params.ArticleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Article,
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
    ) -> ArticleList:
        """
        You can fetch a list of all articles by making a GET request to
        `https://api.intercom.io/articles`.

        > 📘 How are the articles sorted and ordered?
        >
        > Articles will be returned in descending order on the `updated_at` attribute.
        > This means if you need to iterate through results then we'll show the most
        > recently updated articles first.
        """
        return self._get(
            "/articles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleList,
        )

    def remove(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedArticleObject:
        """
        You can delete a single article by making a DELETE request to
        `https://api.intercom.io/articles/<id>`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/articles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedArticleObject,
        )

    def search(
        self,
        *,
        help_center_id: int | NotGiven = NOT_GIVEN,
        highlight: bool | NotGiven = NOT_GIVEN,
        phrase: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArticleSearchResponse:
        """
        You can search for articles by making a GET request to
        `https://api.intercom.io/articles/search`.

        Args:
          help_center_id: The ID of the Help Center to search in.

          highlight: Return a highlighted version of the matching content within your articles. Refer
              to the response schema for more details.

          phrase: The phrase within your articles to search for.

          state: The state of the Articles returned. One of `published`, `draft` or `all`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/articles/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "help_center_id": help_center_id,
                        "highlight": highlight,
                        "phrase": phrase,
                        "state": state,
                    },
                    article_search_params.ArticleSearchParams,
                ),
            ),
            cast_to=ArticleSearchResponse,
        )


class AsyncArticles(AsyncAPIResource):
    with_raw_response: AsyncArticlesWithRawResponse

    def __init__(self, client: AsyncIntercom) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncArticlesWithRawResponse(self)

    async def create(
        self,
        *,
        author_id: int,
        title: str,
        body: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        parent_id: int | NotGiven = NOT_GIVEN,
        parent_type: str | NotGiven = NOT_GIVEN,
        state: Literal["published", "draft"] | NotGiven = NOT_GIVEN,
        translated_content: Optional[article_create_params.TranslatedContent] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Article:
        """
        You can create a new article by making a POST request to
        `https://api.intercom.io/articles`.

        Args:
          author_id: The id of the author of the article. For multilingual articles, this will be the
              id of the author of the default language's content. Must be a teammate on the
              help center's workspace.

          title: The title of the article.For multilingual articles, this will be the title of
              the default language's content.

          body: The content of the article. For multilingual articles, this will be the body of
              the default language's content.

          description: The description of the article. For multilingual articles, this will be the
              description of the default language's content.

          parent_id: The id of the article's parent collection or section. An article without this
              field stands alone.

          parent_type: The type of parent, which can either be a `collection` or `section`.

          state: Whether the article will be `published` or will be a `draft`. Defaults to draft.
              For multilingual articles, this will be the state of the default language's
              content.

          translated_content: The Translated Content of an Article. The keys are the locale codes and the
              values are the translated content of the article.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/articles",
            body=maybe_transform(
                {
                    "author_id": author_id,
                    "title": title,
                    "body": body,
                    "description": description,
                    "parent_id": parent_id,
                    "parent_type": parent_type,
                    "state": state,
                    "translated_content": translated_content,
                },
                article_create_params.ArticleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Article,
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
    ) -> Article:
        """
        You can fetch the details of a single article by making a GET request to
        `https://api.intercom.io/articles/<id>`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/articles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Article,
        )

    async def update(
        self,
        id: int,
        *,
        author_id: int | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        parent_id: str | NotGiven = NOT_GIVEN,
        parent_type: str | NotGiven = NOT_GIVEN,
        state: Literal["published", "draft"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        translated_content: Optional[article_update_params.TranslatedContent] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Article:
        """
        You can update the details of a single article by making a PUT request to
        `https://api.intercom.io/articles/<id>`.

        Args:
          author_id: The id of the author of the article. For multilingual articles, this will be the
              id of the author of the default language's content. Must be a teammate on the
              help center's workspace.

          body: The content of the article. For multilingual articles, this will be the body of
              the default language's content.

          description: The description of the article. For multilingual articles, this will be the
              description of the default language's content.

          parent_id: The id of the article's parent collection or section. An article without this
              field stands alone.

          parent_type: The type of parent, which can either be a `collection` or `section`.

          state: Whether the article will be `published` or will be a `draft`. Defaults to draft.
              For multilingual articles, this will be the state of the default language's
              content.

          title: The title of the article.For multilingual articles, this will be the title of
              the default language's content.

          translated_content: The Translated Content of an Article. The keys are the locale codes and the
              values are the translated content of the article.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/articles/{id}",
            body=maybe_transform(
                {
                    "author_id": author_id,
                    "body": body,
                    "description": description,
                    "parent_id": parent_id,
                    "parent_type": parent_type,
                    "state": state,
                    "title": title,
                    "translated_content": translated_content,
                },
                article_update_params.ArticleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Article,
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
    ) -> ArticleList:
        """
        You can fetch a list of all articles by making a GET request to
        `https://api.intercom.io/articles`.

        > 📘 How are the articles sorted and ordered?
        >
        > Articles will be returned in descending order on the `updated_at` attribute.
        > This means if you need to iterate through results then we'll show the most
        > recently updated articles first.
        """
        return await self._get(
            "/articles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArticleList,
        )

    async def remove(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletedArticleObject:
        """
        You can delete a single article by making a DELETE request to
        `https://api.intercom.io/articles/<id>`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/articles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletedArticleObject,
        )

    async def search(
        self,
        *,
        help_center_id: int | NotGiven = NOT_GIVEN,
        highlight: bool | NotGiven = NOT_GIVEN,
        phrase: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArticleSearchResponse:
        """
        You can search for articles by making a GET request to
        `https://api.intercom.io/articles/search`.

        Args:
          help_center_id: The ID of the Help Center to search in.

          highlight: Return a highlighted version of the matching content within your articles. Refer
              to the response schema for more details.

          phrase: The phrase within your articles to search for.

          state: The state of the Articles returned. One of `published`, `draft` or `all`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/articles/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "help_center_id": help_center_id,
                        "highlight": highlight,
                        "phrase": phrase,
                        "state": state,
                    },
                    article_search_params.ArticleSearchParams,
                ),
            ),
            cast_to=ArticleSearchResponse,
        )


class ArticlesWithRawResponse:
    def __init__(self, articles: Articles) -> None:
        self.create = to_raw_response_wrapper(
            articles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            articles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            articles.update,
        )
        self.list = to_raw_response_wrapper(
            articles.list,
        )
        self.remove = to_raw_response_wrapper(
            articles.remove,
        )
        self.search = to_raw_response_wrapper(
            articles.search,
        )


class AsyncArticlesWithRawResponse:
    def __init__(self, articles: AsyncArticles) -> None:
        self.create = async_to_raw_response_wrapper(
            articles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            articles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            articles.update,
        )
        self.list = async_to_raw_response_wrapper(
            articles.list,
        )
        self.remove = async_to_raw_response_wrapper(
            articles.remove,
        )
        self.search = async_to_raw_response_wrapper(
            articles.search,
        )
