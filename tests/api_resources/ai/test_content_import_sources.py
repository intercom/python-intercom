# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.ai import ContentImportSource, ContentImportSourcesList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestContentImportSources:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        content_import_source = client.ai.content_import_sources.create(
            sync_behavior="api",
            url="https://www.example.com",
        )
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        content_import_source = client.ai.content_import_sources.create(
            sync_behavior="api",
            url="https://www.example.com",
            status="active",
        )
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.ai.content_import_sources.with_raw_response.create(
            sync_behavior="api",
            url="https://www.example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_import_source = response.parse()
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        content_import_source = client.ai.content_import_sources.retrieve(
            "string",
        )
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.ai.content_import_sources.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_import_source = response.parse()
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        content_import_source = client.ai.content_import_sources.update(
            "string",
            sync_behavior="api",
            url="https://www.example.com",
        )
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        content_import_source = client.ai.content_import_sources.update(
            "string",
            sync_behavior="api",
            url="https://www.example.com",
            status="active",
        )
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.ai.content_import_sources.with_raw_response.update(
            "string",
            sync_behavior="api",
            url="https://www.example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_import_source = response.parse()
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        content_import_source = client.ai.content_import_sources.list()
        assert_matches_type(ContentImportSourcesList, content_import_source, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.ai.content_import_sources.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_import_source = response.parse()
        assert_matches_type(ContentImportSourcesList, content_import_source, path=["response"])

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        content_import_source = client.ai.content_import_sources.delete(
            "string",
        )
        assert content_import_source is None

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.ai.content_import_sources.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_import_source = response.parse()
        assert content_import_source is None


class TestAsyncContentImportSources:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        content_import_source = await client.ai.content_import_sources.create(
            sync_behavior="api",
            url="https://www.example.com",
        )
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        content_import_source = await client.ai.content_import_sources.create(
            sync_behavior="api",
            url="https://www.example.com",
            status="active",
        )
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.ai.content_import_sources.with_raw_response.create(
            sync_behavior="api",
            url="https://www.example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_import_source = response.parse()
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        content_import_source = await client.ai.content_import_sources.retrieve(
            "string",
        )
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.ai.content_import_sources.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_import_source = response.parse()
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIntercom) -> None:
        content_import_source = await client.ai.content_import_sources.update(
            "string",
            sync_behavior="api",
            url="https://www.example.com",
        )
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIntercom) -> None:
        content_import_source = await client.ai.content_import_sources.update(
            "string",
            sync_behavior="api",
            url="https://www.example.com",
            status="active",
        )
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncIntercom) -> None:
        response = await client.ai.content_import_sources.with_raw_response.update(
            "string",
            sync_behavior="api",
            url="https://www.example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_import_source = response.parse()
        assert_matches_type(ContentImportSource, content_import_source, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        content_import_source = await client.ai.content_import_sources.list()
        assert_matches_type(ContentImportSourcesList, content_import_source, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.ai.content_import_sources.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_import_source = response.parse()
        assert_matches_type(ContentImportSourcesList, content_import_source, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncIntercom) -> None:
        content_import_source = await client.ai.content_import_sources.delete(
            "string",
        )
        assert content_import_source is None

    @parametrize
    async def test_raw_response_delete(self, client: AsyncIntercom) -> None:
        response = await client.ai.content_import_sources.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_import_source = response.parse()
        assert content_import_source is None
