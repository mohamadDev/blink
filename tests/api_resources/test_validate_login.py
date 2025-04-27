# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blink import Blink, AsyncBlink
from blink.types import ValidateLoginValidateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidateLogin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_validate(self, client: Blink) -> None:
        validate_login = client.validate_login.validate(
            email="bud@smartlinker.email",
            password="password",
        )
        assert_matches_type(ValidateLoginValidateResponse, validate_login, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate(self, client: Blink) -> None:
        response = client.validate_login.with_raw_response.validate(
            email="bud@smartlinker.email",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_login = response.parse()
        assert_matches_type(ValidateLoginValidateResponse, validate_login, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate(self, client: Blink) -> None:
        with client.validate_login.with_streaming_response.validate(
            email="bud@smartlinker.email",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_login = response.parse()
            assert_matches_type(ValidateLoginValidateResponse, validate_login, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncValidateLogin:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate(self, async_client: AsyncBlink) -> None:
        validate_login = await async_client.validate_login.validate(
            email="bud@smartlinker.email",
            password="password",
        )
        assert_matches_type(ValidateLoginValidateResponse, validate_login, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncBlink) -> None:
        response = await async_client.validate_login.with_raw_response.validate(
            email="bud@smartlinker.email",
            password="password",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_login = await response.parse()
        assert_matches_type(ValidateLoginValidateResponse, validate_login, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncBlink) -> None:
        async with async_client.validate_login.with_streaming_response.validate(
            email="bud@smartlinker.email",
            password="password",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_login = await response.parse()
            assert_matches_type(ValidateLoginValidateResponse, validate_login, path=["response"])

        assert cast(Any, response.is_closed) is True
