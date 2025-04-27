# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["LinkValidateResponse", "Object"]


class Object(BaseModel):
    url: Optional[str] = None


class LinkValidateResponse(BaseModel):
    objects: Optional[List[Object]] = None
