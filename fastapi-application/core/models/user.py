from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
)


from core.models import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):
    pass
