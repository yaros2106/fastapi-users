from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from api.api_v1.fastapi_users_router import (
    current_active_user,
    current_active_superuser,
)
from core.config import settings
from core.models import User
from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"],
)


class MessageResponse(BaseModel):
    messages: list[str]
    user: UserRead


@router.get("", response_model=MessageResponse)
def get_user_messages(
    user: Annotated[
        User,
        Depends(current_active_user),
    ],
):
    return MessageResponse(
        messages=["m1", "m2", "m3", "m4"],
        user=UserRead.model_validate(user),
    )


@router.get(
    "/secrets",
    response_model=MessageResponse,
)
def get_superuser_messages(
    user: Annotated[
        User,
        Depends(current_active_superuser),
    ],
):
    return {
        "messages": ["secret-m1", "secret-m2", "secret-m3", "secret-m4"],
        "user": UserRead.model_validate(user),
    }
