# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["AccessTokenCreateParams", "CredentialsEmailPassword", "CredentialsEmailRefreshToken"]


class CredentialsEmailPassword(TypedDict, total=False):
    email: Required[str]

    password: Required[str]


class CredentialsEmailRefreshToken(TypedDict, total=False):
    email: Required[str]

    refresh_token: Required[str]


AccessTokenCreateParams: TypeAlias = Union[CredentialsEmailPassword, CredentialsEmailRefreshToken]
