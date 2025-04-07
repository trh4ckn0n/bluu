import os
from dotenv import load_dotenv
import openai

load_dotenv()

# Crée une instance de client une seule fois
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image(prompt):
    """
    Génère une image via DALL·E 3 à partir d'un prompt.
    """
    response = client.images.generate(
        model="dall-e-3",  # dall-e-2 fonctionne aussi selon ton plan OpenAI
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response.data[0].url
