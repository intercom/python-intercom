# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from python_minus_intercom import Intercom, AsyncIntercom
from python_minus_intercom.types import PhoneSwitch

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneCallRedirects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Intercom) -> None:
        phone_call_redirect = client.phone_call_redirects.create(
            phone="+353832345678",
        )
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Intercom) -> None:
        phone_call_redirect = client.phone_call_redirects.create(
            phone="+353832345678",
            custom_attributes={
                "issue_type": "Billing",
                "priority": "High",
            },
            intercom_version="2.11",
        )
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Intercom) -> None:
        response = client.phone_call_redirects.with_raw_response.create(
            phone="+353832345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_call_redirect = response.parse()
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Intercom) -> None:
        with client.phone_call_redirects.with_streaming_response.create(
            phone="+353832345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_call_redirect = response.parse()
            assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhoneCallRedirects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncIntercom) -> None:
        phone_call_redirect = await async_client.phone_call_redirects.create(
            phone="+353832345678",
        )
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncIntercom) -> None:
        phone_call_redirect = await async_client.phone_call_redirects.create(
            phone="+353832345678",
            custom_attributes={
                "issue_type": "Billing",
                "priority": "High",
            },
            intercom_version="2.11",
        )
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncIntercom) -> None:
        response = await async_client.phone_call_redirects.with_raw_response.create(
            phone="+353832345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_call_redirect = await response.parse()
        assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncIntercom) -> None:
        async with async_client.phone_call_redirects.with_streaming_response.create(
            phone="+353832345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_call_redirect = await response.parse()
            assert_matches_type(Optional[PhoneSwitch], phone_call_redirect, path=["response"])

        assert cast(Any, response.is_closed) is True
