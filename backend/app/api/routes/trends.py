from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.db.database import get_db
from app.core.db.models.recommendation import RecommendationHistory

router = APIRouter()


@router.get("/trend-insights")
def trend_insights(db: Session = Depends(get_db)):

    top_concern = (
        db.query(
            RecommendationHistory.concern,
            func.count().label("count")
        )
        .group_by(RecommendationHistory.concern)
        .order_by(func.count().desc())
        .first()
    )

    top_product = (
        db.query(
            RecommendationHistory.recommended_product,
            func.count().label("count")
        )
        .group_by(RecommendationHistory.recommended_product)
        .order_by(func.count().desc())
        .first()
    )

    return {
        "trending_concern": top_concern[0] if top_concern else None,
        "top_product": top_product[0] if top_product else None,
        "market_insight": f"Users are currently focused on {top_concern[0] if top_concern else 'general skincare'} products."
    }