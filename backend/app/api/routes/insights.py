from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.db.database import get_db
from app.core.db.models.recommendation import RecommendationHistory

router = APIRouter()


@router.get("/user-insights/{user_name}")
def user_insights(user_name: str, db: Session = Depends(get_db)):

    total_recommendations = (
        db.query(RecommendationHistory)
        .filter(RecommendationHistory.user_name == user_name)
        .count()
    )

    top_concern = (
        db.query(
            RecommendationHistory.concern,
            func.count().label("count")
        )
        .filter(RecommendationHistory.user_name == user_name)
        .group_by(RecommendationHistory.concern)
        .order_by(func.count().desc())
        .first()
    )

    return {
        "user": user_name,
        "total_recommendations": total_recommendations,
        "top_concern": top_concern[0] if top_concern else None
    }