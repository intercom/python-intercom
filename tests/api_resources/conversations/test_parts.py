# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types.shared import Conversation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Intercom) -> None:
        with client.conversations.parts.with_streaming_response.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Conversation, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.parts.with_raw_response.create(
                "",
                admin_id="12345",
                message_type="close",
                type="admin",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Intercom) -> None:
        with client.conversations.parts.with_streaming_response.create(
            "string",
            admin_id="5017691",
            message_type="snoozed",
            snoozed_until=1673609604,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Conversation, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.parts.with_raw_response.create(
                "",
                admin_id="5017691",
                message_type="snoozed",
                snoozed_until=1673609604,
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Intercom) -> None:
        with client.conversations.parts.with_streaming_response.create(
            "string",
            admin_id="5017690",
            message_type="open",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Conversation, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_3(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.parts.with_raw_response.create(
                "",
                admin_id="5017690",
                message_type="open",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: Intercom) -> None:
        with client.conversations.parts.with_streaming_response.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Conversation, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_4(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.parts.with_raw_response.create(
                "",
                admin_id="12345",
                assignee_id="4324241",
                message_type="assignment",
                type="admin",
            )


class TestAsyncParts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncIntercom) -> None:
        part = await async_client.conversations.parts.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncIntercom) -> None:
        part = await async_client.conversations.parts.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
            body=" This conversation is now closed!",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.parts.with_streaming_response.create(
            "string",
            admin_id="12345",
            message_type="close",
            type="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Conversation, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.parts.with_raw_response.create(
                "",
                admin_id="12345",
                message_type="close",
                type="admin",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncIntercom) -> None:
        part = await async_client.conversations.parts.create(
            "string",
            admin_id="5017691",
            message_type="snoozed",
            snoozed_until=1673609604,
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="5017691",
            message_type="snoozed",
            snoozed_until=1673609604,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.parts.with_streaming_response.create(
            "string",
            admin_id="5017691",
            message_type="snoozed",
            snoozed_until=1673609604,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Conversation, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.parts.with_raw_response.create(
                "",
                admin_id="5017691",
                message_type="snoozed",
                snoozed_until=1673609604,
            )

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncIntercom) -> None:
        part = await async_client.conversations.parts.create(
            "string",
            admin_id="5017690",
            message_type="open",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="5017690",
            message_type="open",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.parts.with_streaming_response.create(
            "string",
            admin_id="5017690",
            message_type="open",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Conversation, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.parts.with_raw_response.create(
                "",
                admin_id="5017690",
                message_type="open",
            )

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncIntercom) -> None:
        part = await async_client.conversations.parts.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncIntercom) -> None:
        part = await async_client.conversations.parts.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
            body="Let me pass you over to one of my colleagues.",
        )
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.parts.with_raw_response.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Conversation, part, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.parts.with_streaming_response.create(
            "string",
            admin_id="12345",
            assignee_id="4324241",
            message_type="assignment",
            type="admin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Conversation, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.parts.with_raw_response.create(
                "",
                admin_id="12345",
                assignee_id="4324241",
                message_type="assignment",
                type="admin",
            )
