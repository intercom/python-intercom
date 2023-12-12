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


class TestParts:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_overload_1(self, client: Intercom) -> None:
        part = client.conversations.parts.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Intercom) -> None:
        part = client.conversations.parts.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
            body=" This conversation is now closed!",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Intercom) -> None:
        response = client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_method_create_overload_2(self, client: Intercom) -> None:
        part = client.conversations.parts.create(
            "string",
            admin_id="5017691",
            message_type="snoozed",
            snoozed_until=1673609604,
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Intercom) -> None:
        response = client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="5017691",
            message_type="snoozed",
            snoozed_until=1673609604,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_method_create_overload_3(self, client: Intercom) -> None:
        part = client.conversations.parts.create(
            "string",
            admin_id="5017690",
            message_type="open",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Intercom) -> None:
        response = client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="5017690",
            message_type="open",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_method_create_overload_4(self, client: Intercom) -> None:
        part = client.conversations.parts.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Intercom) -> None:
        part = client.conversations.parts.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
            body="Let me pass you over to one of my colleagues.",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Intercom) -> None:
        response = client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])


class TestAsyncParts:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_overload_1(self, client: AsyncIntercom) -> None:
        part = await client.conversations.parts.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, client: AsyncIntercom) -> None:
        part = await client.conversations.parts.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
            body=" This conversation is now closed!",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, client: AsyncIntercom) -> None:
        response = await client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncIntercom) -> None:
        part = await client.conversations.parts.create(
            "string",
            admin_id="5017691",
            message_type="snoozed",
            snoozed_until=1673609604,
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, client: AsyncIntercom) -> None:
        response = await client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="5017691",
            message_type="snoozed",
            snoozed_until=1673609604,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_method_create_overload_3(self, client: AsyncIntercom) -> None:
        part = await client.conversations.parts.create(
            "string",
            admin_id="5017690",
            message_type="open",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, client: AsyncIntercom) -> None:
        response = await client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="5017690",
            message_type="open",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_method_create_overload_4(self, client: AsyncIntercom) -> None:
        part = await client.conversations.parts.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, client: AsyncIntercom) -> None:
        part = await client.conversations.parts.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
            body="Let me pass you over to one of my colleagues.",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, client: AsyncIntercom) -> None:
        response = await client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])
