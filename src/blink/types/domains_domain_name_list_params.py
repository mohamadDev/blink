# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DomainsDomainNameListParams"]


class DomainsDomainNameListParams(TypedDict, total=False):
    query_domain_name: Required[Annotated[str, PropertyInfo(alias="domain_name")]]
