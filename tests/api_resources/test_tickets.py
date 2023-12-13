# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Optional

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import TicketList, TicketReply
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import Ticket

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestTickets:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        ticket = client.tickets.create(
            contacts=[{"id": "654b84736abd01feb7c111a1"}],
            ticket_type_id="string",
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        ticket = client.tickets.create(
            contacts=[{"id": "654b84736abd01feb7c111a1"}],
            ticket_type_id="string",
            ticket_attributes={
                "title": "example",
                "description": "there is a problem",
            },
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.create(
            contacts=[{"id": "654b84736abd01feb7c111a1"}],
            ticket_type_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_method_reply_overload_1(self, client: Intercom) -> None:
        ticket = client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_method_reply_with_all_params_overload_1(self, client: Intercom) -> None:
        ticket = client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            email="string",
            intercom_user_id="string",
            user_id="string",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_raw_response_reply_overload_1(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_method_reply_overload_2(self, client: Intercom) -> None:
        ticket = client.tickets.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_method_reply_with_all_params_overload_2(self, client: Intercom) -> None:
        ticket = client.tickets.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            body="Hello there!",
            reply_options=[
                {
                    "text": "string",
                    "uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "text": "string",
                    "uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "text": "string",
                    "uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
            ],
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_raw_response_reply_overload_2(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_method_retrieve_by_id(self, client: Intercom) -> None:
        ticket = client.tickets.retrieve_by_id(
            "string",
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_raw_response_retrieve_by_id(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.retrieve_by_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_method_search(self, client: Intercom) -> None:
        ticket = client.tickets.search(
            query={},
        )
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Intercom) -> None:
        ticket = client.tickets.search(
            query={
                "field": "custom_attributes.social_network",
                "operator": "=",
                "value": "string",
            },
            pagination={
                "page": 2,
                "starting_after": "1HaSB+xrOyyMXAkS/c1RteCL7BzOzTvYjmjakgTergIH31eoe2v4/sbLsJWP\nIncfQLD3ouPkZlCwJ86F\n",
            },
        )
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.search(
            query={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    def test_method_update_by_id(self, client: Intercom) -> None:
        ticket = client.tickets.update_by_id(
            "string",
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_method_update_by_id_with_all_params(self, client: Intercom) -> None:
        ticket = client.tickets.update_by_id(
            "string",
            assignment={
                "admin_id": "991269042",
                "assignee_id": "991269044",
            },
            is_shared=True,
            open=True,
            snoozed_until=1673609604,
            state="in_progress",
            ticket_attributes={
                "title": "example",
                "description": "there is a problem",
            },
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_raw_response_update_by_id(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.update_by_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])


class TestAsyncTickets:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.create(
            contacts=[{"id": "654b84736abd01feb7c111a1"}],
            ticket_type_id="string",
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.create(
            contacts=[{"id": "654b84736abd01feb7c111a1"}],
            ticket_type_id="string",
            ticket_attributes={
                "title": "example",
                "description": "there is a problem",
            },
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.tickets.with_raw_response.create(
            contacts=[{"id": "654b84736abd01feb7c111a1"}],
            ticket_type_id="string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_method_reply_overload_1(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_method_reply_with_all_params_overload_1(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            email="string",
            intercom_user_id="string",
            user_id="string",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_raw_response_reply_overload_1(self, client: AsyncIntercom) -> None:
        response = await client.tickets.with_raw_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_method_reply_overload_2(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_method_reply_with_all_params_overload_2(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            body="Hello there!",
            reply_options=[
                {
                    "text": "string",
                    "uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "text": "string",
                    "uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
                {
                    "text": "string",
                    "uuid": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                },
            ],
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_raw_response_reply_overload_2(self, client: AsyncIntercom) -> None:
        response = await client.tickets.with_raw_response.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_method_retrieve_by_id(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.retrieve_by_id(
            "string",
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_by_id(self, client: AsyncIntercom) -> None:
        response = await client.tickets.with_raw_response.retrieve_by_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_method_search(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.search(
            query={},
        )
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.search(
            query={
                "field": "custom_attributes.social_network",
                "operator": "=",
                "value": "string",
            },
            pagination={
                "page": 2,
                "starting_after": "1HaSB+xrOyyMXAkS/c1RteCL7BzOzTvYjmjakgTergIH31eoe2v4/sbLsJWP\nIncfQLD3ouPkZlCwJ86F\n",
            },
        )
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    async def test_raw_response_search(self, client: AsyncIntercom) -> None:
        response = await client.tickets.with_raw_response.search(
            query={},
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    async def test_method_update_by_id(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.update_by_id(
            "string",
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_method_update_by_id_with_all_params(self, client: AsyncIntercom) -> None:
        ticket = await client.tickets.update_by_id(
            "string",
            assignment={
                "admin_id": "991269042",
                "assignee_id": "991269044",
            },
            is_shared=True,
            open=True,
            snoozed_until=1673609604,
            state="in_progress",
            ticket_attributes={
                "title": "example",
                "description": "there is a problem",
            },
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_raw_response_update_by_id(self, client: AsyncIntercom) -> None:
        response = await client.tickets.with_raw_response.update_by_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])
