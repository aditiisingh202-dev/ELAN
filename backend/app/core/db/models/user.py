from sqlalchemy import Column, Integer, String
from app.core.db.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String, unique=True)

    skin_type = Column(String)
    concern = Column(String)
    favorite_category = Column(String)