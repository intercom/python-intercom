# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import Company
from intercom.types.contacts import ContactAttachedCompanies

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestCompanies:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        company = client.contacts.companies.create(
            path_id="string",
            body_id="653a6a5235824d7a15ffe94a",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.contacts.companies.with_raw_response.create(
            path_id="string",
            body_id="653a6a5235824d7a15ffe94a",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        company = client.contacts.companies.list(
            "string",
        )
        assert_matches_type(ContactAttachedCompanies, company, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.contacts.companies.with_raw_response.list(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(ContactAttachedCompanies, company, path=["response"])

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        company = client.contacts.companies.delete(
            "string",
            contact_id="58a430d35458202d41b1e65b",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.contacts.companies.with_raw_response.delete(
            "string",
            contact_id="58a430d35458202d41b1e65b",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Company, company, path=["response"])


class TestAsyncCompanies:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        company = await client.contacts.companies.create(
            path_id="string",
            body_id="653a6a5235824d7a15ffe94a",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.contacts.companies.with_raw_response.create(
            path_id="string",
            body_id="653a6a5235824d7a15ffe94a",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        company = await client.contacts.companies.list(
            "string",
        )
        assert_matches_type(ContactAttachedCompanies, company, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.contacts.companies.with_raw_response.list(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(ContactAttachedCompanies, company, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncIntercom) -> None:
        company = await client.contacts.companies.delete(
            "string",
            contact_id="58a430d35458202d41b1e65b",
        )
        assert_matches_type(Company, company, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, client: AsyncIntercom) -> None:
        response = await client.contacts.companies.with_raw_response.delete(
            "string",
            contact_id="58a430d35458202d41b1e65b",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        company = response.parse()
        assert_matches_type(Company, company, path=["response"])
