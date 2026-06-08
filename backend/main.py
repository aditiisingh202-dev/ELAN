from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import user
from app.api.routes import recommendation
from app.api.routes import analytics
from app.api.routes import insights
from app.api.routes import wrapped
from app.api.routes import trends
from app.api.routes import dashboard
from app.api.routes import score
from app.api.routes import beauty_score
from app.api.routes import customer_segment
from app.api.routes import personalisation 
# Fix 1: Correct the path to database.py
from app.core.db.database import engine, Base

# Fix 2: Correct the path to your User model (remove '.db')
from app.core.db.models.user import User 
from app.core.db.models.recommendation import RecommendationHistory

# This creates your tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ELAN AI Platform")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",    # <-- Add this line
        "http://127.0.0.1:3001",    # <-- Add this one too just in case
        "http://127.0.0.1:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(recommendation.router)
app.include_router(analytics.router)
app.include_router(insights.router)
app.include_router(wrapped.router)
app.include_router(trends.router)
app.include_router(dashboard.router)
app.include_router(score.router)
app.include_router(beauty_score.router,tags=["Beauty Score"])
app.include_router(customer_segment.router, tags=["Customer Segment"])
app.include_router(personalisation.router,tags=["Hyper Personalization"]
)
