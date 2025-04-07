import streamlit as st
from logo_generator import generate_image
from helpers import get_user_inputs, show_image

# Configuration de l'interface
st.title("Générateur d'Images et Interface Interactive")
st.markdown("Créons quelque chose de magnifique et puissant ensemble.")

# Récupérer les entrées de l'utilisateur
style, color, hidden_word, user_prompt = get_user_inputs()

# Afficher un résumé des choix
st.subheader("Résumé de vos choix")
st.write(f"Style : {style}")
st.write(f"Couleur : {color}")
st.write(f"Mot caché : {hidden_word}")
st.write(f"Description : {user_prompt}")

# Bouton pour générer l'image
if st.button("Générer l'Image"):
    image_url = generate_image(user_prompt)
    show_image(image_url)
