from typing import Sequence, Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.users.crud.users import get_all_users, create_user
from core.config import settings
from core.models import db_helper, UserModel
from core.schemas.user import UserReadSchema, UserCreateSchema

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)


@router.get(
    "/",
    response_model=list[UserReadSchema],
)
async def get_users_view(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> Sequence[UserModel]:
    return await get_all_users(session=session)


@router.post(
    "/",
    response_model=UserReadSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_user_view(
    user_in: UserCreateSchema,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> UserModel:
    return await create_user(
        session=session,
        user_in=user_in,
    )
