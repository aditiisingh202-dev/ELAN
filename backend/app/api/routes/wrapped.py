from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.db.database import get_db
from app.core.db.models.recommendation import RecommendationHistory

router = APIRouter()


@router.get("/beauty-wrapped/{user_name}")
def beauty_wrapped(user_name: str, db: Session = Depends(get_db)):

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

    favorite_product = (
        db.query(
            RecommendationHistory.recommended_product,
            func.count().label("count")
        )
        .filter(RecommendationHistory.user_name == user_name)
        .group_by(RecommendationHistory.recommended_product)
        .order_by(func.count().desc())
        .first()
    )

    return {
        "user": user_name,
        "total_recommendations": total_recommendations,
        "top_concern": top_concern[0] if top_concern else None,
        "favorite_product": favorite_product[0] if favorite_product else None,
        "summary": f"{user_name} explored skincare focused on {top_concern[0] if top_concern else 'general care'} and loved {favorite_product[0] if favorite_product else 'beauty essentials'}."
    }