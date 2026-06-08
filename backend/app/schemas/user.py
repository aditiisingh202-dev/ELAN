from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    skin_type: str
    concern: str
    favorite_category: str


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True