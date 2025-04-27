# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blink import Blink, AsyncBlink
from blink.types import Domain
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomainsDomainName:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Blink) -> None:
        domains_domain_name = client.domains_domain_name.list(
            path_domain_name="domain_name",
            query_domain_name="domain_name",
        )
        assert_matches_type(Domain, domains_domain_name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Blink) -> None:
        response = client.domains_domain_name.with_raw_response.list(
            path_domain_name="domain_name",
            query_domain_name="domain_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domains_domain_name = response.parse()
        assert_matches_type(Domain, domains_domain_name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Blink) -> None:
        with client.domains_domain_name.with_streaming_response.list(
            path_domain_name="domain_name",
            query_domain_name="domain_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domains_domain_name = response.parse()
            assert_matches_type(Domain, domains_domain_name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Blink) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_domain_name` but received ''"):
            client.domains_domain_name.with_raw_response.list(
                path_domain_name="",
                query_domain_name="domain_name",
            )


class TestAsyncDomainsDomainName:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBlink) -> None:
        domains_domain_name = await async_client.domains_domain_name.list(
            path_domain_name="domain_name",
            query_domain_name="domain_name",
        )
        assert_matches_type(Domain, domains_domain_name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBlink) -> None:
        response = await async_client.domains_domain_name.with_raw_response.list(
            path_domain_name="domain_name",
            query_domain_name="domain_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domains_domain_name = await response.parse()
        assert_matches_type(Domain, domains_domain_name, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBlink) -> None:
        async with async_client.domains_domain_name.with_streaming_response.list(
            path_domain_name="domain_name",
            query_domain_name="domain_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domains_domain_name = await response.parse()
            assert_matches_type(Domain, domains_domain_name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBlink) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_domain_name` but received ''"):
            await async_client.domains_domain_name.with_raw_response.list(
                path_domain_name="",
                query_domain_name="domain_name",
            )
