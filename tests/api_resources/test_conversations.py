# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Optional

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import Ticket, Message, Conversation, PaginatedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestConversations:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        conversation = client.conversations.create(
            body="Hello there",
            from_={
                "type": "user",
                "id": "654b70ce6abd01feb7c11081",
            },
        )
        assert_matches_type(Message, conversation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.conversations.with_raw_response.create(
            body="Hello there",
            from_={
                "type": "user",
                "id": "654b70ce6abd01feb7c11081",
            },
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Message, conversation, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(PaginatedResponse, conversation, path=["response"])

    @parametrize
    def test_method_convert(self, client: Intercom) -> None:
        conversation = client.conversations.convert(
            0,
            ticket_type_id="108",
        )
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    def test_method_convert_with_all_params(self, client: Intercom) -> None:
        conversation = client.conversations.convert(
            0,
            ticket_type_id="108",
            attributes={
                "name": "example",
                "question": "Can I have some help?",
            },
        )
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    def test_raw_response_convert(self, client: Intercom) -> None:
        response = client.conversations.with_raw_response.convert(
            0,
            ticket_type_id="108",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])


class TestAsyncConversations:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.create(
            body="Hello there",
            from_={
                "type": "user",
                "id": "654b70ce6abd01feb7c11081",
            },
        )
        assert_matches_type(Message, conversation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.conversations.with_raw_response.create(
            body="Hello there",
            from_={
                "type": "user",
                "id": "654b70ce6abd01feb7c11081",
            },
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Message, conversation, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.retrieve(
            0,
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.retrieve(
            0,
            display_as="string",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.conversations.with_raw_response.retrieve(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.update(
            0,
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.update(
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
    async def test_raw_response_update(self, client: AsyncIntercom) -> None:
        response = await client.conversations.with_raw_response.update(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.list()
        assert_matches_type(PaginatedResponse, conversation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.list(
            per_page=0,
            starting_after="string",
        )
        assert_matches_type(PaginatedResponse, conversation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.conversations.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(PaginatedResponse, conversation, path=["response"])

    @parametrize
    async def test_method_convert(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.convert(
            0,
            ticket_type_id="108",
        )
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    async def test_method_convert_with_all_params(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.convert(
            0,
            ticket_type_id="108",
            attributes={
                "name": "example",
                "question": "Can I have some help?",
            },
        )
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    async def test_raw_response_convert(self, client: AsyncIntercom) -> None:
        response = await client.conversations.with_raw_response.convert(
            0,
            ticket_type_id="108",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Optional[Ticket], conversation, path=["response"])

    @parametrize
    async def test_method_redact_overload_1(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.redact(
            conversation_id="19894788788",
            conversation_part_id="19381789428",
            type="conversation_part",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_raw_response_redact_overload_1(self, client: AsyncIntercom) -> None:
        response = await client.conversations.with_raw_response.redact(
            conversation_id="19894788788",
            conversation_part_id="19381789428",
            type="conversation_part",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_method_redact_overload_2(self, client: AsyncIntercom) -> None:
        conversation = await client.conversations.redact(
            conversation_id="19894788788",
            source_id="19894781231",
            type="source",
        )
        assert_matches_type(Conversation, conversation, path=["response"])

    @parametrize
    async def test_raw_response_redact_overload_2(self, client: AsyncIntercom) -> None:
        response = await client.conversations.with_raw_response.redact(
            conversation_id="19894788788",
            source_id="19894781231",
            type="source",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(Conversation, conversation, path=["response"])
