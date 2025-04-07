import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .env
load_dotenv()

# Utiliser la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    """
    Fonction pour générer une image à partir du prompt via l'API OpenAI.
    """
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']
