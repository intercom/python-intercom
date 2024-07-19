# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types.shared import Conversation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRunAssignmentRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        run_assignment_rule = client.conversations.run_assignment_rules.create(
            id="123",
        )
        assert_matches_type(Conversation, run_assignment_rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        run_assignment_rule = client.conversations.run_assignment_rules.create(
            id="123",
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, run_assignment_rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.conversations.run_assignment_rules.with_raw_response.create(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run_assignment_rule = response.parse()
        assert_matches_type(Conversation, run_assignment_rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.conversations.run_assignment_rules.with_streaming_response.create(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run_assignment_rule = response.parse()
            assert_matches_type(Conversation, run_assignment_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.run_assignment_rules.with_raw_response.create(
                id="",
            )


class TestAsyncRunAssignmentRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        run_assignment_rule = await async_client.conversations.run_assignment_rules.create(
            id="123",
        )
        assert_matches_type(Conversation, run_assignment_rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        run_assignment_rule = await async_client.conversations.run_assignment_rules.create(
            id="123",
            intercom_version="2.11",
        )
        assert_matches_type(Conversation, run_assignment_rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.conversations.run_assignment_rules.with_raw_response.create(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run_assignment_rule = await response.parse()
        assert_matches_type(Conversation, run_assignment_rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.conversations.run_assignment_rules.with_streaming_response.create(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run_assignment_rule = await response.parse()
            assert_matches_type(Conversation, run_assignment_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.run_assignment_rules.with_raw_response.create(
                id="",
            )
