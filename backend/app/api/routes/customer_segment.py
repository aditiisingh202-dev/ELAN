from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db.database import get_db
from app.core.db.models.recommendation import RecommendationHistory

router = APIRouter()


@router.get("/customer-segment/{user_name}")
def customer_segment(
    user_name: str,
    db: Session = Depends(get_db)
):
    history = (
        db.query(RecommendationHistory)
        .filter(
            RecommendationHistory.user_name == user_name
        )
        .all()
    )

    total_recommendations = len(history)

    if total_recommendations >= 5:
        engagement_level = "High"
        loyalty_score = 90

    elif total_recommendations >= 2:
        engagement_level = "Medium"
        loyalty_score = 75

    else:
        engagement_level = "Low"
        loyalty_score = 60

    top_concern = (
        history[-1].concern
        if history
        else "General Skincare"
    )

    segment = f"{top_concern} Care Enthusiast"

    if loyalty_score >= 85:
        strategy = "Retain with premium bundles"

    elif loyalty_score >= 70:
        strategy = "Promote personalized skincare routines"

    else:
        strategy = "Increase engagement with starter kits"

    return {
        "user": user_name,
        "segment": segment,
        "engagement_level": engagement_level,
        "loyalty_score": loyalty_score,
        "recommended_strategy": strategy
    }