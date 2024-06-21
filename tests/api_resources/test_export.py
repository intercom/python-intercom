# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from python_intercom import Intercom, AsyncIntercom
from python_intercom.types import DataExport

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cancel(self, client: Intercom) -> None:
        export = client.export.cancel(
            "string",
        )
        assert_matches_type(DataExport, export, path=["response"])

    @parametrize
    def test_method_cancel_with_all_params(self, client: Intercom) -> None:
        export = client.export.cancel(
            "string",
            intercom_version="2.11",
        )
        assert_matches_type(DataExport, export, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Intercom) -> None:
        response = client.export.with_raw_response.cancel(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(DataExport, export, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Intercom) -> None:
        with client.export.with_streaming_response.cancel(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(DataExport, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Intercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_identifier` but received ''"):
            client.export.with_raw_response.cancel(
                "",
            )


class TestAsyncExport:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_cancel(self, async_client: AsyncIntercom) -> None:
        export = await async_client.export.cancel(
            "string",
        )
        assert_matches_type(DataExport, export, path=["response"])

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncIntercom) -> None:
        export = await async_client.export.cancel(
            "string",
            intercom_version="2.11",
        )
        assert_matches_type(DataExport, export, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncIntercom) -> None:
        response = await async_client.export.with_raw_response.cancel(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(DataExport, export, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncIntercom) -> None:
        async with async_client.export.with_streaming_response.cancel(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(DataExport, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncIntercom) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_identifier` but received ''"):
            await async_client.export.with_raw_response.cancel(
                "",
            )
