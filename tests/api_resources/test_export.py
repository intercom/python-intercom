# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from intercom import Intercom, AsyncIntercom
from tests.utils import assert_matches_type
from intercom.types import DataExport
from intercom._client import Intercom, AsyncIntercom

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


class TestExport:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_cancel(self, client: Intercom) -> None:
        export = client.export.cancel(
            "string",
        )
        assert_matches_type(DataExport, export, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Intercom) -> None:
        response = client.export.with_raw_response.cancel(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(DataExport, export, path=["response"])


class TestAsyncExport:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_cancel(self, client: AsyncIntercom) -> None:
        export = await client.export.cancel(
            "string",
        )
        assert_matches_type(DataExport, export, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, client: AsyncIntercom) -> None:
        response = await client.export.with_raw_response.cancel(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(DataExport, export, path=["response"])
