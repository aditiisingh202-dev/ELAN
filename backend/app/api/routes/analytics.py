from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.db.database import get_db
from app.core.db.models.recommendation import RecommendationHistory

router = APIRouter()


@router.get("/analytics/top-products")
def top_products(db: Session = Depends(get_db)):

    results = (
        db.query(
            RecommendationHistory.recommended_product,
            func.count().label("count")
        )
        .group_by(RecommendationHistory.recommended_product)
        .all()
    )

    return results


@router.get("/analytics/top-concerns")
def top_concerns(db: Session = Depends(get_db)):

    results = (
        db.query(
            RecommendationHistory.concern,
            func.count().label("count")
        )
        .group_by(RecommendationHistory.concern)
        .all()
    )

    return results