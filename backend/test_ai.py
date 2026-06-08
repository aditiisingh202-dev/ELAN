from app.services.ai_engine import generate_personalized_advice

result = generate_personalized_advice(
    "Aditi",
    "Oily",
    "Acne",
    82
)

print(result)