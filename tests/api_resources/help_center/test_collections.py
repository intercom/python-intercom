# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.help_center import (
    Collection,
    CollectionList,
    DeletedCollectionObject,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestCollections:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        collection = client.help_center.collections.create(
            name="Thanks for everything",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        collection = client.help_center.collections.create(
            name="Thanks for everything",
            description="English description",
            help_center_id=0,
            parent_id="6871118",
            translated_content={
                "type": "group_translated_content",
                "ar": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bg": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ca": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "cs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "da": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "de": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "el": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "en": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "es": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "et": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "he": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hu": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "id": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "it": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ja": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ko": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "mn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nb": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ro": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ru": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "tr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "vi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt_br": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_cn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_tw": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
            },
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.help_center.collections.with_raw_response.create(
            name="Thanks for everything",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        collection = client.help_center.collections.retrieve(
            0,
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.help_center.collections.with_raw_response.retrieve(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        collection = client.help_center.collections.update(
            0,
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        collection = client.help_center.collections.update(
            0,
            description="English description",
            name="Update collection name",
            parent_id="6871118",
            translated_content={
                "type": "group_translated_content",
                "ar": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bg": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ca": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "cs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "da": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "de": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "el": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "en": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "es": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "et": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "he": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hu": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "id": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "it": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ja": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ko": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "mn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nb": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ro": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ru": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "tr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "vi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt_br": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_cn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_tw": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
            },
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.help_center.collections.with_raw_response.update(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        collection = client.help_center.collections.list()
        assert_matches_type(CollectionList, collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.help_center.collections.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionList, collection, path=["response"])

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        collection = client.help_center.collections.delete(
            0,
        )
        assert_matches_type(DeletedCollectionObject, collection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.help_center.collections.with_raw_response.delete(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(DeletedCollectionObject, collection, path=["response"])


class TestAsyncCollections:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        collection = await client.help_center.collections.create(
            name="Thanks for everything",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        collection = await client.help_center.collections.create(
            name="Thanks for everything",
            description="English description",
            help_center_id=0,
            parent_id="6871118",
            translated_content={
                "type": "group_translated_content",
                "ar": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bg": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ca": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "cs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "da": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "de": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "el": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "en": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "es": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "et": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "he": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hu": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "id": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "it": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ja": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ko": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "mn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nb": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ro": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ru": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "tr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "vi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt_br": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_cn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_tw": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
            },
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.help_center.collections.with_raw_response.create(
            name="Thanks for everything",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        collection = await client.help_center.collections.retrieve(
            0,
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.help_center.collections.with_raw_response.retrieve(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIntercom) -> None:
        collection = await client.help_center.collections.update(
            0,
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIntercom) -> None:
        collection = await client.help_center.collections.update(
            0,
            description="English description",
            name="Update collection name",
            parent_id="6871118",
            translated_content={
                "type": "group_translated_content",
                "ar": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bg": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "bs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ca": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "cs": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "da": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "de": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "el": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "en": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "es": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "et": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "fr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "he": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "hu": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "id": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "it": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ja": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ko": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "lv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "mn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nb": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "nl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ro": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "ru": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sl": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "sv": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "tr": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "vi": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "pt_br": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_cn": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
                "zh_tw": {
                    "type": "group_content",
                    "name": "Collection name",
                    "description": " Collection description",
                },
            },
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncIntercom) -> None:
        response = await client.help_center.collections.with_raw_response.update(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        collection = await client.help_center.collections.list()
        assert_matches_type(CollectionList, collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.help_center.collections.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionList, collection, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncIntercom) -> None:
        collection = await client.help_center.collections.delete(
            0,
        )
        assert_matches_type(DeletedCollectionObject, collection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncIntercom) -> None:
        response = await client.help_center.collections.with_raw_response.delete(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(DeletedCollectionObject, collection, path=["response"])
