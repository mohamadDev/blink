# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TagListParams"]


class TagListParams(TypedDict, total=False):
    domain_id: Required[int]
    """Domain ID to query by"""

    search: str
    """Tag name to query by"""
