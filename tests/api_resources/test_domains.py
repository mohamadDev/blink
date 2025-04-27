# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from blink import Blink, AsyncBlink
from blink.types import Domain, DomainDeleteResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Blink) -> None:
        domain = client.domains.create(
            domain="domain",
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Blink) -> None:
        domain = client.domains.create(
            domain="domain",
            default=True,
            homepage="homepage",
            url_404="url_404",
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Blink) -> None:
        response = client.domains.with_raw_response.create(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Blink) -> None:
        with client.domains.with_streaming_response.create(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Blink) -> None:
        domain = client.domains.retrieve(
            0,
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Blink) -> None:
        response = client.domains.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Blink) -> None:
        with client.domains.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Blink) -> None:
        domain = client.domains.update(
            domain_id=0,
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Blink) -> None:
        domain = client.domains.update(
            domain_id=0,
            op="replace",
            path="status",
            value="value",
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Blink) -> None:
        response = client.domains.with_raw_response.update(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Blink) -> None:
        with client.domains.with_streaming_response.update(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Blink) -> None:
        domain = client.domains.list()
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Blink) -> None:
        domain = client.domains.list(
            page=0,
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Blink) -> None:
        response = client.domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Blink) -> None:
        with client.domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Blink) -> None:
        domain = client.domains.delete(
            0,
        )
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Blink) -> None:
        response = client.domains.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Blink) -> None:
        with client.domains.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainDeleteResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncBlink) -> None:
        domain = await async_client.domains.create(
            domain="domain",
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBlink) -> None:
        domain = await async_client.domains.create(
            domain="domain",
            default=True,
            homepage="homepage",
            url_404="url_404",
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBlink) -> None:
        response = await async_client.domains.with_raw_response.create(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBlink) -> None:
        async with async_client.domains.with_streaming_response.create(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBlink) -> None:
        domain = await async_client.domains.retrieve(
            0,
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBlink) -> None:
        response = await async_client.domains.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBlink) -> None:
        async with async_client.domains.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncBlink) -> None:
        domain = await async_client.domains.update(
            domain_id=0,
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBlink) -> None:
        domain = await async_client.domains.update(
            domain_id=0,
            op="replace",
            path="status",
            value="value",
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBlink) -> None:
        response = await async_client.domains.with_raw_response.update(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBlink) -> None:
        async with async_client.domains.with_streaming_response.update(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBlink) -> None:
        domain = await async_client.domains.list()
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBlink) -> None:
        domain = await async_client.domains.list(
            page=0,
        )
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBlink) -> None:
        response = await async_client.domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Domain, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBlink) -> None:
        async with async_client.domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Domain, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncBlink) -> None:
        domain = await async_client.domains.delete(
            0,
        )
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBlink) -> None:
        response = await async_client.domains.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBlink) -> None:
        async with async_client.domains.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainDeleteResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True
