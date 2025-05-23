# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TagCreateParams"]


class TagCreateParams(TypedDict, total=False):
    domain_id: int

    name: str

    notes: str

    shared: bool
