# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

__all__ = ["ClickDailyCountsParams"]


class ClickDailyCountsParams(TypedDict, total=False):
    from_unix: int
    """The UTC unix timestamp, query returns values after this date."""

    keyword: str
    """Search link alias, notes, and redirect url for keyword"""

    label_id: Union[str, int]
    """An optional parameter containing the label's ID to query."""

    page: int
    """The page of to query the values from the paginated results."""

    to_unix: int
    """The UTC unix timestamp, query returns values before this date.

    Required if from_unix is specified.
    """

    user_id: Union[str, int]
    """An optional parameter containing the user's ID to query.

    Elevated privileges are required to specify another. Defaults to current user.
    Valid value 'all' is allowed for users of elevated privileges.
    """
