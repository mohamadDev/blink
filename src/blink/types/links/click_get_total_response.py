# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ClickGetTotalResponse"]


class ClickGetTotalResponse(BaseModel):
    scan_count: Optional[int] = None

    total: Optional[int] = None

    unique: Optional[int] = None
