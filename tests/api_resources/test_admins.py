# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Optional

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import AdminList
from intercom._client import Intercom, AsyncIntercom
from intercom.types.shared import Admin

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestAdmins:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Intercom) -> None:
        admin = client.admins.retrieve(
            0,
        )
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Intercom) -> None:
        response = client.admins.with_raw_response.retrieve(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    def test_method_list(self, client: Intercom) -> None:
        admin = client.admins.list()
        assert_matches_type(AdminList, admin, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Intercom) -> None:
        response = client.admins.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminList, admin, path=["response"])


class TestAsyncAdmins:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncIntercom) -> None:
        admin = await client.admins.retrieve(
            0,
        )
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncIntercom) -> None:
        response = await client.admins.with_raw_response.retrieve(
            0,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(Optional[Admin], admin, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncIntercom) -> None:
        admin = await client.admins.list()
        assert_matches_type(AdminList, admin, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncIntercom) -> None:
        response = await client.admins.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminList, admin, path=["response"])
