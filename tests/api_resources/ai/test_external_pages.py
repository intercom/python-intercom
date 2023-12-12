# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.ai import ExternalPage, ExternalPagesList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestExternalPages:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        external_page = client.ai.external_pages.create(
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=12,
            title="Test",
            url="https://www.example.com",
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        external_page = client.ai.external_pages.create(
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=12,
            title="Test",
            url="https://www.example.com",
            external_id="abc1234",
            fin_availability=True,
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.ai.external_pages.with_raw_response.create(
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=12,
            title="Test",
            url="https://www.example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_page = response.parse()
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        external_page = client.ai.external_pages.retrieve(
            "string",
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.ai.external_pages.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_page = response.parse()
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        external_page = client.ai.external_pages.update(
            "string",
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=15,
            title="Test",
            url="https://www.example.com",
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        external_page = client.ai.external_pages.update(
            "string",
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=15,
            title="Test",
            url="https://www.example.com",
            external_id="5678",
            fin_availability=True,
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.ai.external_pages.with_raw_response.update(
            "string",
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=15,
            title="Test",
            url="https://www.example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_page = response.parse()
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        external_page = client.ai.external_pages.list()
        assert_matches_type(ExternalPagesList, external_page, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.ai.external_pages.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_page = response.parse()
        assert_matches_type(ExternalPagesList, external_page, path=["response"])

    @parametrize
    def test_method_remove_all(self, client: Intercom) -> None:
        external_page = client.ai.external_pages.remove_all(
            "string",
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    def test_raw_response_remove_all(self, client: Intercom) -> None:
        response = client.ai.external_pages.with_raw_response.remove_all(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_page = response.parse()
        assert_matches_type(ExternalPage, external_page, path=["response"])


class TestAsyncExternalPages:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        external_page = await client.ai.external_pages.create(
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=12,
            title="Test",
            url="https://www.example.com",
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        external_page = await client.ai.external_pages.create(
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=12,
            title="Test",
            url="https://www.example.com",
            external_id="abc1234",
            fin_availability=True,
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.ai.external_pages.with_raw_response.create(
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=12,
            title="Test",
            url="https://www.example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_page = response.parse()
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        external_page = await client.ai.external_pages.retrieve(
            "string",
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.ai.external_pages.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_page = response.parse()
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIntercom) -> None:
        external_page = await client.ai.external_pages.update(
            "string",
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=15,
            title="Test",
            url="https://www.example.com",
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIntercom) -> None:
        external_page = await client.ai.external_pages.update(
            "string",
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=15,
            title="Test",
            url="https://www.example.com",
            external_id="5678",
            fin_availability=True,
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncIntercom) -> None:
        response = await client.ai.external_pages.with_raw_response.update(
            "string",
            html="<html><body><h1>Test</h1></body></html>",
            locale="en",
            source_id=15,
            title="Test",
            url="https://www.example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_page = response.parse()
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        external_page = await client.ai.external_pages.list()
        assert_matches_type(ExternalPagesList, external_page, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.ai.external_pages.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_page = response.parse()
        assert_matches_type(ExternalPagesList, external_page, path=["response"])

    @parametrize
    async def test_method_remove_all(self, client: AsyncIntercom) -> None:
        external_page = await client.ai.external_pages.remove_all(
            "string",
        )
        assert_matches_type(ExternalPage, external_page, path=["response"])

    @parametrize
    async def test_raw_response_remove_all(self, client: AsyncIntercom) -> None:
        response = await client.ai.external_pages.with_raw_response.remove_all(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_page = response.parse()
        assert_matches_type(ExternalPage, external_page, path=["response"])
