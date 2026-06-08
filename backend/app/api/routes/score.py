from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db.database import get_db
from app.core.db.models.recommendation import RecommendationHistory

router = APIRouter()


@router.get("/skin-score/{user_name}")
def skin_score(user_name: str, db: Session = Depends(get_db)):

    total_recommendations = (
        db.query(RecommendationHistory)
        .filter(RecommendationHistory.user_name == user_name)
        .count()
    )

    score = min(total_recommendations * 20, 100)

    if score >= 80:
        level = "Skincare Expert"
    elif score >= 50:
        level = "Beauty Enthusiast"
    else:
        level = "Beginner"

    return {
        "user": user_name,
        "engagement_score": score,
        "beauty_level": level,
        "ai_message":
        f"{user_name} has a skincare engagement score of {score} and is categorized as a {level}."
    }