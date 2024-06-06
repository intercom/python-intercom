# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types.shared import Conversation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReply:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            body="string",
            intercom_user_id="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            body="string",
            intercom_user_id="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Intercom) -> None:
        response = client.conversations.reply.with_raw_response.create(
            "123",
            body="string",
            intercom_user_id="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Intercom) -> None:
        with client.conversations.reply.with_streaming_response.create(
            "123",
            body="string",
            intercom_user_id="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            body="string",
            email="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            body="string",
            email="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Intercom) -> None:
        response = client.conversations.reply.with_raw_response.create(
            "123",
            body="string",
            email="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Intercom) -> None:
        with client.conversations.reply.with_streaming_response.create(
            "123",
            body="string",
            email="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
            user_id="string",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
            user_id="string",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Intercom) -> None:
        response = client.conversations.reply.with_raw_response.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
            user_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Intercom) -> None:
        with client.conversations.reply.with_streaming_response.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
            user_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_4(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Intercom) -> None:
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
    def test_raw_response_create_overload_4(self, client: Intercom) -> None:
        response = client.conversations.reply.with_raw_response.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: Intercom) -> None:
        with client.conversations.reply.with_streaming_response.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReply:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "123",
            body="string",
            intercom_user_id="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "123",
            body="string",
            intercom_user_id="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.reply.with_raw_response.create(
            "123",
            body="string",
            intercom_user_id="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.reply.with_streaming_response.create(
            "123",
            body="string",
            intercom_user_id="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "123",
            body="string",
            email="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "123",
            body="string",
            email="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.reply.with_raw_response.create(
            "123",
            body="string",
            email="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.reply.with_streaming_response.create(
            "123",
            body="string",
            email="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
            user_id="string",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
            user_id="string",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.reply.with_raw_response.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
            user_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.reply.with_streaming_response.create(
            "123",
            body="string",
            message_type="comment",
            type="user",
            user_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            body="Hello there!",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.reply.with_raw_response.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.reply.with_streaming_response.create(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True
