# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ValidateLoginValidateResponse", "User"]


class User(BaseModel):
    email: Optional[str] = None

    nickname: Optional[str] = None

    user_id: Optional[int] = None


class ValidateLoginValidateResponse(BaseModel):
    success: Optional[int] = None

    user: Optional[User] = None
