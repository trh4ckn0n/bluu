import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .env
load_dotenv()

# Utiliser la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

import openai

def generate_image(prompt):
    client = openai.OpenAI(api_key="TA_CLE_API")  # ou utilise os.getenv('OPENAI_API_KEY')

    response = client.images.generate(
        model="dall-e-3",  # dall-e-2 possible aussi
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    return response.data[0].url
    
