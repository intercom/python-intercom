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


class TestDataExports:
    strict_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = Intercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_content_data(self, client: Intercom) -> None:
        data_export = client.data_exports.content_data(
            created_at_after=1698309467,
            created_at_before=1698327467,
        )
        assert_matches_type(DataExport, data_export, path=["response"])

    @parametrize
    def test_raw_response_content_data(self, client: Intercom) -> None:
        response = client.data_exports.with_raw_response.content_data(
            created_at_after=1698309467,
            created_at_before=1698327467,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExport, data_export, path=["response"])


class TestAsyncDataExports:
    strict_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
    loose_client = AsyncIntercom(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_content_data(self, client: AsyncIntercom) -> None:
        data_export = await client.data_exports.content_data(
            created_at_after=1698309467,
            created_at_before=1698327467,
        )
        assert_matches_type(DataExport, data_export, path=["response"])

    @parametrize
    async def test_raw_response_content_data(self, client: AsyncIntercom) -> None:
        response = await client.data_exports.with_raw_response.content_data(
            created_at_after=1698309467,
            created_at_before=1698327467,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExport, data_export, path=["response"])
