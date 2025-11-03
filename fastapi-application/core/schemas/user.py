from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    foo: int
    bar: int


class UserCreateSchema(UserBase):
    pass


class UserReadSchema(UserBase):
    # default configured
    # model_config = ConfigDict(
    #     from_attributes=True,
    # )

    id: int
