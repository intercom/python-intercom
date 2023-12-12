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


class TestRunAssignmentRules:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        run_assignment_rule = client.conversations.run_assignment_rules.create(
            "string",
        )
        assert_matches_type(Conversation, run_assignment_rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.conversations.run_assignment_rules.with_raw_response.create(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run_assignment_rule = response.parse()
        assert_matches_type(Conversation, run_assignment_rule, path=["response"])


class TestAsyncRunAssignmentRules:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncIntercom) -> None:
        run_assignment_rule = await client.conversations.run_assignment_rules.create(
            "string",
        )
        assert_matches_type(Conversation, run_assignment_rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncIntercom) -> None:
        response = await client.conversations.run_assignment_rules.with_raw_response.create(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run_assignment_rule = response.parse()
        assert_matches_type(Conversation, run_assignment_rule, path=["response"])
