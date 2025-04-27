# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ClickGetHourlyResponse", "Objects"]


class Objects(BaseModel):
    count: Optional[int] = None

    hour: Optional[int] = None

    scan_count: Optional[int] = None
    """The scan count associated with the hour."""


class ClickGetHourlyResponse(BaseModel):
    objects: Optional[Objects] = None
