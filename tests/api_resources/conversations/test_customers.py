# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types.shared import Conversation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        customer = client.conversations.customers.create(
            id="123",
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        customer = client.conversations.customers.create(
            id="123",
            admin_id="admin_id",
            customer={
                "intercom_user_id": "6657ae626abd0167d9419d6f",
                "customer": {"intercom_user_id": "6329bd9ffe4e2e91dac76188"},
            },
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.conversations.customers.with_raw_response.create(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.conversations.customers.with_streaming_response.create(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Conversation, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.customers.with_raw_response.create(
                id="",
            )

    @parametrize
    def test_method_delete(self, client: Intercom) -> None:
        customer = client.conversations.customers.delete(
            contact_id="123",
            conversation_id="123",
            admin_id="admin_id",
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Intercom) -> None:
        customer = client.conversations.customers.delete(
            contact_id="123",
            conversation_id="123",
            admin_id="admin_id",
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Intercom) -> None:
        response = client.conversations.customers.with_raw_response.delete(
            contact_id="123",
            conversation_id="123",
            admin_id="admin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Intercom) -> None:
        with client.conversations.customers.with_streaming_response.delete(
            contact_id="123",
            conversation_id="123",
            admin_id="admin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Conversation, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.conversations.customers.with_raw_response.delete(
                contact_id="123",
                conversation_id="",
                admin_id="admin_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.conversations.customers.with_raw_response.delete(
                contact_id="",
                conversation_id="123",
                admin_id="admin_id",
            )


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        customer = await async_client.conversations.customers.create(
            id="123",
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        customer = await async_client.conversations.customers.create(
            id="123",
            admin_id="admin_id",
            customer={
                "intercom_user_id": "6657ae626abd0167d9419d6f",
                "customer": {"intercom_user_id": "6329bd9ffe4e2e91dac76188"},
            },
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.customers.with_raw_response.create(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.customers.with_streaming_response.create(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Conversation, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.customers.with_raw_response.create(
                id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncIntercom) -> None:
        customer = await async_client.conversations.customers.delete(
            contact_id="123",
            conversation_id="123",
            admin_id="admin_id",
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncIntercom) -> None:
        customer = await async_client.conversations.customers.delete(
            contact_id="123",
            conversation_id="123",
            admin_id="admin_id",
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.customers.with_raw_response.delete(
            contact_id="123",
            conversation_id="123",
            admin_id="admin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(Conversation, customer, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.customers.with_streaming_response.delete(
            contact_id="123",
            conversation_id="123",
            admin_id="admin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Conversation, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.conversations.customers.with_raw_response.delete(
                contact_id="123",
                conversation_id="",
                admin_id="admin_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.conversations.customers.with_raw_response.delete(
                contact_id="",
                conversation_id="123",
                admin_id="admin_id",
            )
