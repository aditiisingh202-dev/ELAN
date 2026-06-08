from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db.database import get_db
from app.core.db.models.recommendation import RecommendationHistory
from app.services.ai_engine import generate_personalized_advice

router = APIRouter()

# CHANGED: The route path now precisely matches your React frontend's fetch call
@router.get("/recommend/{user_name}/{skin_type}/{concern}")
def hyper_personalization(
    user_name: str,
    skin_type: str,
    concern: str,
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
        customer_tier = "Premium"
        recommendations = [
            "La Roche-Posay Effaclar",
            "Clinique Anti-Blemish",
            "Kiehl's Ultra Facial Cream"
        ]

    elif total_recommendations >= 2:
        customer_tier = "Growth"
        recommendations = [
            "CeraVe Cleanser",
            "The Ordinary Niacinamide",
            "Cetaphil Moisturizer"
        ]

    else:
        customer_tier = "Starter"
        recommendations = [
            "Simple Face Wash",
            "Minimalist Serum",
            "Pond's Light Moisturizer"
        ]

    beauty_score = min(50 + (total_recommendations * 10), 100)

    # CHANGED: Replaced hardcoded "Unknown" and "General Beauty" with real values from the URL path!
    ai_advice = generate_personalized_advice(
        name=user_name,
        skin_type=skin_type,
        concern=concern,
        beauty_score=beauty_score
    )

    return {
        "status": "success",
        "user_name": user_name,
        "skin_type": skin_type,
        "top_concern": concern,
        "customer_tier": customer_tier,
        "beauty_score": beauty_score,
        "personalized_products": recommendations,
        "strategy": f"Target {customer_tier} customer journey",
        "ai_advice": ai_advice  # This feeds right into your React display state variable!
    }