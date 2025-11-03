from typing import Sequence
from sqlalchemy import select

from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import UserModel
from core.schemas.user import UserCreateSchema


async def get_all_users(session: AsyncSession) -> Sequence[UserModel]:
    stmt = select(UserModel).order_by(UserModel.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return users


async def create_user(
    session: AsyncSession,
    user_in: UserCreateSchema,
) -> UserModel:
    product = UserModel(**user_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product
