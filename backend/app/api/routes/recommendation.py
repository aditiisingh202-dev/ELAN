from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db.database import get_db
from app.core.db.models.recommendation import RecommendationHistory

router = APIRouter()

@router.get("/recommend/{user_name}/{skin_type}/{concern}")
def recommend_product(user_name: str, skin_type: str, concern: str, db: Session = Depends(get_db)):
    # Everything inside the function must be indented by 4 spaces
    recommendations = []
    
    if skin_type.lower() == "oily":
        recommendations = [
            {"product": "Salicylic Acid Cleanser", "score": 95},
            {"product": "Oil Control Moisturizer", "score": 90}
        ]
    elif skin_type.lower() == "dry":
        recommendations = [
            {"product": "Hyaluronic Acid Serum", "score": 95},
            {"product": "Ceramide Cream", "score": 92}
        ]
    else:
        recommendations = [
            {"product": "Gentle Cleanser", "score": 85}
        ]
        
    # TODO: Log this evaluation to your RecommendationHistory model if needed!
    
    return {
        "user_name": user_name,
        "skin_type": skin_type,
        "concern": concern,
        "recommendations": recommendations
    }