# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blink import Blink, AsyncBlink
from blink.types import ErrorCodeListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestErrorCodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Blink) -> None:
        error_code = client.error_codes.list()
        assert_matches_type(ErrorCodeListResponse, error_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Blink) -> None:
        response = client.error_codes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        error_code = response.parse()
        assert_matches_type(ErrorCodeListResponse, error_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Blink) -> None:
        with client.error_codes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            error_code = response.parse()
            assert_matches_type(ErrorCodeListResponse, error_code, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncErrorCodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBlink) -> None:
        error_code = await async_client.error_codes.list()
        assert_matches_type(ErrorCodeListResponse, error_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBlink) -> None:
        response = await async_client.error_codes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        error_code = await response.parse()
        assert_matches_type(ErrorCodeListResponse, error_code, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBlink) -> None:
        async with async_client.error_codes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            error_code = await response.parse()
            assert_matches_type(ErrorCodeListResponse, error_code, path=["response"])

        assert cast(Any, response.is_closed) is True
