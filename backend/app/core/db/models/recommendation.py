from sqlalchemy import Column, Integer, String
from app.core.db.database import Base


class RecommendationHistory(Base):

    __tablename__ = "recommendation_history"

    id = Column(Integer, primary_key=True, index=True)

    user_name = Column(String)
    skin_type = Column(String)
    concern = Column(String)

    recommended_product = Column(String)
    brand = Column(String)