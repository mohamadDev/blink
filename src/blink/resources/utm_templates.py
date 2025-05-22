# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import utm_template_list_params
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
from ..types.utm_template_list_response import UtmTemplateListResponse

__all__ = ["UtmTemplatesResource", "AsyncUtmTemplatesResource"]


class UtmTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UtmTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mohamadDev/blink#accessing-raw-response-data-eg-headers
        """
        return UtmTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UtmTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mohamadDev/blink#with_streaming_response
        """
        return UtmTemplatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UtmTemplateListResponse:
        """
        Returns a list of available UTM templates

        Args:
          domain_id: Domain ID to query by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/utm_templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"domain_id": domain_id}, utm_template_list_params.UtmTemplateListParams),
            ),
            cast_to=UtmTemplateListResponse,
        )


class AsyncUtmTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUtmTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mohamadDev/blink#accessing-raw-response-data-eg-headers
        """
        return AsyncUtmTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUtmTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mohamadDev/blink#with_streaming_response
        """
        return AsyncUtmTemplatesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UtmTemplateListResponse:
        """
        Returns a list of available UTM templates

        Args:
          domain_id: Domain ID to query by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/utm_templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"domain_id": domain_id}, utm_template_list_params.UtmTemplateListParams
                ),
            ),
            cast_to=UtmTemplateListResponse,
        )


class UtmTemplatesResourceWithRawResponse:
    def __init__(self, utm_templates: UtmTemplatesResource) -> None:
        self._utm_templates = utm_templates

        self.list = to_raw_response_wrapper(
            utm_templates.list,
        )


class AsyncUtmTemplatesResourceWithRawResponse:
    def __init__(self, utm_templates: AsyncUtmTemplatesResource) -> None:
        self._utm_templates = utm_templates

        self.list = async_to_raw_response_wrapper(
            utm_templates.list,
        )


class UtmTemplatesResourceWithStreamingResponse:
    def __init__(self, utm_templates: UtmTemplatesResource) -> None:
        self._utm_templates = utm_templates

        self.list = to_streamed_response_wrapper(
            utm_templates.list,
        )


class AsyncUtmTemplatesResourceWithStreamingResponse:
    def __init__(self, utm_templates: AsyncUtmTemplatesResource) -> None:
        self._utm_templates = utm_templates

        self.list = async_to_streamed_response_wrapper(
            utm_templates.list,
        )
