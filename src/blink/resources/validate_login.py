# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import validate_login_validate_params
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
from ..types.validate_login_validate_response import ValidateLoginValidateResponse

__all__ = ["ValidateLoginResource", "AsyncValidateLoginResource"]


class ValidateLoginResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidateLoginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mohamadDev/blink#accessing-raw-response-data-eg-headers
        """
        return ValidateLoginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidateLoginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mohamadDev/blink#with_streaming_response
        """
        return ValidateLoginResourceWithStreamingResponse(self)

    def validate(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValidateLoginValidateResponse:
        """
        Validates login information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/validate_login",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                validate_login_validate_params.ValidateLoginValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateLoginValidateResponse,
        )


class AsyncValidateLoginResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValidateLoginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mohamadDev/blink#accessing-raw-response-data-eg-headers
        """
        return AsyncValidateLoginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidateLoginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mohamadDev/blink#with_streaming_response
        """
        return AsyncValidateLoginResourceWithStreamingResponse(self)

    async def validate(
        self,
        *,
        email: str,
        password: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValidateLoginValidateResponse:
        """
        Validates login information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/validate_login",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                },
                validate_login_validate_params.ValidateLoginValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateLoginValidateResponse,
        )


class ValidateLoginResourceWithRawResponse:
    def __init__(self, validate_login: ValidateLoginResource) -> None:
        self._validate_login = validate_login

        self.validate = to_raw_response_wrapper(
            validate_login.validate,
        )


class AsyncValidateLoginResourceWithRawResponse:
    def __init__(self, validate_login: AsyncValidateLoginResource) -> None:
        self._validate_login = validate_login

        self.validate = async_to_raw_response_wrapper(
            validate_login.validate,
        )


class ValidateLoginResourceWithStreamingResponse:
    def __init__(self, validate_login: ValidateLoginResource) -> None:
        self._validate_login = validate_login

        self.validate = to_streamed_response_wrapper(
            validate_login.validate,
        )


class AsyncValidateLoginResourceWithStreamingResponse:
    def __init__(self, validate_login: AsyncValidateLoginResource) -> None:
        self._validate_login = validate_login

        self.validate = async_to_streamed_response_wrapper(
            validate_login.validate,
        )
