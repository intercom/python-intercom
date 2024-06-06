# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import (
    TicketList,
    TicketReply,
)
from intercom.types.shared import Ticket

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTickets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        ticket = client.tickets.create(
            contacts=[{"id": "6657af026abd0167d9419def"}],
            ticket_type_id="string",
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        ticket = client.tickets.create(
            contacts=[{"id": "6657af026abd0167d9419def"}],
            ticket_type_id="string",
            company_id="1234",
            created_at=1590000000,
            ticket_attributes={
                "_default_title_": "example",
                "_default_description_": "there is a problem",
            },
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.create(
            contacts=[{"id": "6657af026abd0167d9419def"}],
            ticket_type_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.tickets.with_streaming_response.create(
            contacts=[{"id": "6657af026abd0167d9419def"}],
            ticket_type_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(Optional[Ticket], ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            created_at=1590000000,
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_streaming_response_reply_overload_1(self, client: Intercom) -> None:
        with client.tickets.with_streaming_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(TicketReply, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reply_overload_1(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tickets.with_raw_response.reply(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    def test_method_reply_overload_2(self, client: Intercom) -> None:
        ticket = client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_method_reply_with_all_params_overload_2(self, client: Intercom) -> None:
        ticket = client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_raw_response_reply_overload_2(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_streaming_response_reply_overload_2(self, client: Intercom) -> None:
        with client.tickets.with_streaming_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(TicketReply, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reply_overload_2(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tickets.with_raw_response.reply(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    def test_method_reply_overload_3(self, client: Intercom) -> None:
        ticket = client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_method_reply_with_all_params_overload_3(self, client: Intercom) -> None:
        ticket = client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_raw_response_reply_overload_3(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_streaming_response_reply_overload_3(self, client: Intercom) -> None:
        with client.tickets.with_streaming_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(TicketReply, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reply_overload_3(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tickets.with_raw_response.reply(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    def test_method_reply_overload_4(self, client: Intercom) -> None:
        ticket = client.tickets.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_method_reply_with_all_params_overload_4(self, client: Intercom) -> None:
        ticket = client.tickets.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            body="Hello there!",
            created_at=1590000000,
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
    def test_raw_response_reply_overload_4(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    def test_streaming_response_reply_overload_4(self, client: Intercom) -> None:
        with client.tickets.with_streaming_response.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(TicketReply, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reply_overload_4(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tickets.with_raw_response.reply(
                "",
                admin_id="3156780",
                message_type="comment",
                type="admin",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_by_id(self, client: Intercom) -> None:
        with client.tickets.with_streaming_response.retrieve_by_id(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(Optional[Ticket], ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_by_id(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tickets.with_raw_response.retrieve_by_id(
                "",
            )

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
                "field": "created_at",
                "operator": "=",
                "value": "string",
            },
            pagination={
                "per_page": 5,
                "starting_after": "your-cursor-from-response",
            },
        )
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.search(
            query={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Intercom) -> None:
        with client.tickets.with_streaming_response.search(
            query={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(TicketList, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

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
                "admin_id": "991268839",
                "assignee_id": "991268841",
            },
            is_shared=True,
            open=True,
            snoozed_until=1673609604,
            state="in_progress",
            ticket_attributes={
                "_default_title_": "example",
                "_default_description_": "there is a problem",
            },
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_raw_response_update_by_id(self, client: Intercom) -> None:
        response = client.tickets.with_raw_response.update_by_id(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    def test_streaming_response_update_by_id(self, client: Intercom) -> None:
        with client.tickets.with_streaming_response.update_by_id(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(Optional[Ticket], ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_by_id(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tickets.with_raw_response.update_by_id(
                "",
            )


class TestAsyncTickets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.create(
            contacts=[{"id": "6657af026abd0167d9419def"}],
            ticket_type_id="string",
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.create(
            contacts=[{"id": "6657af026abd0167d9419def"}],
            ticket_type_id="string",
            company_id="1234",
            created_at=1590000000,
            ticket_attributes={
                "_default_title_": "example",
                "_default_description_": "there is a problem",
            },
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tickets.with_raw_response.create(
            contacts=[{"id": "6657af026abd0167d9419def"}],
            ticket_type_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.tickets.with_streaming_response.create(
            contacts=[{"id": "6657af026abd0167d9419def"}],
            ticket_type_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(Optional[Ticket], ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reply_overload_1(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_method_reply_with_all_params_overload_1(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_raw_response_reply_overload_1(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tickets.with_raw_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_streaming_response_reply_overload_1(self, async_client: AsyncIntercom) -> None:
        async with async_client.tickets.with_streaming_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(TicketReply, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reply_overload_1(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tickets.with_raw_response.reply(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    async def test_method_reply_overload_2(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_method_reply_with_all_params_overload_2(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_raw_response_reply_overload_2(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tickets.with_raw_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_streaming_response_reply_overload_2(self, async_client: AsyncIntercom) -> None:
        async with async_client.tickets.with_streaming_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(TicketReply, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reply_overload_2(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tickets.with_raw_response.reply(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    async def test_method_reply_overload_3(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_method_reply_with_all_params_overload_3(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            created_at=1590000000,
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_raw_response_reply_overload_3(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tickets.with_raw_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_streaming_response_reply_overload_3(self, async_client: AsyncIntercom) -> None:
        async with async_client.tickets.with_streaming_response.reply(
            "123",
            body="string",
            message_type="comment",
            type="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(TicketReply, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reply_overload_3(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tickets.with_raw_response.reply(
                "",
                body="string",
                message_type="comment",
                type="user",
            )

    @parametrize
    async def test_method_reply_overload_4(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_method_reply_with_all_params_overload_4(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
            attachment_urls=["https://example.com", "https://example.com", "https://example.com"],
            body="Hello there!",
            created_at=1590000000,
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
    async def test_raw_response_reply_overload_4(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tickets.with_raw_response.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(TicketReply, ticket, path=["response"])

    @parametrize
    async def test_streaming_response_reply_overload_4(self, async_client: AsyncIntercom) -> None:
        async with async_client.tickets.with_streaming_response.reply(
            "123",
            admin_id="3156780",
            message_type="comment",
            type="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(TicketReply, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reply_overload_4(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tickets.with_raw_response.reply(
                "",
                admin_id="3156780",
                message_type="comment",
                type="admin",
            )

    @parametrize
    async def test_method_retrieve_by_id(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.retrieve_by_id(
            "string",
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_by_id(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tickets.with_raw_response.retrieve_by_id(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_by_id(self, async_client: AsyncIntercom) -> None:
        async with async_client.tickets.with_streaming_response.retrieve_by_id(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(Optional[Ticket], ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_by_id(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tickets.with_raw_response.retrieve_by_id(
                "",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.search(
            query={},
        )
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.search(
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
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tickets.with_raw_response.search(
            query={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(TicketList, ticket, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncIntercom) -> None:
        async with async_client.tickets.with_streaming_response.search(
            query={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(TicketList, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_by_id(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.update_by_id(
            "string",
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_method_update_by_id_with_all_params(self, async_client: AsyncIntercom) -> None:
        ticket = await async_client.tickets.update_by_id(
            "string",
            assignment={
                "admin_id": "991268839",
                "assignee_id": "991268841",
            },
            is_shared=True,
            open=True,
            snoozed_until=1673609604,
            state="in_progress",
            ticket_attributes={
                "_default_title_": "example",
                "_default_description_": "there is a problem",
            },
        )
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_raw_response_update_by_id(self, async_client: AsyncIntercom) -> None:
        response = await async_client.tickets.with_raw_response.update_by_id(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(Optional[Ticket], ticket, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_id(self, async_client: AsyncIntercom) -> None:
        async with async_client.tickets.with_streaming_response.update_by_id(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(Optional[Ticket], ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_by_id(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tickets.with_raw_response.update_by_id(
                "",
            )
