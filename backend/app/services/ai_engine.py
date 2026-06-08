import ollama

def generate_personalized_advice(name, skin_type, concern, beauty_score):
    prompt = f"""
    You are ELAN AI, an expert beauty intelligence assistant.
    
    User Name: {name}
    Skin Type: {skin_type}
    Concern: {concern}
    Beauty Score: {beauty_score}
    
    Give:
    1. Personalized skincare advice
    2. Recommended routine
    3. Improvement suggestions
    4. Future beauty goals
    
    Keep response under 150 words.
    """
    
    try:
        response = ollama.chat(
            model="qwen3:4b",  # Matches your exact 'ollama list' command perfectly
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        print(f"Ollama integration error: {e}")
        return "System matrix processing offline. Reconnecting to local AI core engine..."