# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ClickGetTotalParams"]


class ClickGetTotalParams(TypedDict, total=False):
    domain_id: Required[int]

    from_unix: int
    """The UTC unix timestamp, query returns values after this date."""

    to_unix: int
    """The UTC unix timestamp, query returns values before this date.

    Required if from_unix is specified.
    """
