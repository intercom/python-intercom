# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Optional

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import TicketType, TicketTypeList
from intercom._client import Intercom, AsyncIntercom

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestTicketTypes:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        ticket_type = client.ticket_types.create(
            name="Customer Issue",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        ticket_type = client.ticket_types.create(
            name="Customer Issue",
            category="Customer",
            description="Customer Report Template",
            icon="🎟️",
            is_internal=False,
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.ticket_types.with_raw_response.create(
            name="Customer Issue",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        ticket_type = client.ticket_types.retrieve(
            "string",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.ticket_types.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_method_update(self, client: Intercom) -> None:
        ticket_type = client.ticket_types.update(
            "string",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Intercom) -> None:
        ticket_type = client.ticket_types.update(
            "string",
            archived=False,
            category="Customer",
            description="A bug has been occured",
            icon="🐞",
            is_internal=False,
            name="Bug Report 2",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.ticket_types.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        ticket_type = client.ticket_types.list()
        assert_matches_type(TicketTypeList, ticket_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.ticket_types.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(TicketTypeList, ticket_type, path=["response"])


class TestAsyncTicketTypes:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        ticket_type = await client.ticket_types.create(
            name="Customer Issue",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        ticket_type = await client.ticket_types.create(
            name="Customer Issue",
            category="Customer",
            description="Customer Report Template",
            icon="🎟️",
            is_internal=False,
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.ticket_types.with_raw_response.create(
            name="Customer Issue",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        ticket_type = await client.ticket_types.retrieve(
            "string",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.ticket_types.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncIntercom) -> None:
        ticket_type = await client.ticket_types.update(
            "string",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncIntercom) -> None:
        ticket_type = await client.ticket_types.update(
            "string",
            archived=False,
            category="Customer",
            description="A bug has been occured",
            icon="🐞",
            is_internal=False,
            name="Bug Report 2",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncIntercom) -> None:
        response = await client.ticket_types.with_raw_response.update(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        ticket_type = await client.ticket_types.list()
        assert_matches_type(TicketTypeList, ticket_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.ticket_types.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(TicketTypeList, ticket_type, path=["response"])
