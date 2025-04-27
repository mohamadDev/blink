# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ErrorCodeListResponse", "Object"]


class Object(BaseModel):
    code: Optional[int] = None

    description: Optional[str] = None

    message: Optional[str] = None


class ErrorCodeListResponse(BaseModel):
    objects: Optional[List[Object]] = None
