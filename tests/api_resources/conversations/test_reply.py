# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_minus_intercom import Intercom, AsyncIntercom
from python_minus_intercom.types.shared import Conversation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReply:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Intercom) -> None:
        response = client.conversations.reply.with_raw_response.create(
            "string",
            body="string",
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
            "string",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.reply.with_raw_response.create(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    def test_method_create_overload_2(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Intercom) -> None:
        response = client.conversations.reply.with_raw_response.create(
            "string",
            body="string",
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
            "string",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.reply.with_raw_response.create(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    def test_method_create_overload_3(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Intercom) -> None:
        response = client.conversations.reply.with_raw_response.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Intercom) -> None:
        with client.conversations.reply.with_streaming_response.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_3(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.reply.with_raw_response.create(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    def test_method_create_overload_4(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "string",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Intercom) -> None:
        reply = client.conversations.reply.create(
            "string",
            admin_id="3156780",
            message_type="comment",
            type="admin",
            attachment_files=[
                {
                    "content_type": "application/json",
                    "data": "ewogICJ0ZXN0IjogMQp9",
                    "name": "test.json",
                },
                {
                    "content_type": "application/json",
                    "data": "ewogICJ0ZXN0IjogMQp9",
                    "name": "test.json",
                },
                {
                    "content_type": "application/json",
                    "data": "ewogICJ0ZXN0IjogMQp9",
                    "name": "test.json",
                },
            ],
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            body="Hello there!",
            created_at=1590000000,
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Intercom) -> None:
        response = client.conversations.reply.with_raw_response.create(
            "string",
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
            "string",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_4(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.reply.with_raw_response.create(
                "",
                admin_id="3156780",
                message_type="comment",
                type="admin",
            )


class TestAsyncReply:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.reply.with_raw_response.create(
            "string",
            body="string",
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
            "string",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.reply.with_raw_response.create(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.reply.with_raw_response.create(
            "string",
            body="string",
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
            "string",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.reply.with_raw_response.create(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.reply.with_raw_response.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.reply.with_streaming_response.create(
            "string",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.reply.with_raw_response.create(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "string",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncIntercom) -> None:
        reply = await async_client.conversations.reply.create(
            "string",
            admin_id="3156780",
            message_type="comment",
            type="admin",
            attachment_files=[
                {
                    "content_type": "application/json",
                    "data": "ewogICJ0ZXN0IjogMQp9",
                    "name": "test.json",
                },
                {
                    "content_type": "application/json",
                    "data": "ewogICJ0ZXN0IjogMQp9",
                    "name": "test.json",
                },
                {
                    "content_type": "application/json",
                    "data": "ewogICJ0ZXN0IjogMQp9",
                    "name": "test.json",
                },
            ],
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            body="Hello there!",
            created_at=1590000000,
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, reply, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.reply.with_raw_response.create(
            "string",
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
            "string",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(Conversation, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.reply.with_raw_response.create(
                "",
                admin_id="3156780",
                message_type="comment",
                type="admin",
            )
