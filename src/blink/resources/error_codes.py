# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.error_code_list_response import ErrorCodeListResponse

__all__ = ["ErrorCodesResource", "AsyncErrorCodesResource"]


class ErrorCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ErrorCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mohamadDev/blink#accessing-raw-response-data-eg-headers
        """
        return ErrorCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ErrorCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mohamadDev/blink#with_streaming_response
        """
        return ErrorCodesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ErrorCodeListResponse:
        """Returns a list of available error codes.

        The code is guaranteed to stay the
        same. The message and description may change.
        """
        return self._get(
            "/error_codes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ErrorCodeListResponse,
        )


class AsyncErrorCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncErrorCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mohamadDev/blink#accessing-raw-response-data-eg-headers
        """
        return AsyncErrorCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncErrorCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mohamadDev/blink#with_streaming_response
        """
        return AsyncErrorCodesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ErrorCodeListResponse:
        """Returns a list of available error codes.

        The code is guaranteed to stay the
        same. The message and description may change.
        """
        return await self._get(
            "/error_codes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ErrorCodeListResponse,
        )


class ErrorCodesResourceWithRawResponse:
    def __init__(self, error_codes: ErrorCodesResource) -> None:
        self._error_codes = error_codes

        self.list = to_raw_response_wrapper(
            error_codes.list,
        )


class AsyncErrorCodesResourceWithRawResponse:
    def __init__(self, error_codes: AsyncErrorCodesResource) -> None:
        self._error_codes = error_codes

        self.list = async_to_raw_response_wrapper(
            error_codes.list,
        )


class ErrorCodesResourceWithStreamingResponse:
    def __init__(self, error_codes: ErrorCodesResource) -> None:
        self._error_codes = error_codes

        self.list = to_streamed_response_wrapper(
            error_codes.list,
        )


class AsyncErrorCodesResourceWithStreamingResponse:
    def __init__(self, error_codes: AsyncErrorCodesResource) -> None:
        self._error_codes = error_codes

        self.list = async_to_streamed_response_wrapper(
            error_codes.list,
        )
