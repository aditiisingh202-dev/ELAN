from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db.database import get_db
from app.core.db.models.recommendation import RecommendationHistory

router = APIRouter()


@router.get("/beauty-score/{user_name}")
def get_beauty_score(
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

    beauty_score = min(
        50 + (total_recommendations * 10),
        100
    )

    customer_health = min(
        60 + (total_recommendations * 8),
        100
    )

    if total_recommendations >= 5:
        retention_risk = "Low"
    elif total_recommendations >= 2:
        retention_risk = "Medium"
    else:
        retention_risk = "High"

    predicted_next_concern = "Pigmentation"

    return {
        "user": user_name,
        "beauty_score": beauty_score,
        "customer_health": customer_health,
        "retention_risk": retention_risk,
        "predicted_next_concern": predicted_next_concern
    }