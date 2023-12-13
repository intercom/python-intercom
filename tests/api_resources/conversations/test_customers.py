# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import Conversation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestCustomers:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        customer = client.conversations.customers.create(
            "string",
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        customer = client.conversations.customers.create(
            "string",
            admin_id="string",
            customer={
                "intercom_user_id": "654b71376abd01feb7c110af",
                "customer": {"intercom_user_id": "6329bd9ffe4e2e91dac76188"},
            },
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.conversations.customers.with_raw_response.create(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Conversation, customer, path=["response"])


class TestAsyncCustomers:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        customer = await client.conversations.customers.create(
            "string",
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        customer = await client.conversations.customers.create(
            "string",
            admin_id="string",
            customer={
                "intercom_user_id": "654b71376abd01feb7c110af",
                "customer": {"intercom_user_id": "6329bd9ffe4e2e91dac76188"},
            },
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.conversations.customers.with_raw_response.create(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Conversation, customer, path=["response"])
