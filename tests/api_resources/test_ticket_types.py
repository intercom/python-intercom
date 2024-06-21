# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types import TicketType, TicketTypeList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTicketTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            intercom_version="2.11",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.ticket_types.with_raw_response.create(
            name="Customer Issue",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.ticket_types.with_streaming_response.create(
            name="Customer Issue",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket_type = response.parse()
            assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        ticket_type = client.ticket_types.retrieve(
            "string",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Intercom) -> None:
        ticket_type = client.ticket_types.retrieve(
            "string",
            intercom_version="2.11",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.ticket_types.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Intercom) -> None:
        with client.ticket_types.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket_type = response.parse()
            assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ticket_types.with_raw_response.retrieve(
                "",
            )

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
            intercom_version="2.11",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Intercom) -> None:
        response = client.ticket_types.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Intercom) -> None:
        with client.ticket_types.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket_type = response.parse()
            assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ticket_types.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        ticket_type = client.ticket_types.list()
        assert_matches_type(TicketTypeList, ticket_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Intercom) -> None:
        ticket_type = client.ticket_types.list(
            intercom_version="2.11",
        )
        assert_matches_type(TicketTypeList, ticket_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.ticket_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = response.parse()
        assert_matches_type(TicketTypeList, ticket_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Intercom) -> None:
        with client.ticket_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket_type = response.parse()
            assert_matches_type(TicketTypeList, ticket_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTicketTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        ticket_type = await async_client.ticket_types.create(
            name="Customer Issue",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        ticket_type = await async_client.ticket_types.create(
            name="Customer Issue",
            category="Customer",
            description="Customer Report Template",
            icon="🎟️",
            is_internal=False,
            intercom_version="2.11",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.ticket_types.with_raw_response.create(
            name="Customer Issue",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = await response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.ticket_types.with_streaming_response.create(
            name="Customer Issue",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket_type = await response.parse()
            assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncIntercom) -> None:
        ticket_type = await async_client.ticket_types.retrieve(
            "string",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncIntercom) -> None:
        ticket_type = await async_client.ticket_types.retrieve(
            "string",
            intercom_version="2.11",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncIntercom) -> None:
        response = await async_client.ticket_types.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = await response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncIntercom) -> None:
        async with async_client.ticket_types.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket_type = await response.parse()
            assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ticket_types.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncIntercom) -> None:
        ticket_type = await async_client.ticket_types.update(
            "string",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncIntercom) -> None:
        ticket_type = await async_client.ticket_types.update(
            "string",
            archived=False,
            category="Customer",
            description="A bug has been occured",
            icon="🐞",
            is_internal=False,
            name="Bug Report 2",
            intercom_version="2.11",
        )
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncIntercom) -> None:
        response = await async_client.ticket_types.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = await response.parse()
        assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncIntercom) -> None:
        async with async_client.ticket_types.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket_type = await response.parse()
            assert_matches_type(Optional[TicketType], ticket_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ticket_types.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncIntercom) -> None:
        ticket_type = await async_client.ticket_types.list()
        assert_matches_type(TicketTypeList, ticket_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncIntercom) -> None:
        ticket_type = await async_client.ticket_types.list(
            intercom_version="2.11",
        )
        assert_matches_type(TicketTypeList, ticket_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncIntercom) -> None:
        response = await async_client.ticket_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket_type = await response.parse()
        assert_matches_type(TicketTypeList, ticket_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncIntercom) -> None:
        async with async_client.ticket_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket_type = await response.parse()
            assert_matches_type(TicketTypeList, ticket_type, path=["response"])

        assert cast(Any, response.is_closed) is True
