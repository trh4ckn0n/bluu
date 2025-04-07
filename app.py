import streamlit as st
from logo_generator import generate_image
from helpers import get_user_inputs, show_image
import time



# Fonction pour afficher un loader personnalisé
def display_loader():
    with st.spinner("Génération de l'image..."):
        time.sleep(3)  # Simuler un délai pour l'exemple

# Bouton pour générer l'image avec le loader

# Charger le CSS personnalisé
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Appliquer le CSS personnalisé
local_css("style.css")

# Récupérer les entrées de l'utilisateur depuis helpers.py
style, color, hidden_word, user_prompt = get_user_inputs()

# Sidebar avec options
st.sidebar.title("Options")
style = st.sidebar.selectbox("Choisissez un style", 
                             ["Cyberpunk", "Futuristic", "Hacker Underground", "Artistique", "Autre"],
                             index=["Cyberpunk", "Futuristic", "Hacker Underground", "Artistique", "Autre"].index(style), 
                             key="style_selectbox")

color = st.sidebar.selectbox("Sélectionnez la couleur dominante", 
                             ["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", "Autre"],
                             index=["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", "Autre"].index(color),
                             key="color_selectbox")

hidden_word = st.sidebar.text_input("Quel mot voulez-vous inclure de manière cachée ?", value=hidden_word, key="hidden_word_input")

user_prompt = st.sidebar.text_area("Description du logo", value=user_prompt, key="user_prompt_textarea")

st.sidebar.markdown("**Résumé de vos choix**")
st.sidebar.write(f"Style : {style}")
st.sidebar.write(f"Couleur : {color}")
st.sidebar.write(f"Mot caché : {hidden_word}")
st.sidebar.write(f"Description : {user_prompt}")

# Titre principal et description
st.title("Générateur d'Images et Interface Interactive")
st.markdown("Créons quelque chose de magnifique et puissant ensemble.")
st.subheader("Résumé de vos choix")
st.write(f"Style : {style}")
st.write(f"Couleur : {color}")
st.write(f"Mot caché : {hidden_word}")
st.write(f"Description : {user_prompt}")

# Utilisation d'un radio button pour simuler des onglets
tab = st.radio("Choisissez une section", ["Générer", "Paramètres"], key="tabs_radio")

if tab == "Générer":
    st.subheader("Générer une image")
    if st.button("Générer l'Image", key="generate_button"):
        display_loader()  # Affichage du loader
        image_url = generate_image(user_prompt)
        show_image(image_url)

elif tab == "Paramètres":
    st.subheader("Paramètres de personnalisation")
    size = st.slider("Sélectionner la taille de l'image", 100, 2000, 1024, key="size_slider")
    st.write(f"Taille de l'image : {size}x{size}")
    st.write("Modifiez les paramètres ci-dessus pour personnaliser votre image.")

# Footer
st.markdown("""
    <footer style="text-align: center; padding: 10px; font-size: 12px; color: #888;">
        Créé avec ❤️ par trhacknon | <a href="https://www.facebook.com/share/g/SpQ3RD4dqmVHwfFm/" target="_blank">Suivez-moi sur Facebook</a>
    </footer>
""", unsafe_allow_html=True)

# Fonction pour afficher un loader pendant le traitement
def display_loader():
    with st.spinner("Génération de l'image..."):
        time.sleep(3)  # Simuler un délai pour l'exemple
