# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LinkGetQrParams"]


class LinkGetQrParams(TypedDict, total=False):
    domain_id: Required[int]

    format: str
    """png (default), eps, svg"""
