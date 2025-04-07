import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .env
load_dotenv()

# Utiliser la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt, size=1024):
    """
    Fonction pour générer une image à partir du prompt via l'API OpenAI.
    La taille doit être une valeur parmi : 256, 512, 1024.
    """
    # Sécurité : forcer la taille à une valeur valide pour l'API DALL·E
    if size not in [256, 512, 1024]:
        size = 1024  # fallback

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=f"{size}x{size}"
    )
    return response['data'][0]['url']
