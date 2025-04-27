# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from blink import Blink, AsyncBlink
from blink.types import (
    LinkListResponse,
    LinkCreateResponse,
    LinkUpdateResponse,
    LinkRetrieveResponse,
    LinkValidateResponse,
    LinkGetByAliasResponse,
    LinkGetClickedResponse,
    LinkGetRawClicksResponse,
)
from tests.utils import assert_matches_type
from blink._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Blink) -> None:
        link = client.links.create(
            domain_id=0,
            url="url",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Blink) -> None:
        link = client.links.create(
            domain_id=0,
            url="url",
            alias="alias",
            archive_on=0,
            delete_on=0,
            dupe_check=0,
            notes="notes",
            notify_on_click=0,
            override_404_check=0,
            rand_alias_length=0,
            redirect_type=301,
            tags=[
                {
                    "name": "name",
                    "shared": True,
                }
            ],
            utm_fields={
                "field_1": "value1",
                "field_2": "value2",
                "field_3": "value c",
            },
            utm_template_id=0,
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Blink) -> None:
        response = client.links.with_raw_response.create(
            domain_id=0,
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Blink) -> None:
        with client.links.with_streaming_response.create(
            domain_id=0,
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkCreateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Blink) -> None:
        link = client.links.retrieve(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Blink) -> None:
        response = client.links.with_raw_response.retrieve(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Blink) -> None:
        with client.links.with_streaming_response.retrieve(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkRetrieveResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Blink) -> None:
        link = client.links.update(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(LinkUpdateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Blink) -> None:
        link = client.links.update(
            link_id=0,
            domain_id=0,
            body=[
                {
                    "op": "replace",
                    "path": "/alias",
                    "value": "string",
                }
            ],
        )
        assert_matches_type(LinkUpdateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Blink) -> None:
        response = client.links.with_raw_response.update(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkUpdateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Blink) -> None:
        with client.links.with_streaming_response.update(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkUpdateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Blink) -> None:
        link = client.links.list(
            domain_id=0,
        )
        assert_matches_type(LinkListResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Blink) -> None:
        link = client.links.list(
            domain_id=0,
            from_unix=0,
            group_id=0,
            keyword="keyword",
            order="order",
            page=0,
            tag="tag",
            to_unix=0,
            url="url",
            users="users",
        )
        assert_matches_type(LinkListResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Blink) -> None:
        response = client.links.with_raw_response.list(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkListResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Blink) -> None:
        with client.links.with_streaming_response.list(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkListResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_alias(self, client: Blink) -> None:
        link = client.links.get_by_alias(
            path_alias="alias",
            domain_id=0,
            query_alias="alias",
        )
        assert_matches_type(LinkGetByAliasResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_alias(self, client: Blink) -> None:
        response = client.links.with_raw_response.get_by_alias(
            path_alias="alias",
            domain_id=0,
            query_alias="alias",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkGetByAliasResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_alias(self, client: Blink) -> None:
        with client.links.with_streaming_response.get_by_alias(
            path_alias="alias",
            domain_id=0,
            query_alias="alias",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkGetByAliasResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_by_alias(self, client: Blink) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_alias` but received ''"):
            client.links.with_raw_response.get_by_alias(
                path_alias="",
                domain_id=0,
                query_alias="alias",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_clicked(self, client: Blink) -> None:
        link = client.links.get_clicked(
            path_tag="tag",
            domain_id=0,
        )
        assert_matches_type(LinkGetClickedResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_clicked_with_all_params(self, client: Blink) -> None:
        link = client.links.get_clicked(
            path_tag="tag",
            domain_id=0,
            from_unix=0,
            from_user="from_user",
            group_id=0,
            keyword="keyword",
            page=0,
            query_tag="tag",
            to_unix=0,
        )
        assert_matches_type(LinkGetClickedResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_clicked(self, client: Blink) -> None:
        response = client.links.with_raw_response.get_clicked(
            path_tag="tag",
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkGetClickedResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_clicked(self, client: Blink) -> None:
        with client.links.with_streaming_response.get_clicked(
            path_tag="tag",
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkGetClickedResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_clicked(self, client: Blink) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_tag` but received ''"):
            client.links.with_raw_response.get_clicked(
                path_tag="",
                domain_id=0,
            )

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_qr(self, client: Blink, respx_mock: MockRouter) -> None:
        respx_mock.get("/0/links/0/qr").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        link = client.links.get_qr(
            link_id=0,
            domain_id=0,
        )
        assert link.is_closed
        assert link.json() == {"foo": "bar"}
        assert cast(Any, link.is_closed) is True
        assert isinstance(link, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_qr_with_all_params(self, client: Blink, respx_mock: MockRouter) -> None:
        respx_mock.get("/0/links/0/qr").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        link = client.links.get_qr(
            link_id=0,
            domain_id=0,
            format="format",
        )
        assert link.is_closed
        assert link.json() == {"foo": "bar"}
        assert cast(Any, link.is_closed) is True
        assert isinstance(link, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_qr(self, client: Blink, respx_mock: MockRouter) -> None:
        respx_mock.get("/0/links/0/qr").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        link = client.links.with_raw_response.get_qr(
            link_id=0,
            domain_id=0,
        )

        assert link.is_closed is True
        assert link.http_request.headers.get("X-Stainless-Lang") == "python"
        assert link.json() == {"foo": "bar"}
        assert isinstance(link, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_qr(self, client: Blink, respx_mock: MockRouter) -> None:
        respx_mock.get("/0/links/0/qr").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.links.with_streaming_response.get_qr(
            link_id=0,
            domain_id=0,
        ) as link:
            assert not link.is_closed
            assert link.http_request.headers.get("X-Stainless-Lang") == "python"

            assert link.json() == {"foo": "bar"}
            assert cast(Any, link.is_closed) is True
            assert isinstance(link, StreamedBinaryAPIResponse)

        assert cast(Any, link.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_raw_clicks(self, client: Blink) -> None:
        link = client.links.get_raw_clicks(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(LinkGetRawClicksResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_raw_clicks(self, client: Blink) -> None:
        response = client.links.with_raw_response.get_raw_clicks(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkGetRawClicksResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_raw_clicks(self, client: Blink) -> None:
        with client.links.with_streaming_response.get_raw_clicks(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkGetRawClicksResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_validate(self, client: Blink) -> None:
        link = client.links.validate(
            url="url",
        )
        assert_matches_type(LinkValidateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate(self, client: Blink) -> None:
        response = client.links.with_raw_response.validate(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkValidateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate(self, client: Blink) -> None:
        with client.links.with_streaming_response.validate(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkValidateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLinks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.create(
            domain_id=0,
            url="url",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.create(
            domain_id=0,
            url="url",
            alias="alias",
            archive_on=0,
            delete_on=0,
            dupe_check=0,
            notes="notes",
            notify_on_click=0,
            override_404_check=0,
            rand_alias_length=0,
            redirect_type=301,
            tags=[
                {
                    "name": "name",
                    "shared": True,
                }
            ],
            utm_fields={
                "field_1": "value1",
                "field_2": "value2",
                "field_3": "value c",
            },
            utm_template_id=0,
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.with_raw_response.create(
            domain_id=0,
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBlink) -> None:
        async with async_client.links.with_streaming_response.create(
            domain_id=0,
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkCreateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.retrieve(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.with_raw_response.retrieve(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkRetrieveResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBlink) -> None:
        async with async_client.links.with_streaming_response.retrieve(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkRetrieveResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.update(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(LinkUpdateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.update(
            link_id=0,
            domain_id=0,
            body=[
                {
                    "op": "replace",
                    "path": "/alias",
                    "value": "string",
                }
            ],
        )
        assert_matches_type(LinkUpdateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.with_raw_response.update(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkUpdateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBlink) -> None:
        async with async_client.links.with_streaming_response.update(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkUpdateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.list(
            domain_id=0,
        )
        assert_matches_type(LinkListResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.list(
            domain_id=0,
            from_unix=0,
            group_id=0,
            keyword="keyword",
            order="order",
            page=0,
            tag="tag",
            to_unix=0,
            url="url",
            users="users",
        )
        assert_matches_type(LinkListResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.with_raw_response.list(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkListResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBlink) -> None:
        async with async_client.links.with_streaming_response.list(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkListResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_alias(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.get_by_alias(
            path_alias="alias",
            domain_id=0,
            query_alias="alias",
        )
        assert_matches_type(LinkGetByAliasResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_alias(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.with_raw_response.get_by_alias(
            path_alias="alias",
            domain_id=0,
            query_alias="alias",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkGetByAliasResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_alias(self, async_client: AsyncBlink) -> None:
        async with async_client.links.with_streaming_response.get_by_alias(
            path_alias="alias",
            domain_id=0,
            query_alias="alias",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkGetByAliasResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_by_alias(self, async_client: AsyncBlink) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_alias` but received ''"):
            await async_client.links.with_raw_response.get_by_alias(
                path_alias="",
                domain_id=0,
                query_alias="alias",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_clicked(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.get_clicked(
            path_tag="tag",
            domain_id=0,
        )
        assert_matches_type(LinkGetClickedResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_clicked_with_all_params(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.get_clicked(
            path_tag="tag",
            domain_id=0,
            from_unix=0,
            from_user="from_user",
            group_id=0,
            keyword="keyword",
            page=0,
            query_tag="tag",
            to_unix=0,
        )
        assert_matches_type(LinkGetClickedResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_clicked(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.with_raw_response.get_clicked(
            path_tag="tag",
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkGetClickedResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_clicked(self, async_client: AsyncBlink) -> None:
        async with async_client.links.with_streaming_response.get_clicked(
            path_tag="tag",
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkGetClickedResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_clicked(self, async_client: AsyncBlink) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_tag` but received ''"):
            await async_client.links.with_raw_response.get_clicked(
                path_tag="",
                domain_id=0,
            )

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_qr(self, async_client: AsyncBlink, respx_mock: MockRouter) -> None:
        respx_mock.get("/0/links/0/qr").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        link = await async_client.links.get_qr(
            link_id=0,
            domain_id=0,
        )
        assert link.is_closed
        assert await link.json() == {"foo": "bar"}
        assert cast(Any, link.is_closed) is True
        assert isinstance(link, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_qr_with_all_params(self, async_client: AsyncBlink, respx_mock: MockRouter) -> None:
        respx_mock.get("/0/links/0/qr").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        link = await async_client.links.get_qr(
            link_id=0,
            domain_id=0,
            format="format",
        )
        assert link.is_closed
        assert await link.json() == {"foo": "bar"}
        assert cast(Any, link.is_closed) is True
        assert isinstance(link, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_qr(self, async_client: AsyncBlink, respx_mock: MockRouter) -> None:
        respx_mock.get("/0/links/0/qr").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        link = await async_client.links.with_raw_response.get_qr(
            link_id=0,
            domain_id=0,
        )

        assert link.is_closed is True
        assert link.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await link.json() == {"foo": "bar"}
        assert isinstance(link, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_qr(self, async_client: AsyncBlink, respx_mock: MockRouter) -> None:
        respx_mock.get("/0/links/0/qr").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.links.with_streaming_response.get_qr(
            link_id=0,
            domain_id=0,
        ) as link:
            assert not link.is_closed
            assert link.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await link.json() == {"foo": "bar"}
            assert cast(Any, link.is_closed) is True
            assert isinstance(link, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, link.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_raw_clicks(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.get_raw_clicks(
            link_id=0,
            domain_id=0,
        )
        assert_matches_type(LinkGetRawClicksResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_raw_clicks(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.with_raw_response.get_raw_clicks(
            link_id=0,
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkGetRawClicksResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_raw_clicks(self, async_client: AsyncBlink) -> None:
        async with async_client.links.with_streaming_response.get_raw_clicks(
            link_id=0,
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkGetRawClicksResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate(self, async_client: AsyncBlink) -> None:
        link = await async_client.links.validate(
            url="url",
        )
        assert_matches_type(LinkValidateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncBlink) -> None:
        response = await async_client.links.with_raw_response.validate(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkValidateResponse, link, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncBlink) -> None:
        async with async_client.links.with_streaming_response.validate(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkValidateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True
