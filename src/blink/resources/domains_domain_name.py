# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import domains_domain_name_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.domain import Domain

__all__ = ["DomainsDomainNameResource", "AsyncDomainsDomainNameResource"]


class DomainsDomainNameResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainsDomainNameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blink-python#accessing-raw-response-data-eg-headers
        """
        return DomainsDomainNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsDomainNameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blink-python#with_streaming_response
        """
        return DomainsDomainNameResourceWithStreamingResponse(self)

    def list(
        self,
        path_domain_name: str,
        *,
        query_domain_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Domain:
        """
        Returns a list of the user's requested domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_domain_name:
            raise ValueError(f"Expected a non-empty value for `path_domain_name` but received {path_domain_name!r}")
        return self._get(
            f"/domains?domain_name={path_domain_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"query_domain_name": query_domain_name},
                    domains_domain_name_list_params.DomainsDomainNameListParams,
                ),
            ),
            cast_to=Domain,
        )


class AsyncDomainsDomainNameResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainsDomainNameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/blink-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainsDomainNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsDomainNameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/blink-python#with_streaming_response
        """
        return AsyncDomainsDomainNameResourceWithStreamingResponse(self)

    async def list(
        self,
        path_domain_name: str,
        *,
        query_domain_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Domain:
        """
        Returns a list of the user's requested domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_domain_name:
            raise ValueError(f"Expected a non-empty value for `path_domain_name` but received {path_domain_name!r}")
        return await self._get(
            f"/domains?domain_name={path_domain_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_domain_name": query_domain_name},
                    domains_domain_name_list_params.DomainsDomainNameListParams,
                ),
            ),
            cast_to=Domain,
        )


class DomainsDomainNameResourceWithRawResponse:
    def __init__(self, domains_domain_name: DomainsDomainNameResource) -> None:
        self._domains_domain_name = domains_domain_name

        self.list = to_raw_response_wrapper(
            domains_domain_name.list,
        )


class AsyncDomainsDomainNameResourceWithRawResponse:
    def __init__(self, domains_domain_name: AsyncDomainsDomainNameResource) -> None:
        self._domains_domain_name = domains_domain_name

        self.list = async_to_raw_response_wrapper(
            domains_domain_name.list,
        )


class DomainsDomainNameResourceWithStreamingResponse:
    def __init__(self, domains_domain_name: DomainsDomainNameResource) -> None:
        self._domains_domain_name = domains_domain_name

        self.list = to_streamed_response_wrapper(
            domains_domain_name.list,
        )


class AsyncDomainsDomainNameResourceWithStreamingResponse:
    def __init__(self, domains_domain_name: AsyncDomainsDomainNameResource) -> None:
        self._domains_domain_name = domains_domain_name

        self.list = async_to_streamed_response_wrapper(
            domains_domain_name.list,
        )
