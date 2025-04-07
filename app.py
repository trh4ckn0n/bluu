import streamlit as st
from logo_generator import generate_image
from helpers import get_user_inputs, show_image
import os

# Fonction pour injecter du CSS personnalisé
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Appliquer le CSS personnalisé
local_css("style.css")

# Configuration de l'interface
st.title("Générateur d'Images et Interface Interactive")
st.markdown("Créons quelque chose de magnifique et puissant ensemble.")

# Récupérer les entrées de l'utilisateur
style, color, hidden_word, user_prompt = get_user_inputs()

# Afficher un résumé des choix
st.subheader("Résumé de vos choix")
st.write(f"**Style** : {style}")
st.write(f"**Couleur** : {color}")
st.write(f"**Mot caché** : {hidden_word}")
st.write(f"**Description** : {user_prompt}")

# Bouton pour générer l'image
if st.button("Générer l'Image"):
    st.write("Génération de l'image en cours...")
    image_url = generate_image(user_prompt)
    show_image(image_url)

# Ajout d'un footer personnalisé (optionnel)
st.markdown("""
    <footer style="text-align: center; padding: 10px; font-size: 12px; color: #888;">
        Créé avec ❤️ par trhacknon | <a href="https://www.facebook.com/share/g/SpQ3RD4dqmVHwfFm/" target="_blank">Suivez-moi sur Facebook</a>
    </footer>
""", unsafe_allow_html=True)
