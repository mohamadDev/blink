# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LinkGetByAliasParams"]


class LinkGetByAliasParams(TypedDict, total=False):
    domain_id: Required[int]

    query_alias: Required[Annotated[str, PropertyInfo(alias="alias")]]
