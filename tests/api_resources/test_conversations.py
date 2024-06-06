# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import (
    ConversationList,
)
from intercom.types.shared import Ticket, Message, Conversation, PaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        conversation = client.conversations.create(
            body="Hello there",
            from_={
                "type": "user",
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        )
        assert_matches_type(Message, conversation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.conversations.with_raw_response.create(
            body="Hello there",
            from_={
                "type": "user",
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Message, conversation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.conversations.with_streaming_response.create(
            body="Hello there",
            from_={
                "type": "user",
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Message, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        conversation = client.conversations.retrieve(
            0,
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        conversation = client.conversations.retrieve(
            0,
            display_as="string",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.conversations.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.conversations.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        conversation = client.conversations.update(
            0,
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        conversation = client.conversations.update(
            0,
            display_as="string",
            custom_attributes={
                "issue_type": "Billing",
                "priority": "High",
            },
            read=True,
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.conversations.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Intercom) -> None:
        with client.conversations.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        conversation = client.conversations.list()
        assert_matches_type(PaginatedResponse, conversation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        conversation = client.conversations.list(
            per_page=0,
            starting_after="string",
        )
        assert_matches_type(PaginatedResponse, conversation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.conversations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(PaginatedResponse, conversation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.conversations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(PaginatedResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_convert(self, client: Intercom) -> None:
        conversation = client.conversations.convert(
            0,
            ticket_type_id="120",
        )
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    def test_method_convert_with_all_params(self, client: Intercom) -> None:
        conversation = client.conversations.convert(
            0,
            ticket_type_id="120",
            attributes={
                "_default_title_": "Found a bug",
                "_default_description_": "The button is not working",
            },
        )
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    def test_raw_response_convert(self, client: Intercom) -> None:
        response = client.conversations.with_raw_response.convert(
            0,
            ticket_type_id="120",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    def test_streaming_response_convert(self, client: Intercom) -> None:
        with client.conversations.with_streaming_response.convert(
            0,
            ticket_type_id="120",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Optional[Ticket], conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_redact_overload_1(self, client: Intercom) -> None:
        conversation = client.conversations.redact(
            conversation_id="19894788788",
            conversation_part_id="19381789428",
            type="conversation_part",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    def test_raw_response_redact_overload_1(self, client: Intercom) -> None:
        response = client.conversations.with_raw_response.redact(
            conversation_id="19894788788",
            conversation_part_id="19381789428",
            type="conversation_part",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    def test_streaming_response_redact_overload_1(self, client: Intercom) -> None:
        with client.conversations.with_streaming_response.redact(
            conversation_id="19894788788",
            conversation_part_id="19381789428",
            type="conversation_part",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_redact_overload_2(self, client: Intercom) -> None:
        conversation = client.conversations.redact(
            conversation_id="19894788788",
            source_id="19894781231",
            type="source",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    def test_raw_response_redact_overload_2(self, client: Intercom) -> None:
        response = client.conversations.with_raw_response.redact(
            conversation_id="19894788788",
            source_id="19894781231",
            type="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    def test_streaming_response_redact_overload_2(self, client: Intercom) -> None:
        with client.conversations.with_streaming_response.redact(
            conversation_id="19894788788",
            source_id="19894781231",
            type="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Intercom) -> None:
        conversation = client.conversations.search(
            query={},
        )
        assert_matches_type(ConversationList, conversation, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Intercom) -> None:
        conversation = client.conversations.search(
            query={
                "field": "created_at",
                "operator": "=",
                "value": "string",
            },
            pagination={
                "per_page": 5,
                "starting_after": "your-cursor-from-response",
            },
        )
        assert_matches_type(ConversationList, conversation, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Intercom) -> None:
        response = client.conversations.with_raw_response.search(
            query={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationList, conversation, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Intercom) -> None:
        with client.conversations.with_streaming_response.search(
            query={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationList, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConversations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.create(
            body="Hello there",
            from_={
                "type": "user",
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        )
        assert_matches_type(Message, conversation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.with_raw_response.create(
            body="Hello there",
            from_={
                "type": "user",
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Message, conversation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.with_streaming_response.create(
            body="Hello there",
            from_={
                "type": "user",
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Message, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.retrieve(
            0,
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.retrieve(
            0,
            display_as="string",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.update(
            0,
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.update(
            0,
            display_as="string",
            custom_attributes={
                "issue_type": "Billing",
                "priority": "High",
            },
            read=True,
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.list()
        assert_matches_type(PaginatedResponse, conversation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.list(
            per_page=0,
            starting_after="string",
        )
        assert_matches_type(PaginatedResponse, conversation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(PaginatedResponse, conversation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(PaginatedResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_convert(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.convert(
            0,
            ticket_type_id="120",
        )
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    async def test_method_convert_with_all_params(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.convert(
            0,
            ticket_type_id="120",
            attributes={
                "_default_title_": "Found a bug",
                "_default_description_": "The button is not working",
            },
        )
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    async def test_raw_response_convert(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.with_raw_response.convert(
            0,
            ticket_type_id="120",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    async def test_streaming_response_convert(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.with_streaming_response.convert(
            0,
            ticket_type_id="120",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Optional[Ticket], conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_redact_overload_1(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.redact(
            conversation_id="19894788788",
            conversation_part_id="19381789428",
            type="conversation_part",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_raw_response_redact_overload_1(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.with_raw_response.redact(
            conversation_id="19894788788",
            conversation_part_id="19381789428",
            type="conversation_part",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_streaming_response_redact_overload_1(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.with_streaming_response.redact(
            conversation_id="19894788788",
            conversation_part_id="19381789428",
            type="conversation_part",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_redact_overload_2(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.redact(
            conversation_id="19894788788",
            source_id="19894781231",
            type="source",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_raw_response_redact_overload_2(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.with_raw_response.redact(
            conversation_id="19894788788",
            source_id="19894781231",
            type="source",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_streaming_response_redact_overload_2(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.with_streaming_response.redact(
            conversation_id="19894788788",
            source_id="19894781231",
            type="source",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(Conversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.search(
            query={},
        )
        assert_matches_type(ConversationList, conversation, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncIntercom) -> None:
        conversation = await async_client.conversations.search(
            query={
                "field": "created_at",
                "operator": "=",
                "value": "string",
            },
            pagination={
                "per_page": 5,
                "starting_after": "your-cursor-from-response",
            },
        )
        assert_matches_type(ConversationList, conversation, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.with_raw_response.search(
            query={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationList, conversation, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.with_streaming_response.search(
            query={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationList, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True
