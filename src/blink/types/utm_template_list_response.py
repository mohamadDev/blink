# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["UtmTemplateListResponse", "Object", "ObjectField"]


class ObjectField(BaseModel):
    field_code: Optional[str] = None

    label: Optional[str] = None

    required: Optional[bool] = None

    type: Optional[str] = None


class Object(BaseModel):
    id: Optional[int] = None

    fields: Optional[List[ObjectField]] = None
    """Contains a list of fields that the parent UTM template contains."""

    name: Optional[str] = None


class UtmTemplateListResponse(BaseModel):
    objects: Optional[List[Object]] = None
