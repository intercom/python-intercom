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


class TestReply:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_overload_1(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            email="string",
            intercom_user_id="string",
            user_id="string",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Intercom) -> None:
        response = client.conversations.reply.with_raw_response.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_overload_2(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            body="Hello there!",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Intercom) -> None:
        response = client.conversations.reply.with_raw_response.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(Conversation, reply, path=["response"])


class TestAsyncReply:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_overload_1(self, client: AsyncIntercom) -> None:
        reply = await client.conversations.reply.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, client: AsyncIntercom) -> None:
        reply = await client.conversations.reply.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            email="string",
            intercom_user_id="string",
            user_id="string",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, client: AsyncIntercom) -> None:
        response = await client.conversations.reply.with_raw_response.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncIntercom) -> None:
        reply = await client.conversations.reply.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, client: AsyncIntercom) -> None:
        reply = await client.conversations.reply.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            body="Hello there!",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, client: AsyncIntercom) -> None:
        response = await client.conversations.reply.with_raw_response.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(Conversation, reply, path=["response"])
