# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import (
    Article,
    ArticleList,
    DeletedArticleObject,
    ArticleSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArticles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        article = client.articles.create(
            author_id=991268363,
            title="Thanks for everything",
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        article = client.articles.create(
            author_id=991268363,
            title="Thanks for everything",
            body="Body of the Article",
            description="Description of the Article",
            parent_id=290,
            parent_type="collection",
            state="published",
            translated_content={
                "type": "article_translated_content",
                "ar": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "bg": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "bs": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ca": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "cs": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "da": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "de": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "el": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "en": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "es": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "et": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "fi": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "fr": {
                    "type": "article_content",
                    "title": "Merci pour tout",
                    "description": "Description de l'article",
                    "body": "Corps de l'article",
                    "author_id": 991268363,
                    "state": "published",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "he": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "hr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "hu": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "id": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "it": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ja": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ko": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "lt": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "lv": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "mn": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "nb": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "nl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pt": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ro": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ru": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sv": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "tr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "vi": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pt_br": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "zh_cn": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "zh_tw": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
            },
            intercom_version="2.11",
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.articles.with_raw_response.create(
            author_id=991268363,
            title="Thanks for everything",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.articles.with_streaming_response.create(
            author_id=991268363,
            title="Thanks for everything",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(Article, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        article = client.articles.retrieve(
            0,
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        article = client.articles.retrieve(
            0,
            intercom_version="2.11",
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.articles.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.articles.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(Article, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        article = client.articles.update(
            0,
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        article = client.articles.update(
            0,
            author_id=1295,
            body="<p>New gifts in store for the jolly season</p>",
            description="Description of the Article",
            parent_id="18",
            parent_type="collection",
            state="draft",
            title="Christmas is here!",
            translated_content={
                "type": "article_translated_content",
                "ar": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "bg": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "bs": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ca": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "cs": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "da": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "de": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "el": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "en": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "es": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "et": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "fi": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "fr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "he": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "hr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "hu": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "id": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "it": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ja": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ko": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "lt": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "lv": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "mn": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "nb": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "nl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pt": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ro": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ru": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sv": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "tr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "vi": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pt_br": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "zh_cn": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "zh_tw": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
            },
            intercom_version="2.11",
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.articles.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Intercom) -> None:
        with client.articles.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(Article, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        article = client.articles.list()
        assert_matches_type(ArticleList, article, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        article = client.articles.list(
            intercom_version="2.11",
        )
        assert_matches_type(ArticleList, article, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.articles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(ArticleList, article, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.articles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(ArticleList, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove(self, client: Intercom) -> None:
        article = client.articles.remove(
            0,
        )
        assert_matches_type(DeletedArticleObject, article, path=["response"])

    @parametrize
    def test_method_remove_with_all_params(self, client: Intercom) -> None:
        article = client.articles.remove(
            0,
            intercom_version="2.11",
        )
        assert_matches_type(DeletedArticleObject, article, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Intercom) -> None:
        response = client.articles.with_raw_response.remove(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(DeletedArticleObject, article, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Intercom) -> None:
        with client.articles.with_streaming_response.remove(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(DeletedArticleObject, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Intercom) -> None:
        article = client.articles.search()
        assert_matches_type(ArticleSearchResponse, article, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Intercom) -> None:
        article = client.articles.search(
            help_center_id=0,
            highlight=True,
            phrase="string",
            state="string",
            intercom_version="2.11",
        )
        assert_matches_type(ArticleSearchResponse, article, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Intercom) -> None:
        response = client.articles.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(ArticleSearchResponse, article, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Intercom) -> None:
        with client.articles.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(ArticleSearchResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncArticles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.create(
            author_id=991268363,
            title="Thanks for everything",
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.create(
            author_id=991268363,
            title="Thanks for everything",
            body="Body of the Article",
            description="Description of the Article",
            parent_id=290,
            parent_type="collection",
            state="published",
            translated_content={
                "type": "article_translated_content",
                "ar": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "bg": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "bs": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ca": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "cs": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "da": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "de": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "el": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "en": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "es": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "et": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "fi": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "fr": {
                    "type": "article_content",
                    "title": "Merci pour tout",
                    "description": "Description de l'article",
                    "body": "Corps de l'article",
                    "author_id": 991268363,
                    "state": "published",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "he": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "hr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "hu": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "id": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "it": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ja": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ko": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "lt": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "lv": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "mn": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "nb": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "nl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pt": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ro": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ru": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sv": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "tr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "vi": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pt_br": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "zh_cn": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "zh_tw": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
            },
            intercom_version="2.11",
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.articles.with_raw_response.create(
            author_id=991268363,
            title="Thanks for everything",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.articles.with_streaming_response.create(
            author_id=991268363,
            title="Thanks for everything",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(Article, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.retrieve(
            0,
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.retrieve(
            0,
            intercom_version="2.11",
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.articles.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.articles.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(Article, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.update(
            0,
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.update(
            0,
            author_id=1295,
            body="<p>New gifts in store for the jolly season</p>",
            description="Description of the Article",
            parent_id="18",
            parent_type="collection",
            state="draft",
            title="Christmas is here!",
            translated_content={
                "type": "article_translated_content",
                "ar": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "bg": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "bs": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ca": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "cs": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "da": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "de": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "el": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "en": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "es": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "et": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "fi": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "fr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "he": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "hr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "hu": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "id": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "it": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ja": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ko": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "lt": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "lv": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "mn": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "nb": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "nl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pt": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ro": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "ru": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sl": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "sv": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "tr": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "vi": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "pt_br": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "zh_cn": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
                "zh_tw": {
                    "type": "article_content",
                    "title": "How to create a new article",
                    "description": "This article will show you how to create a new article.",
                    "body": "This is the body of the article.",
                    "author_id": 0,
                    "state": "draft",
                    "created_at": 1663597223,
                    "updated_at": 1663597260,
                    "url": "http://intercom.test/help/en/articles/3-default-language",
                },
            },
            intercom_version="2.11",
        )
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIntercom) -> None:
        response = await async_client.articles.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(Article, article, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIntercom) -> None:
        async with async_client.articles.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(Article, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.list()
        assert_matches_type(ArticleList, article, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.list(
            intercom_version="2.11",
        )
        assert_matches_type(ArticleList, article, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.articles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(ArticleList, article, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.articles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(ArticleList, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.remove(
            0,
        )
        assert_matches_type(DeletedArticleObject, article, path=["response"])

    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.remove(
            0,
            intercom_version="2.11",
        )
        assert_matches_type(DeletedArticleObject, article, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncIntercom) -> None:
        response = await async_client.articles.with_raw_response.remove(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(DeletedArticleObject, article, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncIntercom) -> None:
        async with async_client.articles.with_streaming_response.remove(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(DeletedArticleObject, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.search()
        assert_matches_type(ArticleSearchResponse, article, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncIntercom) -> None:
        article = await async_client.articles.search(
            help_center_id=0,
            highlight=True,
            phrase="string",
            state="string",
            intercom_version="2.11",
        )
        assert_matches_type(ArticleSearchResponse, article, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncIntercom) -> None:
        response = await async_client.articles.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(ArticleSearchResponse, article, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncIntercom) -> None:
        async with async_client.articles.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(ArticleSearchResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True
